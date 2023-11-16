# CH03 初识Python语法
# Task03 函数
# 题目01：点外卖
"""
编写一个函数 order_food()，该函数接受两个参数：food_name（食物名称）和 location（送餐地址）。
函数应根据食物名称和送餐地址返回一个消息，告诉用户预计多少时间能送达。
如果是快餐，如“汉堡”等，返回"30分钟内送达您的地址：[location]"。
如果是火锅、烧烤等需要时间准备的食物，返回"1小时内送达您的地址：[location]"。
其他食物返回"45分钟内送达您的地址：[location]"。
示例:
order_food("汉堡", "北京市朝阳区")  # 返回 "30分钟内送达您的地址：北京市朝阳区"
"""

def order(food_name, location):
    if food_name in ["汉堡", "披萨", "炸鸡"]:
        return f"30分钟内送达您的地址：{location}。"
    elif food_name in ["火锅", "烧烤", "烤肉", "烤鱼"]:
        return f"1小时内送达您的地址：{location}。"
    else:
        return f"45分钟内送达您的地址：{location}。"

your_order_food = input("Please order your food: ")
your_location = input("Please enter your location: ")
print(order(your_order_food, your_location))