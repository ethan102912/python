# for i in range(2, 10):
#     print(i)
# else:
#     print("迴圈正常結束")

# i = 2
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("迴圈正常結束")

# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)
# else:

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
#     i += 1

# i = 1
# while i < 6:
#     if i == 3:
#         continue
#     print(i)
#     i += 1

# while True:
#     print('  1. 蘋果汁2. 柳橙汁3. 葡萄汁4. 系統關閉')
#     ans = int(input("請輸入編號:"))
#     if ans == "1":
#         print("蘋果汁")
#     elif ans == "2":
#         print("柳橙汁")
#     if ans == "3":
#         print("葡萄汁")
#     elif ans == "4":
#         print("系統關閉")
#         break
#     else:
#         print('重新輸入')

# import random as r

# print(r.randrange(5))
# print(r.randrange(3))
# print(r.randrange(0, 10, 2))

# print(r.randint(1, 3))
# print(r.randint(1, 10))
import random as r

x = r.randint(1, 100)
while True:
    i = int(input("輸入0~100之間的數字:"))
    if i > x:
        print("再小一點")
    elif i < x:
        print("再大一點")
    elif i == x:
        print("答對了")
        break
