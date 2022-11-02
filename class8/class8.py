# password = ''
# while password != "12947":
#     password = input("請輸入密碼")
#     if password == '12947':
#         print("hi")
#     else:
#         print('nope')
x = int(input("請輸入正整數"))

i = 2
while x % i != 0 and i != x:
    i += 1

if i == x:
    print("yes")
else:
    print('no')
