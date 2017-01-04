# -*- coding: utf-8 -*-
import os


class Config(object):

    # 自己更改
    static_path = ''

    champion_shelve_path = os.path.join(
        static_path, 'champion', 'champion_full')
    champion_json_path = os.path.join(
        static_path, 'raw_data', 'champion_full.json')

    item_shelve_path = os.path.join(static_path, 'item', 'item_full')
    item_json_path = os.path.join(static_path, 'raw_data', 'item.json')

    item_shelve_at_map11 = os.path.join(static_path, 'item', 'item_at_map11')


# 配置实例
__instanse = None


def __init_instanse():
    ''' 初始化配置实例 '''
    global __instanse
    if __instanse:
        return
    try:
        from config_local import ConfigLocal
        if not issubclass(ConfigLocal, Config):
            raise TypeError('自定义配置类必须是config.Config的子类')
        __instanse = ConfigLocal()
    except ImportError:
        __instanse = Config()


def get(name, default=None):
    ''' 获取配置 '''
    __instanse or __init_instanse()
    return getattr(__instanse, name, default)


def set(name, value):
    ''' 运行时动态修改配置 '''
    __instanse or __init_instanse()
    return setattr(__instanse, name, value)


__init_instanse()
