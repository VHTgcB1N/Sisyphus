import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from util.shelve_tool import champion_full, _Marksman  # item_full
from model.champion_model import Champion

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


def adc_attack_speed():
    m_data = [champion_full.get_item_with_key(n) for n in _Marksman]
    champion_objects = [Champion(c['name'], **c['stats']) for c in m_data]
    data_as = {'champion': [],
               'attack speed': [],
               'level': []}

    for c in champion_objects:
        for i in range(1, 19):
            c.update_lv(i)
            data_as['champion'].append(c.name)
            data_as['attack speed'].append(c.attackspeed)
            data_as['level'].append(i)

    dff = pd.DataFrame(data_as)
    g = sns.FacetGrid(dff, hue='champion', size=5, aspect=1.5)
    g = g.map(plt.plot, 'level', 'attack speed').add_legend()
    g.set_axis_labels('等级', '攻速')
    g.set_titles("攻速随等级变化折线图")
    g.set(xticks=np.arange(1, 20, 1))
    g.set(yticks=np.arange(0.5, 1.2, 0.05))
    sns.plt.show()


if __name__ == '__main__':
    adc_attack_speed()
