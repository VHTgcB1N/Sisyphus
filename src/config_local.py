import os
from config import Config


class ConfigLocal(Config):

    static_path = r'D:\workspace\analol\Sisyphus\static'

    champion_shelve_path = os.path.join(
        static_path, 'champion', 'champion_full')
    champion_json_path = os.path.join(
        static_path, 'raw_data', 'champion_full.json')

    item_shelve_path = os.path.join(static_path, 'item', 'item_full')
    item_json_path = os.path.join(static_path, 'raw_data', 'item.json')

    item_shelve_at_map11 = os.path.join(static_path, 'item', 'item_at_map11')
