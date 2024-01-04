
from tkinter import *
from tkinter.ttk import Combobox

class CalcWinFrm:
    def __init__(self, win):

        self.entry_focused = 1
        
        # Create 4 Label
        self.lbl_calc = Label(win, text='Calculator Application - Tkinter UI',
                              font=('Arial', 16, 'bold'),
                              foreground='navy',
                              background='lightgray',
                              width=50, height=2,
                              justify='center'
                              )

        self.lbl_1st_op = Label(win, text="First Number",
                                font=('Arial', 10, 'bold'),
                                background='grey',
                                width=19
                                )
        self.lbl_2nd_op = Label(win, text="Second Number",
                                font=('Arial', 10, 'bold'),
                                background='grey',
                                width=19
                                )
        self.lbl_Results = Label(win, text="Results",
                                 font=('Arial', 15, 'bold'),
                                 background='green',
                                 width=30, height=1
                                 )

        entry_text_1 = StringVar()
        entry_text_2 = StringVar()

        # Create 3 Entry
        self.entry_1st_num = Entry(width=15,
                                   font=('Arial', 14, 'normal'),
                                   background="white",
                                   foreground='red',
                                   justify='right',
                                   textvariable=entry_text_1,
                                   name='entry1'
                                   )

        self.entry_2nd_num = Entry(width=15, font=('Arial', 14, 'normal'),
                                   background='white',
                                   foreground='red',
                                   justify='right',
                                   textvariable=entry_text_2,
                                   )
        self.entry_result_num = Entry(
            width=33,
            font=('Arial', 14, 'bold'),
            background='yellow',
            justify='center',
        )

        # Create Function for focus on entry 1 and 2
        # We create in for call numbers from button into entry 1 & 2

        def set_entry_focus(value):
            self.entry_focused = value

        self.entry_1st_num.bind('<1>', lambda event: set_entry_focus(1))
        self.entry_2nd_num.bind('<1>', lambda event: set_entry_focus(2))

        def set_entry_value(value):
            if self.entry_focused == 2:
                val = entry_text_2.get()
                entry_text_2.set(val + str(value))
            else:
                val = entry_text_1.get()
                entry_text_1.set(val + str(value))
                pass

        # Create 4 Buttons
        self.btn_add = Button(win,
                              text='+',
                              width=3, height=2,
                              font=('Arial', 14, 'bold'), fg='red',
                              command=self.add)
        self.btn_sub = Button(win,
                              text='-',
                              width=3, height=2,
                              font=('Arial', 14, 'bold'), fg='red',
                              command=self.sub)
        self.btn_mul = Button(win,
                              text='x',
                              width=3, height=2,
                              font=('Arial', 14, 'bold'), fg='red',
                              command=self.multi)
        self.btn_dev = Button(win,
                              text='/',
                              width=3, height=2,
                              font=('Arial', 14, 'bold'), fg='red',
                              command=self.devi)

        # Set Title Label
        # side = TOP it's mean TOP of the window form
        self.lbl_calc.pack(side=TOP)

        # Set 3 Labels
        # .plae is the way for set label using x and y
        self.lbl_1st_op.place(x=13, y=120)
        self.lbl_2nd_op.place(x=200-45, y=120)
        self.lbl_Results.place(x=5, y=53)

        # Set 3 Entry box
        self.entry_1st_num.place(x=5, y=140)
        self.entry_2nd_num.place(x=180-30, y=140)
        self.entry_result_num.place(x=5, y=80)

        # Set 4 Buttons
        self.btn_add.place(x=55-45, y=190)
        self.btn_sub.place(x=125-45, y=190)
        self.btn_mul.place(x=195-45, y=190)
        self.btn_dev.place(x=267-45, y=190)

    # Create Button Clear and Delete
        button_clear = Button(win, text='Clear All',
                                width=6, height=2, 
                                foreground='green',
                                command=self.clear_all)
        button_clear.place(x=55-45, y=400)

        button_delete = Button(win, text='Delete', 
                                width=6,
                                height=2, 
                                foreground='red',
                                command=self.delete_last_digit)  # Assign the function here
        button_delete.place(x=238-45, y=400)

    # Create function of Button number 0-9

    # Create Button 0-9
        button1 = Button(win,
                         text='1',
                         width=4, height=2,
                         command=lambda value=1: set_entry_value(value))
        button1.place(x=55-45, y=250)

        button2 = Button(win,
                         text='2',
                         width=4, height=2,
                         command=lambda value=2: set_entry_value(value))
        button2.place(x=155-45, y=250)

        button3 = Button(win,
                         text='3',
                         width=4, height=2,
                         command=lambda value=3: set_entry_value(value))
        button3.place(x=255-45, y=250)

        button4 = Button(win,
                         text='4',
                         width=4, height=2,
                         command=lambda value=4: set_entry_value(value))
        button4.place(x=55-45, y=300)

        button5 = Button(win,
                         text='5',
                         width=4, height=2,
                         command=lambda value=4: set_entry_value(value))
        button5.place(x=155-45, y=300)

        button6 = Button(win,
                         text='6',
                         width=4, height=2,
                         command=lambda value=6: set_entry_value(value))
        button6.place(x=255-45, y=300)

        button7 = Button(win,
                         text='7',
                         width=4, height=2,
                         command=lambda value=7: set_entry_value(value))
        button7.place(x=55-45, y=350)

        button8 = Button(win,
                         text='8',
                         width=4, height=2,
                         command=lambda value=8: set_entry_value(value))
        button8.place(x=155-45, y=350)

        button9 = Button(win,
                         text='9',
                         width=4, height=2,
                         command=lambda value=9: set_entry_value(value))
        button9.place(x=255-45, y=350)

        button0 = Button(win,
                         text='0',
                         width=4, height=2,
                         command=lambda value=0: set_entry_value(value))
        button0.place(x=155-45, y=400)

    # Create add() function

    def add(self):
        self.entry_result_num.configure(state='normal')
        self.entry_result_num.delete(0, 'end')

        num1 = float(self.entry_1st_num.get())
        num2 = float(self.entry_2nd_num.get())
        result = num1 + num2

        self.entry_result_num.insert(END, str(float(result)))
        self.entry_result_num.configure(state='disabled')
        print('Successful with Addition')

    # Create sub() Function
    def sub(self):
        self.entry_result_num.configure(state='normal')
        self.entry_result_num.delete(0, 'end')

        num1 = float(self.entry_1st_num.get())
        num2 = float(self.entry_2nd_num.get())
        result = num1 - num2

        self.entry_result_num.insert(END, str(float(result)))
        self.entry_result_num.configure(state='disabled')
        print('Successful with Subbtract')

    # Create multi() function
    def multi(self):
        self.entry_result_num.configure(state='normal')
        self.entry_result_num.delete(0, 'end')

        num1 = float(self.entry_1st_num.get())
        num2 = float(self.entry_2nd_num.get())
        result = num1 * num2

        self.entry_result_num.insert(END, str(float(result)))
        self.entry_result_num.configure(state='disabled')
        print('Successful with Multication')

    # Create devi() function
    def devi(self):
        self.entry_result_num.configure(state='normal')
        self.entry_result_num.delete(0, 'end')

        num1 = float(self.entry_1st_num.get())
        num2 = float(self.entry_2nd_num.get())
        if (num1 != 0):
            result = num1 / num2
            self.entry_result_num.insert(END, str(float(result)))
            print('Successful with Divide')
        elif (num2 != 0):
            result = num1 / num2
            self.entry_result_num.insert(END, str(float(result)))
            print('Successful with Divide')
        elif (num1 == 0):
            self.entry_result_num.insert(END, str(float(result)))
            print('Successful with Divide ,THE ANSWER IS 0')
        elif (num2 == 0):
            self.entry_result_num.insert(END, str(float(result)))
            print('The Answer is 0, Because 0 is cannot Divide with others numbers')
            self.entry_result_num.configure(state='disabled')
        else:
            self.entry_result_num.insert(END, str())
        self.entry_result_num.configure(state='disabled')
        
    # Create the delete function
    def delete_last_digit(self):
        focused_entry = self.entry_1st_num if self.entry_focused == 1 else self.entry_2nd_num
        current_text = focused_entry.get()
        if current_text:
            focused_entry.delete(len(current_text)-1, END)
    
    # Create the clear_all function
    def clear_all(self):
        # Clear all entries
        self.entry_1st_num.delete(0, END)
        self.entry_2nd_num.delete(0, END)
        self.entry_result_num.delete(0, END)

# Create Window form
WinFrm = Tk()
WinFrm.configure(background='gray')
# WinFrm.geometry("555x200")
width = 292
height = 500
# WinFrm.configure(background="blue")
# Call class
mywin = CalcWinFrm(WinFrm)
# Set New title
WinFrm.title('Python Calculator Application')
# Display
screen_width = WinFrm.winfo_screenwidth()
screen_height = WinFrm.winfo_screenheight()

# Calculate Starting x and y
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
WinFrm.geometry('%dx%d+%d+%d' % (width, height, x, y))

lbl_create_by = Label(WinFrm, text="Github: @Smey09",
                                font=('Arial', 10, 'bold'),
                                background='red',
                                foreground='white',
                                width=15
                                )
lbl_create_by.place(x=95, y=470)
WinFrm.resizable(False, False)

WinFrm.mainloop()
