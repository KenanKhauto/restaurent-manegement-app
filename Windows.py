
__author__ = '7592047, Khauto'

import tkinter as tk
import Frames as tf


class MainWindow(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        parent.title('Restaurant Management')
        parent.geometry('1280x920')
        parent.configure(background='#0a0a0d')
        parent.resizable(False, False)
        

        self.top_frame = tf.TopFrame(
            master=parent,
            background='#1c1c1c',
            highlightthickness=4,
            highlightbackground='#f2a343',

        )

        self.table_frame = tf.TablesFrame(
            master=parent,
            tables_num=6,
            background='#1c1c1c',
            highlightthickness=4,
            highlightbackground='#f2a343'
        )

        self.top_frame.place(relx=0.294, rely=0.02)
        self.table_frame.place(relx=0.1, rely=0.18)


class SecondWindow(tk.Frame):

    def __init__(self, parent, table_name, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        parent.title('Restaurant Management')
        parent.geometry('1280x920')
        parent.configure(background='#0a0a0d')
        parent.resizable(False, False)
        
        self.top_frame = tf.TopFrame(
            master=parent,
            background='#1c1c1c',
            highlightthickness=4,
            highlightbackground='#f2a343'
        )
        self.left_frame = tf.LeftFrame(
            master=parent,
            background='#1c1c1c',
            highlightthickness=4,
            highlightbackground='#f2a343'
        )
        
        self.buttom_frame = tf.BottomFrame(
            master=parent,
            background='#1c1c1c',
            highlightthickness=4,
            highlightbackground='#f2a343'
        )
        
        self.right_frame = tf.RightFrame(
            master=parent,
            highlightthickness=4,
            highlightbackground='#f2a343',
            table_name=table_name
        )
        
        self.buttom_frame.bill_btn.config(command=self.add_bill)
        self.buttom_frame.clear_text.config(command=self.clear_history)
        self.buttom_frame.print_bill.config(command=self.print_bill)
        self.buttom_frame.submit_btn.config(command=self.submit_func)
        self.buttom_frame.back_btn.config(command=self.go_back)

        self.buttom_frame.place(relx=0.04, rely=0.8, width=745)
        self.top_frame.place(relx=0.294, rely=0.02)
        self.left_frame.place(relx=0.04, rely=0.18)
        self.right_frame.place(relx=0.7, rely=0.18, height=668, width=330)
    

    def add_bill(self):
        self.right_frame.text_box.delete('5.0', tk.END)
        x = self.left_frame.line_frame.data.create_bill()
        t = tf.localtime + '\n'
        self.right_frame.text_box.insert(tk.END, x+t)

    def clear_history(self):
        self.right_frame.text_box.delete('5.0', tk.END)
        self.left_frame.line_frame.data.clear_stock() 
        for line_frame in self.left_frame.frames_list:
            line_frame.e_var.set('0')
            line_frame.num = 0

    def submit_func(self):        
        self.root = tk.Tk()
        self.text = 'Succesfully ordered!\nThank you for your order!'
        self.info_window = tf.InfoFrame(self.root, self.text)
        w = 270
        h = 200
        ws = self.root.winfo_screenmmwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/0.6) - (w/3)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.go_back()
        self.root.mainloop()

    def print_bill(self):
        with open('Bill_infos.txt', 'w', encoding='UTF-8') as b:
            b.write(self.right_frame.text_box.get('1.0', tk.END))      
        self.root = tk.Tk()
        self.text = 'Succesfully printed!'
        self.info_window = tf.InfoFrame(self.root, self.text)
        w = 208
        h = 180
        ws = self.root.winfo_screenmmwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/0.6) - (w/3)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.mainloop()
    
    def go_back(self):
        self.clear_history()
        self.parent.destroy()
        self.root = tk.Tk()
        self.main_window = MainWindow(self.root)
        w = 1280
        h = 920
        ws = self.root.winfo_screenmmwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/0.6) - (w/3)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.mainloop()


if __name__ == '__main__':
    
    root = tk.Tk()
    app = MainWindow(root)
    
    w = 1280
    h = 920
    ws = root.winfo_screenmmwidth()
    hs = root.winfo_screenheight()
    x = (ws/0.6) - (w/3)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.mainloop()