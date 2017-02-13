# -*- coding: utf-8 -*-
from ..util.shelve_tool import champion_full
from .item_model import Item, Rune


def compute(b, g, n1, n2=1):
    return b + g * (n1 - n2) * (0.6675 + 0.0175 * (n1 + n2))


class DPS(object):
    '''物理dps属性的描述符，在生成champion实例后可以通过obj.raw_physical_dps
    直接获得物理输出。还可以根据输出对象的护甲和生命，获得实际输出（是输出对象
    生命的百分比）。但是需要设置对象的护甲和生命，设置之后就能通过obj.effective_physical_dps
    获得结果。这些数值会在装备更新，或者等级更新后，重新计算。

    设置的方法

    >> obj.effective_physical_dps = dict(armor=100, hp=2000)

    设置之后，直接调用即可

    >> obj.effective_physical_dps
    '''

    def get_raw_dps(self):
        '''计算公式 attackdamage * attackspeed * (1 + critdamage * crit)'''
        dps = self.damage * self.frequency * \
            (1 + self.critdamage * self.crit)
        dps *= (100 / (100 + self.armor))
        dps /= self.hp
        return dps

    def __get__(self, obj, typ):
        if not hasattr(self, 'hp') or getattr(self, 'damage') != getattr(obj, 'attackdamage'):
            self.__set__(obj, {})
        return self.get_raw_dps()

    def __set__(self, obj, dic):
        self.damage = getattr(obj, 'attackdamage')
        self.frequency = getattr(obj, 'attackspeed')
        self.crit = getattr(obj, 'crit')
        self.critdamage = getattr(obj, 'critdamage')

        self.armor = dic.get('armor', 0)
        self.hp = dic.get('hp', 1)


class Champion(object):
    '''
    英雄的基础属性
    '''
    raw_physical_dps = DPS()
    effective_physical_dps = DPS()

    def __init__(self, name, level=1, *itemlist, **stats):
        self.name = name
        self.level = level
        self.itemlist = list[itemlist] if itemlist else []
        self.stats = stats or champion_full.get_attr_from_item(name, 'stats')
        for k, v in self.stats.items():
            setattr(self, k, v)

        self.critdamage = 1  # 基础暴击伤害系数1
        self.magicdamage = 0  # 初始法强
        self.magicdamageperlevel = 0  # 初始法强增长
        self.magicpenetration = 0  # 初始魔抗穿透
        # 需要测试增长的方式，是否遵循compute函数中的方式
        self.magicpenetrationperlevel = 0  # 初始魔抗穿透增长

        self.lifesteal = 0  # 初始生命偷取
        self.spellvamp = 0  # 初始法术吸血
        self.pbap = 0  # 初始百分比额外护甲无视
        self.lilethalityt = 0  # 初始护甲穿透
        self.cooldown = 0  # 初始冷却缩减
        self.cooldownperlevel = 0  # 初始每级冷却缩减

        # 基础攻速
        self.BAS = self.attackspeed = 0.625 / (1 + self.attackspeedoffset)

        # 第一次根据等级初始化
        self.update_lv(self.level)

    def _update_attr(self, attr, lv):
        '''计算某一属性在等级Lv时候的数值，可以用来更新
        hp,mp,armor,spellblock,attackdamage'''
        assert 1 <= lv <= 18, "输入的等级'{0}'超出范围，要求lv属于[1:18]".format(lv)
        assert attr in ["hp", "mp", "armor", "spellblock",
                        "attackdamage"], "无法更新的属性'{0}'".format(attr)
        b = getattr(self, attr)
        g = getattr(self, attr + "perlevel")
        val = compute(b, g, lv, self.level)
        setattr(self, attr, val)

    def update_lv(self, level):
        '''更新英雄在等级level候的属性(没有将装备囊括在内),
        通过调用self._update_attr完成'''
        update_list = ["hp", "mp", "armor",
                       "spellblock", "attackdamage"]
        [self._update_attr(attr, level) for attr in update_list]

        # 攻速计算方法: 基础攻速 * 攻速成长
        self.attackspeed = self.BAS * \
            compute(1, self.attackspeedperlevel / 100, level)

        # 冷却缩减计算
        self.cooldown += (level + 1 - self.level) * self.cooldownperlevel
        self.magicdamage += (level + 1 - self.level) * self.magicdamageperlevel

        self.level = level

    def _build_with_key(self, item_key, map=11):
        '''默认地图为召唤师峡谷，用item_key选择其中的装备，为召唤师更新属性。

        TODO:
            根据MAP属性，选择装备数据源
        '''
        Item(item_key).update_champion(self)

    def _build_rune_with_key(self, rune_key):
        Rune(rune_key).update_champion(self)

    def build(self, *item_keys, map=11):
        for key in item_keys:
            self._build_with_key(key, map)

    def build_runes(self, *rune_keys):
        for key in rune_keys:
            self._build_rune_with_key(key)
