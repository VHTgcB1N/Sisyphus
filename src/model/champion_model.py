# -*- coding: utf-8 -*-
from util.shelve_tool import champion_full


def compute(b, g, n1, n2=1):
    return b + g * (n1 - n2) * (0.6675 + 0.0175 * (n1 + n2))


class Champion(object):
    '''
    英雄的基础属性
    '''

    def __init__(self, name, level=1, *itemlist, **stats):
        self.name = name
        self.level = level
        self.itemlist = list[itemlist] if itemlist else []
        self.stats = stats or champion_full.get_attr_from_item(name, 'stats')
        for k, v in self.stats.items():
            setattr(self, k, v)
        self.critdamage = 1

        # 基础攻速
        self.BAS = self.attackspeed = 0.625 / (1 + self.attackspeedoffset)

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
        update_list = ["hp", "mp", "armor", "spellblock", "attackdamage"]
        [self._update_attr(attr, level) for attr in update_list]
        self.level = level

        # 攻速计算方法: 基础攻速 * 攻速成长
        self.attackspeed = self.BAS * \
            compute(1, self.attackspeedperlevel / 100, level)

    def value_dps(self):
        '''计算公式 attackdamage * attackspeed * (1 + critdamage * crit)'''
        dps = self.attackdamage * self.attackspeed * \
            (1 + self.critdamage * self.crit)
        self.phiscal_dps = dps
        return dps
