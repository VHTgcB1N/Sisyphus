import shelve
from functools import reduce

from .. import config

_f = shelve.open(config.get("champion_shelve_path"))
_Marksman = ['Jayce', 'Varus', 'Caitlyn', 'Quinn', 'KogMaw', 'Ashe',
             'Tristana', 'Ezreal', 'Kalista', 'Jhin', 'MissFortune',
             'Azir', 'Teemo', 'Twitch', 'Graves', 'Jinx', 'Lucian',
             'Vayne', 'Urgot', 'Corki', 'Kindred', 'Draven', 'Kennen', 'Sivir']


def champion_names():
    return list(_f.keys())


def get_champion_with_name(name):
    return _f[name]


def get_attr_from_champion(name, *keys):
    obj = get_champion_with_name(name)
    for key in keys:
        obj = obj[key]
    return obj


def get_champions_with_tag(*tags):
    '''返回某一类型的英雄，如:Marksman, Mage, Assassin,
    Fighter, Tank, Support, Fighter。可以使用多个标签'''
    def is_tags_in(tags, d):
        l = [tag in d for tag in tags]
        return reduce(lambda x, y: x and y, l)

    result = []
    for k, v in _f.items():
        if ('tags' in v) and is_tags_in(tags, v['tags']):
            result.append(k)
    return result
