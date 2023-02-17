from tkinter import *
from tkinter import ttk   #เปลี่ยนหน้าตาปุ่ม(theme of tk)
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกจำนวน')
GUI.geometry('500x400')
# โหลดรูป
image = PhotoImage(file="C:\Users\AstarCom\Pictures\BankCard1.jpg.jpg" ))

# แสดงรูปภาพ
L1 = Label(GUI, image=image)
L1.place(x=0, y=0)

# บรรทัดตัวอักษร
L2 = Label(GUI, text='โปรแกรมนับยอด', font=('Angsana new', 70), fg='#00FF00')
L2.place(x=2, y=2)

# ปุ่ม
B1 = ttk.Button(GUI, text='สตางค์')
B1.pack(ipadx=10, ipady=10)
B1.place(x=120, y=250)
B2 = ttk.Button(GUI, text='ธนบัตร')
B2.pack(ipadx=10, ipady=10)
B2.place(x=160, y=260)

# ฟังก์ชันแจ้งเตือน
def Button2():
    text = 'จำนวณ'
    messagebox.showinfo('จำนวณ', text)

FB1 = Frame(GUI)
FB1.place(x=150, y=300)
B2 = ttk.Button(FB1, text='นับได้รวม', command=Button2)
B2.pack(ipadx=10, ipady=10)

def Button3():
    text='จำนวณใบ'
    messagebox.showinfo('20,50,100,500,1000', text)

FB2 = Frame(GUI)
FB2.place(x=200, y=380)
B3 = ttk.Button(FB1, text=





       
