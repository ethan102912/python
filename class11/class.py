from stringprep import c22_specials

bag = []
s = int(input("請輸入背包的大小:"))
for i in range(s):
    t = input('輸入想要的東西')
    bag.append(t)
    print(bag)

r = input("請輸入想拿出來的東西:")
while r in bag:
    bag.remove(r)

print(bag)

# c = input("請輸入想計算數量的東西:")
# print(bag.count(c))

bag2 = []
for i in bag:
    if i in bag:
        if not (i in bag2):
            bag2.append(i)
            print(f"{i}={bag.count(i)}")

# o=0
# for i in range(len(bag)):
#     bag2=[]
#     e=bag[]
