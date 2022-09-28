try:
    f = float(input("請輸入華氏溫度"))
except:
    print('發生錯誤')
else:
    c = 5 / 9 * (f - 32)
    print("華氏溫度" + str(f) + "f等於華氏溫度" + str(c) + "c")

# git add .
# git commit -m "class4"
# git push