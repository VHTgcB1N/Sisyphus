import sys
sys.path.append(r'.\src')
sys.path.append('.')

import unittest
import config
# from util.champion import champion_full.get_items,i
# get_champion_with_name, get_attr_from_champion
from util.shelve_tool import item_full, champion_full, item_at_map11, _Marksman
from model.champion_model import Champion, compute


from model.item_model import Item


class TestShelveTool(unittest.TestCase):

    def test_get_item_with_tag(self):
        names = champion_full.get_item_with_tag('Marksman')
        self.assertEqual(len(names), len(_Marksman))
        items = item_full.get_item_with_tag('Armor')
        self.assertEqual(len(items), 26)

    def test_get_item_with_name(self):
        champion = champion_full.get_item_with_key('Vayne')
        self.assertIsInstance(champion, dict)
        item = item_full.get_item_with_key('3031')
        self.assertIsInstance(item, dict)

    def test_item_attr(self):
        attr = champion_full.get_attr_from_item('Vayne', 'stats', 'hp')
        self.assertEqual(attr, 498.44)
        attr = item_full.get_attr_from_item(
            '3031', 'stats', 'FlatCritChanceMod')
        self.assertEqual(0.2, attr)
        attr = item_full.get_attr_from_item('3031', 'stats', 'FlatCritDamage')
        self.assertEqual(0.5, attr)


class TestChampionClass(unittest.TestCase):

    def test_champion(self):
        stats = champion_full.get_attr_from_item('Vayne', 'stats')
        c = Champion('Vayne', **stats)
        d = Champion('Vayne', **stats)
        d.update_lv(3)
        d.update_lv(5)
        dhp5 = d.hp
        das = d.attackspeed
        c.update_lv(5)
        hp5 = c.hp
        cas = c.attackspeed
        self.assertEqual(dhp5, hp5)
        self.assertEqual(das, cas)

    def test_value_dps(self):
        stats = champion_full.get_attr_from_item('Vayne', 'stats')
        c = Champion('Vayne', **stats)
        c.value_dps()
        print('dps:', c.phiscal_dps)

    def test_item_at_map11(self):
        wujin = item_at_map11.get_item_with_key('3031')
        print(wujin['description'])
        print(wujin.keys())


class TestItemClass(unittest.TestCase):

    def test_item_init(self):
        champion = Champion('Vayne')
        wujin = Item('3031')
        wujin.update_champion(champion)

    def test_item_update(self):
        champion = Champion('Vayne')
        self.assertEqual(champion.crit, 0)
        self.assertEqual(champion.critdamage, 1)
        self.assertEqual(champion.attackdamage, 55.88)
        wj = Item('3031')
        wj.update_champion(champion)
        self.assertEqual(champion.crit, 0.2)
        self.assertEqual(champion.critdamage, 1.5)
        self.assertEqual(champion.attackdamage, 125.88)

    def test_build(self):
        champion = Champion('Vayne')
        champion.update_lv(12)
        wj = Item('3031')
        wj.update_champion(champion)
        bf = Item('1038')
        bf.update_champion(champion)
        kr = Item('3086')
        kr.update_champion(champion)
        print(champion.hp, champion.attackdamage, champion.attackspeed)
        print(champion.crit, champion.critdamage)
        print(champion.raw_physical_dps)
        print(champion.effective_physical_dps)


def suit():
    suit = unittest.TestLoader().loadTestsFromTestCase(TestItemClass)
    suit = unittest.TestSuite(suit)
    return suit


def main():
    s = suit()
    unittest.TextTestRunner().run(s)


if __name__ == '__main__':
    main()
