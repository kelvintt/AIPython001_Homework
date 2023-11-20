# Ch03 初识Python语法
# Task02 程序结构
# 题目01 基于天气推荐活动的小程序
# 说明 根据天气情况来推荐用户适合的出门活动。
# 如果天气是“晴天”，推荐用户去户外散步；
# 如果天气是“阴天”，推荐用户去逛商场；
# 如果天气是“雨天”，推荐用户在家看书或看电影。

def outdoor_activity(weather):
    if weather == "晴天":
        return "户外散步"
    elif weather == "阴天":
        return "逛商场"
    elif weather == "雨天":
        return "在家看书或看电影"

today_weather = input("请输入今天的天气情况：")
print(f"今天的天气是{today_weather}，推荐的活动是{outdoor_activity(today_weather)}。")