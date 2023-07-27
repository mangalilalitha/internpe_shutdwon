from tkinter import *
import os

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown -l")

root = Tk()
root.geometry("400x200")

Button(root, text="Shutdown", command=shutdown).grid(row=0)
Button(root, text="Restart", command=restart).grid(row=1)
Button(root, text="Logout", command=logout).grid(row=2)

mainloop()
