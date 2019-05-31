import random

menu = '''(0)石头
(1)剪刀
(2)布
(q)退出
请出拳(0/1/2/q)：'''
# 存放所有出拳
all_list = ['石头','剪刀','布']
# 定义变量存放所有胜利的可能
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
i = 1
# 定义比分变量
cwin = 0
ywin = 0

while i <= 3:
    c = random.choice(all_list)
    # 获取你的出拳
    y = input(menu)
    if y.strip().lower() in ['0','1','2','q']:
        if y.strip().lower() == 'q':
            print('\033[31m游戏退出\033[0m')
            break
        elif [all_list[int(y)],c] in win_list:
            print('\033[31m你赢了\033[0m')
            ywin += 1
        elif all_list[int(y)] == c:
            print('\033[31m平局\033[0m')
        else:
            print('\033[31m你输了\033[0m')
            cwin += 1
    else:
        print('\033[31m选择无效\033[0m')

    i += 1

if ywin > cwin:
    print('\033[31m你赢了,比分: %d:%d\033[0m' % (ywin,cwin))
elif ywin == cwin:
    print('\033[31m平局\033[0m')
else:
    print('\033[31m电脑赢,比分: %d:%d\033[0m' % (cwin,ywin))





