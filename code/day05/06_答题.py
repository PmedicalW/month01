import random

print('儿子,欢迎使用老爸的答题系统,开始吧!!!')
correct = 0
wrong = 0

for i in range(5):
    # 随机生成2个数字
    n1 = random.randint(1,20)
    n2 = random.randint(1,20)
    # 随机生成操作符
    s = ['+','-']
    option = random.choice(s)
    # 完成出题,并判断正确与否
    if n1 < n2 and option == '-':
        result = input('%d %s %d = ' % (n2,option,n1))
        result = int(result)
        if result == n2-n1:
            print('你真棒,继续...')
            correct += 1
        else:
            print('回答错误,正确答案:%d' % (n2-n1))
            wrong += 1
    elif n1 >= n2 and option == '-':
        result = input('%d %s %d = ' % (n1,option,n2))
        result = int(result)
        if result == n1-n2:
            print('正确,请继续...')
            correct += 1
        else:
            print('错误,正确答案为: %d' % (n1-n2))
            wrong += 1
    else:
        result = input('%d %s %d = ' % (n1,option,n2))
        result = int(result)
        if result == n1+n2:
            print('正确,请继续...')
            correct += 1
        else:
            print('错误,正确答案为: %d' % (n1+n2))
            wrong += 1

print('共5道题,正确:%d道 错误:%d道' % (correct,wrong))









