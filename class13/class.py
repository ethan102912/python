num = int(input('請輸入想要存幾筆資料'))
b = {}
for i in range(num):
    key = input('請輸入標籤名稱')
    value = input('請輸入資料')
    b[key] = value
    print(b)
r = input("請輸入想珊除的key:")
b.pop(r, "")
print(b)

for key, value in b.items():
    print(key + ":" + value)
