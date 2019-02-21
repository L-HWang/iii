# print(print(print(3)))

import random
c = int(input("請出拳 [0]剪刀 [1]石頭 [2]布"))
trans = ["剪刀", "石頭", "布"]
print("我出的拳:", trans[c])
com = random.randint(0, 2)
print("電腦出拳:", trans[com])
if c == com:
    print("平手")
elif c == (com + 1) % 3:
    print("我贏了")
else:
    print("我輸了")


import random
c = int(input("請出拳 [0]棒 [1]老虎 [2]雞 [3]蟲: "))
trans = ["棒", "老虎", "雞", "蟲"]
print("我出的拳:", trans[c])
com = random.randint(0, 3)
print("電腦出拳:", trans[com])
if c == (com - 1) % 4:
    print("我贏了")

elif c == (com + 1) % 4:
    print("我輸了")
else:
    print("平手")

print(123456789)