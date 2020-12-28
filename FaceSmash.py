from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

global img
global count_1
global count_2
count_1 = 1
count_2 = 2

def main():
   root = Tk()

   image1 = Image.open('Photo'+str(count_1)+'.jpg')
   image1 = image1.resize((450, 350), Image. ANTIALIAS)
   img_1 = ImageTk.PhotoImage(image1)

   image2 = Image.open('Photo'+str(count_2)+'.jpg')
   image2 = image2.resize((450, 350), Image. ANTIALIAS)
   img_2 = ImageTk. PhotoImage(image2)


   def button_like():
       root.destroy()
       return

   def button_dislike():
       root.destroy()
       return
   #Image Display

   first_image= Label(root,image = img_1)
   second_image= Label(root,image = img_2)

   #Button Display
   button_like =Button(root, text ='Like', padx =39, pady=20,command= button_like)
   button_dislike =Button(root, text ='Dislike', padx =39, pady=20, command= button_dislike)

   #Button Display

   first_image.grid(row=0,column=0)
   second_image.grid(row=0,column=1)
   button_like.grid(row=1,column=0)
   button_dislike.grid(row=1,column=1)
   root.mainloop()

while True:
    main()
    count_1 += 2
    count_2 += 2
