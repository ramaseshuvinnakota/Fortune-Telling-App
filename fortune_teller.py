import tkinter as tk
import tkinter.messagebox as messagebox
import random
from PIL import Image, ImageTk

#return fortune phrase
def say_my_fortune():
  fortunes_list = ["A beautiful, smart, and loving person will be coming into your life.", 
                   "A dubious friend may be an enemy in camouflage.",
                   "A faithful friend is a strong defense.",
                   "A feather in the hand is better than a bird in the air.",
                   "A fresh start will put you on your way.",
                   "A friend asks only for your time not your money.",
                   "A friend is a present you give yourself.",
                   "A funny coincidence will make your day.",
                   "A gambler not only will lose what he has, but also will lose what he doesn’t have.",
                   "A golden egg of opportunity falls into your lap this month.",
                   "A good friendship is often more important than a passionate romance."
                  ]
  
  your_fortune = random.choice(fortunes_list)
  msg = messagebox.showinfo(title="Here it is!", message=your_fortune)

#create tkinter window
root = tk.Tk()
root.title("Fortune Teller")
root.geometry("1080x1080")

#set image as background
image = Image.open("./img/Zoltar Speaks.png")
photo = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Label text on window
label = tk.Label(text="Want to Know your Fortune? \n",font="Arial", fg="black", bg="white")
label.pack(anchor="center")
label.place(x=400, y=300)

#btn for replying
button = tk.Button(root, text="YES!", command=say_my_fortune, width=10, height=2)
button.place(x=390, y=560)

root.mainloop()
