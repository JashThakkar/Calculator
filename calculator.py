from tkinter import *

app = Tk()
app.title('Calculator')
app.geometry('325x442')

buttons_pressed = []


def press_0():
    txt.insert(END, '0')
    buttons_pressed.append('0')


def press_1():
    txt.insert(END, '1')
    buttons_pressed.append('1')


def press_2():
    txt.insert(END, '2')
    buttons_pressed.append('2')


def press_3():
    txt.insert(END, '3')
    buttons_pressed.append('3')


def press_4():
    txt.insert(END, '4')
    buttons_pressed.append('4')


def press_5():
    txt.insert(END, '5')
    buttons_pressed.append('5')


def press_6():
    txt.insert(END, '6')
    buttons_pressed.append('6')


def press_7():
    txt.insert(END, '7')
    buttons_pressed.append('7')


def press_8():
    txt.insert(END, '8')
    buttons_pressed.append('8')


def press_9():
    txt.insert(END, '9')
    buttons_pressed.append('9')


def press_plus():
    txt.insert(END, '+')
    buttons_pressed.append('+')


def press_min():
    txt.insert(END, '-')
    buttons_pressed.append('-')


def press_mult():
    txt.insert(END, '*')
    buttons_pressed.append('*')


def press_div():
    txt.insert(END, '/')
    buttons_pressed.append('/')


def press_clear():
    txt.delete(0.0, END)
    buttons_pressed.clear()


def press_eq():
    x = 0
    part_two = part_one = ''

    while buttons_pressed[x].isnumeric() or buttons_pressed[x] == '.':
        part_one = part_one + buttons_pressed[x]
        x = x + 1

    computation = buttons_pressed[x]

    while x < len(buttons_pressed):

        if buttons_pressed[x].isnumeric():
            part_two = part_two + buttons_pressed[x]
            x = x + 1

        else:
            x = x + 1

    part_one = float(part_one)
    part_two = float(part_two)

    if computation == '+':
        answer = part_one + part_two
        txt.delete(0.0, END)
        txt.insert(END, str(answer))
        buttons_pressed.clear()

        for dig in str(answer):
            buttons_pressed.append(dig)

    elif computation == '-':
        answer = part_one - part_two
        txt.delete(0.0, END)
        txt.insert(END, str(answer))
        buttons_pressed.clear()

        for dig in str(answer):
            buttons_pressed.append(dig)

    elif computation == '*':
        answer = part_one * part_two
        txt.delete(0.0, END)
        txt.insert(END, str(answer))
        buttons_pressed.clear()

        for dig in str(answer):
            buttons_pressed.append(dig)

    elif computation == '/':
        answer = part_one / part_two
        txt.delete(0.0, END)
        txt.insert(END, str(answer))
        buttons_pressed.clear()

        for dig in str(answer):
            buttons_pressed.append(dig)


txt = Text(master=app, height=5, width=45)
txt.grid(row=0, column=0, columnspan=4)

button_0 = Button(master=app, text='0', height=5, width=5, command=press_0)
button_0.grid(row=4, column=0)

button_clear = Button(master=app, text='CLEAR', height=5, width=5, command=press_clear)
button_clear.grid(row=4, column=1)

button_eq = Button(master=app, text='=', height=5, width=5, command=press_eq)
button_eq.grid(row=4, column=2)

button_div = Button(master=app, text='/', height=5, width=5, command=press_div)
button_div.grid(row=4, column=3)

button_1 = Button(master=app, text='1', height=5, width=5, command=press_1)
button_1.grid(row=3, column=0)

button_2 = Button(master=app, text='2', height=5, width=5, command=press_2)
button_2.grid(row=3, column=1)

button_3 = Button(master=app, text='3', height=5, width=5, command=press_3)
button_3.grid(row=3, column=2)

button_mult = Button(master=app, text='*', height=5, width=5, command=press_mult)
button_mult.grid(row=3, column=3)

button_4 = Button(master=app, text='4', height=5, width=5, command=press_4)
button_4.grid(row=2, column=0)

button_5 = Button(master=app, text='5', height=5, width=5, command=press_5)
button_5.grid(row=2, column=1)

button_6 = Button(master=app, text='6', height=5, width=5, command=press_6)
button_6.grid(row=2, column=2)

button_min = Button(master=app, text='-', height=5, width=5, command=press_min)
button_min.grid(row=2, column=3)

button_7 = Button(master=app, text='7', height=5, width=5, command=press_7)
button_7.grid(row=1, column=0)

button_8 = Button(master=app, text='8', height=5, width=5, command=press_8)
button_8.grid(row=1, column=1)

button_9 = Button(master=app, text='9', height=5, width=5, command=press_9)
button_9.grid(row=1, column=2)

button_plus = Button(master=app, text='+', height=5, width=5, command=press_plus)
button_plus.grid(row=1, column=3)

app.mainloop()
