import re
from ..util.shelve_tool import item_at_map11, rune_full


class AbstractItem(object):

    def get_item_dict(self):
        ''' '''
        return self._item_shelve.get_item_with_key(self.name)

    def update_champion(self, champion):
        '''根据物品的相关数据，更新champion的属性，

        champion:必须是Champion的实例

        '''
        for stat in self.stats.keys():
            fun = getattr(self, '_{0}'.format(stat), self._donothing)
            para = self.stats[stat]
            fun(champion, para, stat)

    def _donothing(self, champion, para, stat):
        print(stat, 'is requiring')

    def _FlatArmorMod(self, champion, para, stat):
        champion.armor += para

    def _FlatPhysicalDamageMod(self, champion, para, stat):
        champion.attackdamage += para

    def _PercentAttackSpeedMod(self, champion, para, stat):
        champion.attackspeed += champion.BAS * para

    def _FlatCritChanceMod(self, champion, para, stat):
        champion.crit += para

    def _FlatCritDamage(self, champion, para, stat):
        champion.critdamage += para

    def _FlatMovementSpeedMod(self, champion, para, stat):
        champion.movespeed += para

    def _FlatHPPoolMod(self, champion, para, stat):
        champion.hp += para

    def _FlatMagicDamageMod(self, champion, para, stat):
        champion.magicdamage += para

    def _FlatSpellBlockMod(self, champion, para, stat):
        champion.spellblock += para

    def _PercentLifeStealMod(self, champion, para, stat):
        champion.lifesteal += para

    def _PercentBonusArmorPenetration(self, champion, para, stat):
        champion.pbap += para

    def _FlatArmorPenetration(self, champion, para, stat):
        champion.fap += para

    def _rFlatMagicDamageModPerLevel(self, champion, para, stat):
        champion.magicdamageperlevel += para

    def _rPercentMagicPenetrationMod(self, champion, para, stat):
        raise(Exception(self._rPercentMagicPenetrationMod.__name__ + ' not impleted'))

    def _PercentMPPoolMod(self, champion, para, stat):
        raise(Exception(self._PercentMPPoolMod.__name__ + ' not impleted'))

    def _rFlatMagicPenetrationModPerLevel(self, champion, para, stat):
        champion.magicpenetrationperlevel += para

    def _PercentArmorMod(self, champion, para, stat):
        raise(Exception(self._PercentArmorMod.__name__ + ' not impleted'))

    def _PercentSpellBlockMod(self, champion, para, stat):
        raise(Exception(self._PercentSpellBlockMod.__name__ + ' not impleted'))

    def _rPercentAttackSpeedModPerLevel(self, champion, para, stat):
        raise(Exception(self._rPercentAttackSpeedModPerLevel.__name__ + ' not impleted'))

    def _rFlatSpellBlockModPerLevel(self, champion, para, stat):
        champion.spellblockperlevel += para

    def _rFlatArmorModPerLevel(self, champion, para, stat):
        champion.armorperlevel += para

    def _PercentPhysicalDamageMod(self, champion, para, stat):
        raise(Exception(self._PercentPhysicalDamageMod.__name__ + ' not impleted'))

    def _PercentMovementSpeedMod(self, champion, para, stat):
        champion.movespeed *= 1 + para

    def _FlatEnergyRegenMod(self, champion, para, stat):
        champion.mpregen += para

    def _rFlatEnergyModPerLevel(self, champion, para, stat):
        champion.mpperlevel += para

    def _rFlatArmorPenetrationMod(self, champion, para, stat):
        raise(Exception(self._rFlatArmorPenetrationMod.__name__ + ' not impleted'))

    def _PercentDodgeMod(self, champion, para, stat):
        raise(Exception(self._PercentDodgeMod.__name__ + ' not impleted'))

    def _rFlatMovementSpeedModPerLevel(self, champion, para, stat):
        raise(Exception(self._rFlatMovementSpeedModPerLevel.__name__ + ' not impleted'))

    def _rPercentArmorPenetrationMod(self, champion, para, stat):
        raise(Exception(self._rPercentArmorPenetrationMod.__name__ + ' not impleted'))

    def _rFlatDodgeModPerLevel(self, champion, para, stat):
        raise(Exception(self._rFlatDodgeModPerLevel.__name__ + ' not impleted'))

    def _PercentSpellVampMod(self, champion, para, stat):
        champion.spellvamp += para

    def _rPercentMovementSpeedModPerLevel(self, champion, para, stat):
        raise(Exception(self._rPercentMovementSpeedModPerLevel.__name__ + ' not impleted'))

    def _FlatEnergyPoolMod(self, champion, para, stat):
        champion.mp += para

    def _rFlatMagicPenetrationMod(self, champion, para, stat):
        champion.magicpenetration += para

    def _PercentHPRegenMod(self, champion, para, stat):
        raise(Exception(self._PercentHPRegenMod.__name__ + ' not impleted'))

    def _rPercentMagicPenetrationModPerLevel(self, champion, para, stat):
        raise(Exception(
            self._rPercentMagicPenetrationModPerLevel.__name__ + ' not impleted'))

    def _rFlatDodgeMod(self, champion, para, stat):
        raise(Exception(self._rFlatDodgeMod.__name__ + ' not impleted'))

    def _rFlatPhysicalDamageModPerLevel(self, champion, para, stat):
        champion.attackdamageperlevel += para

    def _rFlatCritDamageModPerLevel(self, champion, para, stat):
        raise(Exception(self._rFlatCritDamageModPerLevel.__name__ + ' not impleted'))

    def _PercentEXPBonus(self, champion, para, stat):
        print(self._PercentEXPBonus.__name__ + ' not impleted')

    def _rPercentArmorPenetrationModPerLevel(self, champion, para, stat):
        raise(Exception(
            self._rPercentArmorPenetrationModPerLevel.__name__ + ' not impleted'))

    def _rPercentTimeDeadMod(self, champion, para, stat):
        print(self._rPercentTimeDeadMod.__name__ + ' not impleted')

    def _rFlatMPModPerLevel(self, champion, para, stat):
        champion.mpperlevel += para

    def _rFlatEnergyRegenModPerLevel(self, champion, para, stat):
        champion.mpregenperlevel += para

    def _FlatAttackSpeedMod(self, champion, para, stat):
        raise(Exception(self._FlatAttackSpeedMod.__name__ + ' not impleted'))

    def _PercentMagicDamageMod(self, champion, para, stat):
        raise(Exception(self._PercentMagicDamageMod.__name__ + ' not impleted'))

    def _FlatMPRegenMod(self, champion, para, stat):
        champion.mpregen += para

    def _rFlatHPModPerLevel(self, champion, para, stat):
        champion.hpperlevel += para

    def _PercentHPPoolMod(self, champion, para, stat):
        print('percethppoolmod to be tested')

    def _PercentCritChanceMod(self, champion, para, stat):
        raise(Exception(self._PercentCritChanceMod.__name__ + ' not impleted'))

    def _rFlatCritChanceModPerLevel(self, champion, para, stat):
        raise(Exception(self._rFlatCritChanceModPerLevel.__name__ + ' not impleted'))

    def _PercentMPRegenMod(self, champion, para, stat):
        raise(Exception(self._PercentMPRegenMod.__name__ + ' not impleted'))

    def _FlatEXPBonus(self, champion, para, stat):
        raise(Exception(self._FlatEXPBonus.__name__ + ' not impleted'))

    def _rFlatGoldPer10Mod(self, champion, para, stat):
        print(self._rFlatGoldPer10Mod.__name__ + ' not impleted')

    def _FlatMPPoolMod(self, champion, para, stat):
        champion.mp += para

    def _rFlatHPRegenModPerLevel(self, champion, para, stat):
        champion.hpregenperlevel += para

    def _FlatHPRegenMod(self, champion, para, stat):
        champion.hpregen += para

    def _rFlatArmorPenetrationModPerLevel(self, champion, para, stat):
        raise(Exception(self._rFlatArmorPenetrationModPerLevel.__name__ + ' not impleted'))

    def _rFlatMPRegenModPerLevel(self, champion, para, stat):
        champion.mpregenperlevel += para

    def _FlatCritDamageMod(self, champion, para, stat):
        champion.critdamage += para

    def _PercentCritDamageMod(self, champion, para, stat):
        raise(Exception(self._PercentCritDamageMod.__name__ + ' not impleted'))

    def _rPercentCooldownModPerLevel(self, champion, para, stat):
        champion.cooldownperlevel += para

    def _rPercentCooldownMod(self, champion, para, stat):
        champion.cooldown += para


class Item(AbstractItem):

    def __init__(self, name, item_shelve=item_at_map11):
        self.name = name
        self._item_shelve = item_shelve
        self.stats = self._item_shelve.get_attr_from_item(name, 'stats')


class Rune(AbstractItem):

    def __init__(self, name, rune_shelve=rune_full):
        self.name = name
        self._rune_shelve = rune_full
        self.stats = self._rune_shelve.get_attr_from_item(name, 'stats')
