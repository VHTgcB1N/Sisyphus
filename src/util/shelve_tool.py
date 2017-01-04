import shelve
# import sys
# sys.path.append(r'd:\workspace\analol\Sisyphus\src')
# print(sys.path[-1])
import config
from functools import reduce
from util.con_dict import work_dict, discard, discard_paths

champion_shelve_path = config.get("champion_shelve_path")
item_shelve_path = config.get("item_shelve_path")
item_shelve_path_at_map11 = config.get("item_shelve_at_map11")
_Marksman = ['Jayce', 'Varus', 'Caitlyn', 'Quinn', 'KogMaw', 'Ashe',
             'Tristana', 'Ezreal', 'Kalista', 'Jhin', 'MissFortune',
             'Azir', 'Teemo', 'Twitch', 'Graves', 'Jinx', 'Lucian',
             'Vayne', 'Urgot', 'Corki', 'Kindred', 'Draven', 'Kennen', 'Sivir']


class Shelve(object):

    def __init__(self, path):
        self._f = shelve.open(path)

    def get_items(self):
        return self._f.items()

    def item_keys(self):
        return list(self._f.keys())

    def get_item_with_key(self, key):
        return self._f[key]

    def get_attr_from_item(self, _id, *keys):
        obj = self.get_item_with_key(_id)
        return work_dict(obj, *keys)

    def get_item_with_tag(self, *tags):
        '''返回属于某一类的item的key，打开shelve为item类型的时候，tags应该属于[]，
        当打开的shelve为champion类型时,tags应属于Marksman, Mage, Assassin,
        Fighter, Tank, Support, Fighter。

        >> self.get_item_with_tag(*['Marksman', 'Mage'])

        '''
        def is_tags_in(d, *tags):
            l = [tag in d for tag in tags]
            return reduce(lambda x, y: x and y, l)

        result = []
        for k, v in self._f.items():
            if ('tags' in v) and is_tags_in(v['tags'], *tags):
                result.append(k)
        return result


item_full = Shelve(item_shelve_path)
champion_full = Shelve(champion_shelve_path)
item_at_map11 = Shelve(item_shelve_path_at_map11)
