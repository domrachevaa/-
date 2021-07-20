from tkinter import *

root = Tk()
root.title("=_=")
root.geometry('255x300')

input_textEntry = StringVar()
Eq = []
input_text = Entry(root, width=40, textvariable=input_textEntry)
input_text.place(x=5, y=10)

output_textEntry = StringVar()
output_text = Entry(root, width=40, textvariable=output_textEntry)
output_text.place(x=5, y=35)

def plus():
    input_text.insert(END, '+')

def equally():
    E = input_textEntry.get()
    split_E = E.split('cos(')
    print(split_E)
    Result = eval(E)
    input_textEntry.set(Result)
    print(E)
    print(Result)
    output_textEntry.set('')

def brackets():
    E = input_text.get()
    Split1 = E.split('(')
    Split2 = E.split(')')
    print(Split2)
    if len(Split1) == 1:
        input_text.insert(END, '(')
    elif Split1[-1] == '':
        input_text.insert(END, '(')
    elif Split1[-1] != '' and len(Split1) != len(Split2):
        input_text.insert(END, ')')
    else:
        input_text.insert(END, '*(')




def minus():
    input_text.insert(END, '-')

def multiply():
    input_text.insert(END, '*')

def delete():
    input_text.delete(0, END)

def split():
    input_text.insert(END, '/')

def cos ():
    input_text.insert(END, 'cos(')

def _0():
    input_text.insert(END, '0')

def _1():
    input_text.insert(END, '1')

def _2():
    input_text.insert(END, '2')

def _3():
    input_text.insert(END, '3')

def _4():
    input_text.insert(END, '4')

def _5():
    input_text.insert(END, '5')

def _6():
    input_text.insert(END, '6')

def _7():
    input_text.insert(END, '7')

def _8():
    input_text.insert(END, '8')

def _9():
    input_text.insert(END, '9')

btn_plus = Button(root, text="+", width=5, height=2, command=plus).place(x=5, y=70)

btn_minus = Button(root, text="-", width=5, height=2, command=minus).place(x=55, y=70)

btn_multiply = Button(root, text="*", width=5, height=2, command=multiply).place(x=105, y=70)

btn_split = Button(root, text="/", width=5, height=2, command=split).place(x=155, y=70)

btn_delete = Button(root, text="Del", width=5, height=2, command=delete).place(x=205, y=70)

btn_1 = Button(root, text="1", width=5, height=2, command=_1).place(x=5, y=115)

btn_2 = Button(root, text="2", width=5, height=2, command=_2).place(x=55, y=115)

btn_3 = Button(root, text="3", width=5, height=2, command=_3).place(x=105, y=115)

btn_4 = Button(root, text="4", width=5, height=2, command=_4).place(x=5, y=160)

btn_5 = Button(root, text="5", width=5, height=2, command=_5).place(x=55, y=160)

btn_6 = Button(root, text="6", width=5, height=2, command=_6).place(x=105, y=160)

btn_7 = Button(root, text="7", width=5, height=2, command=_7).place(x=5, y=205)

btn_8 = Button(root, text="8", width=5, height=2, command=_8).place(x=55, y=205)

btn_9 = Button(root, text="9", width=5, height=2, command=_9).place(x=105, y=205)

btn_0 = Button(root, text="0", width=12, height=2, command=_0).place(x=5, y=250)

btm_equally = Button(root, text="=", width=12, height=2, command=equally).place(x=155, y=115)

btn_brackets = Button(root, text="( )", width=12, height=2, command=brackets).place(x=155, y=205)

root.mainloop()

#ZeroDivisionError: