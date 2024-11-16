from tkinter import *
print('Hãy bấm và giữ chuột trái, di chuyển chuột quanh màn hình để vẽ')
print('Bấm chọn màu để chọn màu cho cọ vẽ của bạn')
def xoacu():
    canvas.delete('line')
window = Tk()
Button(window,text='Delete',command=xoacu).pack()
canvas = Canvas(window, height=500, width=750, bg='white')
canvas.pack()
lastX, lastY = 0, 0
colour = 'black'
def store(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y
def onclick(event):
    store(event)
def ondrag(event):
    global lastX, lastY
    canvas.create_line(lastX, lastY, event.x, event.y, fill=colour, width=3,tags='line')
    store(event)
canvas.bind('<Button-1>', onclick)
canvas.bind('<B1-Motion>', ondrag)
red_id = canvas.create_rectangle(10, 10, 30, 30, fill='red')
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill='blue')
black_id = canvas.create_rectangle(10, 60, 30, 80, fill='black')
white_id = canvas.create_rectangle(10, 85, 30, 105, fill='white')
def setred(event):
    global colour
    colour = 'red'
def setblue(event):
    global colour
    colour = 'blue'
def setblack(event):
    global colour
    colour = 'black'
def setwhite(event):
    global colour
    colour = 'white'
canvas.tag_bind(red_id, '<Button-1>', setred)
canvas.tag_bind(blue_id, '<Button-1>', setblue)
canvas.tag_bind(black_id, '<Button-1>', setblack)
canvas.tag_bind(white_id, '<Button-1>', setwhite)
window.mainloop()
