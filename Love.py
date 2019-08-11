# Shuffle-Wedding-Songs
# Shuffles through song titles that were on our wedding CD

from tkinter import *
from random import choice

exps = ["Let it be me", "I can't help falling in love with you", "I want to hold your hand", "Let's get it on",
        "Let my love open the door", "You are the best thing", "Crazy Beautiful",
        "and I love her", "Wouldn't it be nice", "Until the end of time", "Adorn", "Stay with you",
        "Each day gets better", "We found love", "How can I tell you"]

root = Tk()
root.title("For My Wife")

lb = Label(root, text="KK")
lb.pack(pady=30)

def express():
    lb["text"] = choice(exps)

Button(root, text="PRESS", command=express).pack(pady=20)
root.geometry("350x250+400+400")

root.mainloop()
