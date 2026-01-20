import tkinter as ui

clickCount = 0
clicksPerSec = 0
clicksPerClick = 1

root = ui.Tk()
root.title("Clicker Game")
root.geometry("600x400")

label1 = ui.Label(root, text="Click Button To Start", font=("Arial", 26), fg="blue")
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = ui.Label(root, text="Clicks per second: " + str(clicksPerSec), font=("Arial", 20), fg="blue")
label2.place(x=12, y=60)
label3 = ui.Label(root, text="Clicks per click: " + str(clicksPerClick), font=("Arial", 20), fg="blue")
label3.place(x=12, y=100)

def buttonClick():
    global clickCount
    clickCount = clickCount + clicksPerClick
    label1.config(text="Score: " + str(clickCount))

def clickPerSec():
    global clickCount
    global clicksPerSec
    clickCount = clickCount + clicksPerSec

def recieveCPS():
    root.after(1000, clickPerSec)
    root.after(1000, recieveCPS)
    label1.config(text="Score: " + str(clickCount))
    label2.config(text="Clicks per second: " + str(clicksPerSec), font=("Arial", 20), fg="blue")

def upgrade1():
    global clickCount
    global clicksPerSec
    if clickCount > 9:
        clicksPerSec = clicksPerSec + 1
        clickCount = clickCount - 10

def upgrade2():
    global clickCount
    global clicksPerClick
    if clickCount > 14:
        clicksPerClick = clicksPerClick + 1
        clickCount = clickCount - 15
        label3.config(text="Clicks per click: " + str(clicksPerClick))

def updateButton():
    if clickCount > 14:
        button3.config(bg="green")
    else:
        button3.config(bg="gray")
    if clickCount > 9:
        button2.config(bg="green")
    else:
        button2.config(bg="gray")
    root.after(100, updateButton)

def infoWin():
    win2 = ui.Tk()
    win2.title("Info Screen")
    win2.geometry("400x300")
    infoBox = ui.Message(win2, text="CPS = Clicks Per Second CPC = Clicks Per Click", fg="black", font=("Arial", 16))
    infoBox.place(x=0, y=0)
    infoBox.config(width=320)
    infoBox2 = ui.Message(win2, text="Clicker game, coded by Xander Livingstone", fg="black", font=("Arial", 16))
    infoBox2.place(x=0, y=235)
    infoBox2.config(width=320)

button1 = ui.Button(root, text="Clicker", command=buttonClick, fg="white", bg="red", font=("Arial", 26))
button1.place(x=220, y=175)
button2 = ui.Button(root, text="+1 CPS, -$10", command=upgrade1, fg="white", bg="gray", font=("Arial", 16))
button2.place(x=12, y=338)
button3 = ui.Button(root, text="+1 CPC, -$15", command=upgrade2, fg="white", bg="gray", font=("Arial", 16))
button3.place(x=12, y=285)
infoButton = ui.Button(root, text="INFO", command=infoWin, fg="white", bg="black", font=("Arial", 16))
infoButton.place(x=510, y=10)

recieveCPS()
updateButton()
root.mainloop()
