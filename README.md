# Sisyphus
一个用来分析LOL中数据的工具
### 一个例子
下面是各个adc的及攻速成长曲线（本来应该是折线- -）
![image](https://github.com/lezhiii/Sisyphus/blob/master/adc%E5%88%9D%E5%A7%8B%E6%94%BB%E9%80%9F.png)
这是用 src 目录下 marksams.py 完成的（需要一些额外的库
### 功能
现在实现的功能有：
* 英雄数据获取
* 根据攻速、攻击、暴击计算DPS
* 物品数据获取
* 根据等级更新数据
* 英雄装备物品的更新（现在只能更新暴击、攻速和攻击力）

### 关于数据
游戏中的英雄数据，物品数据都来自[拳头的开发者网站](https://developer.riotgames.com/)。拳头提供了json格式的数据下载，有基本物品、天赋、符文这些。
程序需要的数据路径在config中配置，用python的标准库shelve来保存的。
### 其它
更多的使用例子可以看test目录下的文件
### TODO
支持更多的物品属性。还有符文、天赋这些。
