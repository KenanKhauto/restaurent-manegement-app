
import tkinter as tk
import time
from Data import Data

localtime = time.asctime(time.localtime(time.time()))



class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title('Restaurant Management')
        parent.geometry('800x800')
        parent.configure(background='#0a0a0d')

        self.top_frame = TopFrame(
            master=parent,
            background='#1c1c1c',
            highlightthickness=4,
            highlightbackground='#f2a343'
            )
        self.top_frame.grid(row=1, column=2)
        
        
        for i in range(1, 4):
            self.table = Table(
                master=parent, 
                num=i,
                bg='#1c1c1c',
                highlightthickness=4,
                highlightbackground='#f2a343'
                )
            self.table.grid(row=3, column=i, pady=40)




class SecondWindow(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title('Restaurant Management')
        parent.geometry('1920x1080')
        parent.configure(background='#0a0a0d')
        self.top_frame = TopFrame(
            master=parent,
            background='#1c1c1c',
            highlightthickness=4,
            highlightbackground='#f2a343'
            )
        self.left_frame = LeftFrame(
            master=parent,
            background='#1c1c1c',
            highlightthickness=4,
            highlightbackground='#f2a343'
            )
        
        self.button = tk.Button(
            master=parent,
            font='{Segoe UI} 12 bold',
            text='Go Back',
            command=self.go_back
        )

        self.button.pack(side='right')

        self.top_frame.place(relx=0.37, rely=0.02)
        self.left_frame.place(relx=0.04, rely=0.15)


    def go_back(self):
        self.parent.destroy()
        self.root = tk.Tk()
        self.main_window = MainWindow(self.root)
        self.root.mainloop()



class TopFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.label = tk.Label(
            master=self,
            text='The Golden Line Restaurent',
            background='#1c1c1c',
            font='{U.S. 101} 30 bold',
            foreground='#f2a343'
            )
        self.label.grid(row=0, column=0)

        self.time = tk.Label(
            master=self,
            text=localtime, 
            background='#1c1c1c',
            font='{U.S. 101} 15 bold',
            foreground='#f2a343'
            )
        self.time.grid(row=1, column=0)


class LeftFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        for i in range(9):
            self.line_frame = LineFrame(self,i, background='#1c1c1c')
            self.line_frame.grid(row=i, column=0, sticky='E')
        
        row = 0
        for i in range(9,18):
            self.line_frame = LineFrame(self,i, background='#1c1c1c')
            self.line_frame.grid(row=row, column=1, sticky='E')
            row += 1


class LineFrame(tk.Frame):

    def __init__(self, master, num, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.num = 0
        self.e_var=tk.StringVar()
        self.data = Data()
        self.data.create_objects()
        self.list = self.data.get_data()

        self.label = tk.Label(
                master=self,
                text=self.list[num].name+' :',
                background='#0a0a0d',
                fg='#f2a343',
                font='{Segoe UI} 18 bold',
                highlightthickness=4,
                highlightbackground='#f2a343'
            )
        self.label.grid(row=0, column=0, pady=15, padx=20, sticky='E')

        self.btn1m = tk.Button(
            master=self,
            text='-',
            height=1,
            font='{Segoe UI} 12 bold',
            bg= '#0a0a0d',
            fg='#f2a343',
            width=2,
            command=self.del_one
        )
        self.btn1m.grid(row=0, column=1, padx=10)
        self.entry1 = tk.Entry(
            master=self,
            text=0,
            width=4,
            font='{Segoe UI} 12 bold',
            highlightthickness=4,
            highlightbackground='#f2a343',
            textvariable=self.e_var,
            state='readonly'
        )
        self.entry1.grid(row=0, column=2, padx=10)
        self.e_var.set('0')


        self.btn1p = tk.Button(
            master=self,
            text='+',
            height=1,
            font='{Segoe UI} 12 bold',
            bg= '#0a0a0d',
            fg='#f2a343',
            width=2,
            command=self.add_one
        )
        self.btn1p.grid(row=0, column=3, padx=10)

  
    def add_one(self):
        self.num += 1
        self.e_var.set(str(self.num))


    def del_one(self):
        if self.num > 0:
            self.num -= 1
            self.e_var.set(str(self.num))


class Table(tk.Frame):

    def __init__(self, master, num, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.label = tk.Label(
            master=self,
            text=f'Table{num}',
            font='{U.S. 101} 15 bold',
            bg='#1c1c1c',
            fg='#f2a343',
            highlightthickness=4,
            highlightcolor='#f2a343',
            highlightbackground='#f2a343'
        )
        self.button = tk.Button(
            master=self,
            text='Order',
            font='{U.S. 101} 15 bold',
            bg='#1c1c1c',
            fg='#f2a343',
            highlightthickness=4,
            highlightbackground='#f2a343',
            command=self.go_second
        )
        
        self.label.grid(row=0, column=0, padx=20, pady=20)
        self.button.grid(row=1, column=0, padx=20, pady=20)

    def go_second(self):
        self.master.destroy()
        self.root = tk.Tk()
        self.second_window = SecondWindow(self.root)
        self.root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
