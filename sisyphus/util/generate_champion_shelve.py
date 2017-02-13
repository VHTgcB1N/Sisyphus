# -*- coding: utf-8 -*-
import json
import shelve

from .. import config
from ..util.con_dict import discard_paths, work_dict

champion_shelve_path = config.get('champion_shelve_path')
champion_json_path = config.get('champion_json_path')

item_shelve_path = config.get('item_shelve_path')
item_json_path = config.get('item_json_path')

rune_json_path = config.get('rune_json_path')
rune_shelve_path = config.get('rune_shelve_path')

item_shelve_at_map11 = config.get('item_shelve_at_map11')

champion_path = "data/"
needless_path_champion = [
    "image", "skins", "lore",
    "blurb", "allytips", "enemytips",
    "info", "recommended"]

needless_path_item = ['image', 'plaintext']


def generate_shelve(json_path, shelve_path, data_path, discard_path):
    """从json_path中读取json文件，将data_path路径的值
    转换成python对象，并丢弃掉discard_path中说明的部分

    若从json中获得的python对象为dict

    data_path = ”data/"
    discard_path = ['image', 'plaintext']

    则最后将dict['data']中key为'image','plaintext'的部分丢弃，
    然后储存到shelve_path中
    """
    def _discard_paths(d, *paths):
        return [_discard(d, path) for path in paths]

    def _discard(d, key):
        tk = key.split('/', 1)
        if len(tk) == 1:
            return d.pop(tk[0], None)
        else:
            return _discard(d[tk[0]], tk[1])

    with open(json_path, 'r', encoding='utf8') as f:
        data = json.load(f)
    with shelve.open(shelve_path) as f:
        target_data = data[data_path.split('/')[0]]
        [_discard_paths(target_data[k], *discard_path)
         for k in target_data.keys()]
        for key in target_data.keys():
            f[key] = target_data[key]


def generate_item_at_map(item_shelve_path):
    with open(item_json_path, 'r', encoding='utf8') as f:
        data = json.load(f)

    with shelve.open(item_shelve_at_map11) as f:
        target_data = data[champion_path.split('/')[0]]
        discard_paths(target_data, *needless_path_item)
        result_keys = []
        for item_key, value in target_data.items():
            is_at_map_11 = work_dict(value, 'maps', '11')
            if is_at_map_11 is None:
                print(item_key)
                continue
            if is_at_map_11:
                result_keys.append(item_key)
        [discard_paths(target_data[k], 'maps') for k in result_keys]
        for k in result_keys:
            f[k] = target_data[k]


def generate_rune_shelve():
    generate_shelve(rune_json_path, rune_shelve_path, "data/", ['image', 'description'])

if __name__ == '__main__':
    main()
