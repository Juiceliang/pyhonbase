#coding:utf-8
import random
str = input('是否开始游戏？（是/否) ：')
while str == "是" :
    data = input('请输入一个数：剪子（0）、包袱（1）、锤（2）：')
    data = int(data)
    player = random.randint(0, 2)
    if  data == player :
        print('平手')
        str = input('是否继续游戏（是/否）')
    elif (( data == 0) and (player == 2)) or ((data == 1) and (player == 0)) or ((data == 2) and (player == 1)):
        print('输了')
        str = input('是否继续游戏（是/否）')
    else:
        print('赢了')
        str = input('是否继续游戏（是/否）')
print('游戏结束')