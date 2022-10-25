import turtle as t
# for i in range(100):
#     t.forward(100)
#     t.right(90)
# t.done()
#  import turtle
# turtle.color('blue') # 設定小烏龜顏色
# turtle.shape('turtle') # 設定小烏龜形'arrow', 'turtle',
# #'circle', 'square','triangle', 'classic'.
# turtle.stamp() # 蓋章
# turtle.penup() # 提筆
t.penup()
t.shape('turtle')
for i in range(0, 100):
    t.forward(i)
    t.right(25)
    t.stamp()

t.done()