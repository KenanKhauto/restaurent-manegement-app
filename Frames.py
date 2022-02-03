
__author__ = '7592047, Khauto'

import tkinter as tk
import time
import Data2 as d
import Windows as mw
localtime = time.asctime(time.localtime(time.time()))


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
        self.frames_list = []
        self.master = master

        for i in range(9):
            self.line_frame = LineFrame(self,i, background='#1c1c1c')
            self.line_frame.grid(row=i, column=0, sticky='E')
            self.frames_list.append(self.line_frame)
        
        row = 0
        for i in range(9,18):
            self.line_frame = LineFrame(self,i, background='#1c1c1c')
            self.line_frame.grid(row=row, column=1, sticky='E')
            self.frames_list.append(self.line_frame)
            row += 1


class LineFrame(tk.Frame):

    def __init__(self, master, num, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.num = 0
        self.num2 = num
        self.e_var=tk.StringVar()
        self.data = d.Data()
        self.data.create_objects()
        self.list = self.data.get_data()
        self.name = f'{self.list[self.num2].name}'


        self.label = tk.Label(
                master=self,
                text=self.list[num].name+' :',
                background='#0a0a0d',
                fg='#f2a343',
                font='{Segoe UI} 12 bold',
                highlightthickness=1,
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
        self.data.put_in_stock(self.list[self.num2])

    def del_one(self):
        if self.num > 0:
            self.num -= 1
            self.e_var.set(str(self.num))
            self.data.remove_from_stock(self.list[self.num2])


class BottomFrame(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.submit_btn = tk.Button(
            master=self,
            text='Submit',
            background='#0a0a0d',
            fg='#f2a343',
            font='{Segoe UI} 14 bold',
            highlightthickness=4,
            highlightbackground='#f2a343',
        )
        
        self.bill_btn = tk.Button(
            master=self,
            text='Generate Bill',
            background='#0a0a0d',
            fg='#f2a343',
            font='{Segoe UI} 14 bold',
            highlightthickness=4,
            highlightbackground='#f2a343'
        )

        self.back_btn = tk.Button(
            master=self,
            text='Back',
            background='#0a0a0d',
            fg='#f2a343',
            font='{Segoe UI} 14 bold',
            highlightthickness=4,
            highlightbackground='#f2a343',

        )

        self.clear_text = tk.Button(
            master=self,
            text='Clear History',
            background='#0a0a0d',
            fg='#f2a343',
            font='{Segoe UI} 14 bold',
            highlightthickness=4,
            highlightbackground='#f2a343'
        )

        self.print_bill = tk.Button(
            master=self,
            text='Print',
            background='#0a0a0d',
            fg='#f2a343',
            font='{Segoe UI} 14 bold',
            highlightthickness=4,
            highlightbackground='#f2a343'
        )


        self.submit_btn.grid(row=0, column=2, padx=20, pady=20)
        self.bill_btn.grid(row=0, column=3, padx=20, pady=20)
        self.print_bill.grid(row=0, column=4, padx=20, pady=20)
        self.clear_text.grid(row=0, column=5, padx=20, pady=20)
        self.back_btn.grid(row=0, column=6, padx=20, pady=20, sticky='E')


class InfoFrame(tk.Frame):

    def __init__(self, master, text, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        master.title('INFO-BOX!')
        master.configure(background='#0a0a0d')
        self.label = tk.Label(
            master=master,
            text=text,
            bg='#0a0a0d',
            highlightthickness=4,
            highlightbackground='#f2a343',
            fg='#f2a343',
            font='{Segoe UI} 16 bold'
        )
        self.btn = tk.Button(
            master=master,
            text='Done!',
            background='#0a0a0d',
            fg='#f2a343',
            font='{Segoe UI} 16 bold',
            highlightthickness=4,
            highlightbackground='#f2a343',
            relief= tk.SUNKEN,
            command=self.master.destroy
        )
        self.label.grid(row=0, column=0, pady=20)
        self.btn.grid(row=1, column=0, pady=20)


class RightFrame(tk.Frame):

    def __init__(self, master, table_name, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.text_box = tk.Text(
            master=self,
            font='{Segoe UI} 10 bold',
        )
        self.text_box.insert(tk.END, table_name)
        self.text_box.place(height=659, width=320)


class Table(tk.Frame):

    def __init__(self, master, num, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.name = f'Table{num}'

        self.label = tk.Label(
            master=self,
            text=f'Table{num}',
            font='{U.S. 101} 15 bold',
            bg='#1c1c1c',
            fg='#f2a343',
            highlightthickness=1,
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
        TablesFrame.destroy_master(self.master)
        self.root = tk.Tk()
        var = '\n****************************************************\n' + self.name + '\n' + '****************************************************\n'
        self.second_window = mw.SecondWindow(self.root, table_name=var)
        w = 1280
        h = 920
        ws = self.root.winfo_screenmmwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/0.6) - (w/3)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.mainloop()


class TablesFrame(tk.Frame):

    def __init__(self, master, tables_num, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.tables_num = tables_num
        x = 1
        for i in range(self.tables_num):
            for j in range(3):
                self.table = Table(
                    master=self,
                    num=x,
                    bg='#0a0a0d',
                    highlightthickness=4,
                    highlightbackground='#f2a343'
                )
                self.table.grid(row=j, column=i, padx=20, pady=20)
                x += 1
    
    def destroy_master(self):
        self.master.destroy()
    
