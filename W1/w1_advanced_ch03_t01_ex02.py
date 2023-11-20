# Ch03 初识Python语法
# Task01 数据类型
# 题目02 早餐选择
# 说明：请创建一个列表breakfast，其中包含你今天早上吃的食物（至少3样）。例如：['牛奶', '包子', '鸡蛋']。
# 然后使用print()函数随机打印其中一样食物，表示那是你最喜欢的早餐食品。
# 在此题中，你需要使用到Python的random模块来随机选择列表中的元素。因此，请首先导入random模块。
# 导入的方式是：import random。random模块可以帮助你从一个序列中随机选择一个元素。

import random
breakfast_list = ["汉堡", "牛奶", "沙拉"]

my_favorite_food = random.choice(breakfast_list)
print(f"我最喜欢的早餐食品是{my_favorite_food}。")