a = int(input("請輸入開始整數"))
y = int(input("請輸入結束整數"))
for x in range(a, y):
    i = 2
    while x % i != 0 and i != x:
        i += 1

    if i == x:
        print(x)
