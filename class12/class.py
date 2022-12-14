bag = []
end = None
while end == True:
    print(f'目前以點的餐點[]')
    print('1 新增餐點')
    print('2 移除餐點')
    print('3 提交餐點')
    aa = int(input('請輸入功能選項'))
    if aa == 1:
        print('1. 蘋果汁')
        print('2. 柳橙汁')
        print('3. 葡萄汁')

        bag.append('蘋果汁')
        print(bag)

# bag = []
# s = int(input("請輸入背包的大小:"))
# for i in range(s):
#     t = input('輸入想要的東西')
#     bag.append(t)
#     print(bag)

# r = input("請輸入想拿出來的東西:")
# while r in bag:
#     bag.remove(r)

# print(bag)

# # 不要改
# bag2 = []
# for i in bag:
#     if i in bag:
#         if not (i in bag2):
#             bag2.append(i)
#             print(f"{i}={bag.count(i)}")