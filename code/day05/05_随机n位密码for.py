'''随机生成n位密码'''
import random
import string

# 存放所有数字字母下划线的变量all_chars
all_chars = string.ascii_letters + \
                           string.digits + '_'
# 接收用户从终端输入密码位数
n = int(input('请输入密码位数:'))
# 定义一个空字符串变量
pwd = ''
# 用for循环控制循环次数,遍历出来的i的值不使用
for i in range(n):
    # 随机选择1个字符,赋值给一个变量char
    char = random.choice(all_chars)
    # 把选择出来的字符　利用　字符串相加
    pwd = pwd + char


print(pwd)








