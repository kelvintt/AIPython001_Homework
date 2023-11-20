# Ch03 初识Python语法
# Task02 程序结构
# 题目02 猜数字游戏
# 说明：游戏的规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，
# 计算机给出对应的提示信息（大一点、小一点或猜对了），
# 如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
# 在此题中，你需要使用到Python的random模块来随机选择列表中的元素。
# 因此，请首先导入random模块。导入的方式是：import random。random模块可以帮助你从一个序列中随机选择一个元素。



def guess_number():
    import random
    random_number = random.randint(1, 100)
    number = 0
    n = 0
    while number != random_number:
        number = int(input("Please enter the number you guess: "))
        n += 1
        if number > random_number:
            print("大一点")
        elif number < random_number:
            print("小一点")
    print(f"你一共猜了{n}次。")

guess_number()

        

