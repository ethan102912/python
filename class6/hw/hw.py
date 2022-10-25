import turtle as t

t.shape('turtle')
t.speed(0)
t.stamp()
for i in range(1, 405, 45):
    t.penup()
    t.forward(50)
    t.stamp()
    t.home()
    t.right(i)

t.done()