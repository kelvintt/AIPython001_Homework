# Ch03 初识Python语法
# Task03 函数
# 题目1 观看电影计划
# 说明：你和你的朋友们计划一起看电影。
# 请为此设计一个程序，输入是一个包含你的好友名字的列表和你们感兴趣的电影列表，输出需要返回一个字典，
# 字典的键是好友的名字，值是他/她希望观看的电影。
# 示例输入:
# friend_names = ['张三', '李四', '王五']
# movie_list =['流浪地球', '复仇者联盟', '哪吒之魔童降世']

def movie_plan(friends, movies):
    import random

    friend_movie_preferred = {}

    for friend in friends:
        movie_preferred =  random.choice(movies)
        friend_movie_preferred[friend] = movie_preferred
    
    return friend_movie_preferred

friend_names = ["杰克", "赛文", "爱迪", "泰罗"]
movie_list = ["重启人生", "地球脉动", "独自等待", "红猪", "太空堡垒", "蝙蝠侠"]

print(movie_plan(friend_names, movie_list))

