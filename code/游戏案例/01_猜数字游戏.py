# 猜数字,计算机1-100,你来猜,一直到猜对为止
import random

c = random.randint(1, 1000)

while True:
    y = int(input('请猜数字:'))
    # 猜对
    if c == y:
        print('\033[31m恭喜,猜对了\033[0m')
        break
    # 猜大
    elif y > c:
        print('\033[31m猜大了\033[0m')
    # 猜小
    else:
        print('\033[31m猜小了\033[0m')
























