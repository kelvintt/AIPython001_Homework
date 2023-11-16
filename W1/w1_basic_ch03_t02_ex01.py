# CH03 初识Python语法
# Task02 程序结构
# 题目01：用户身份验证程序
# 说明：要求用户输入用户名和口令（密码），然后程序进行验证。
# 正确的用户名是 admin，对应的密码是42。
# 只有当用户名和密码都正确时，才提示“身份验证成功”，否则提示“身份验证失败”。

username = input("Please input your username: ")
password = input("Please input your password: ")

username_right = "admin"
password_right = "42"

if username == username_right:
    print("身份验证成功")
else:
    print("身份验证失败")