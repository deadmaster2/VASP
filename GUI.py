from tkinter import *
import os

def bot_gui():
    root = Tk()
    root.title('VASP')
    root.geometry('500x600')
    root.configure(bg='#49A')

    main_menu = Menu(root)
    main_menu.add_command(label='File')
    main_menu.add_command(label='Edit')
    main_menu.add_command(label='Quit')
    root.config(menu=main_menu)

    Label(root, text='V.A.S.P', font=('Helvetica', 35), bg="#49A").pack(side=TOP)
    Label(root, text='Virtual Assistant Simulation with Python', font=('Helvetica', 10), bg="#49A").pack(side=TOP, pady=2)
    mic = PhotoImage(file = r"D:\PROJECTS\BE Project\BE PROJECT\Webp.net-resizeimage.gif")

    def call_main():
        os.system('python Assistant.py')

    def end():
        exit(0)

    Button(root, image=mic, compound=LEFT).pack(side=TOP, pady=10)
    btn1 = Button(root, text="STOP", bg="black", fg="white", command=end)
    btn1.pack(side=BOTTOM, pady=60)

    btn2 = Button(root, text="START", bg="black", fg="white", command=call_main)
    btn2.pack(side=BOTTOM, pady=60)
    root.mainloop()

if __name__ == '__main__':
    bot_gui()