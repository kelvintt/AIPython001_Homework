# CH03 初识Python语法
# Task02 程序结构
# 题目02：输出斐波那契数列前20个数
"""
斐波那契数列（Fibonacci sequence），通常也被称作黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）
在《计算之书》中研究在理想假设条件下兔子成长率问题而引入的数列，因此这个数列也常被戏称为“兔子数列”。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，按照这个规律，
斐波那契数列的前10个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
"""

# 建立一个函数，用来输出指定的前 n 个斐波那契数列的值。
def generate_fibonacci(n):
    # 数列的列表初始化
    fibonacci_seq = []
    a, b = 1, 1
    for i in range(int(n)):
        fibonacci_seq.append(a)
        a, b = b, a + b
    return fibonacci_seq

n = input("Please enter the number of the sequence that you want to print: ")
print(f"The first {n} numbers of the fibonacci sequence are: {generate_fibonacci(n)}.")

print(f"The sequence contains {len(generate_fibonacci(n))} numbers.")