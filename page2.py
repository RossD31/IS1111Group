import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

def create_root():
    root = ctk.CTk()
    root.title("Order Confirmation")
    root.geometry("1400x800")
    
    
    text_label = ctk.CTkLabel(root, text="Order Number: , is confirmed", font=("Helvetica", 22, "bold"))
    text_label.place(relx=0.52, rely=0.2, anchor=ctk.CENTER)
    
    text_label = ctk.CTkLabel(root, text="Print receipt here", font=("Helvetica", 20))
    text_label.place(relx=0.52, rely=0.4, anchor=ctk.CENTER)
    
    imagelogo = ctk.CTkImage(Image.open("logo2.png"), size=(180, 180))
    logo = ctk.CTkLabel(master=root, text="", corner_radius=10, image=imagelogo)
    logo.place(x=0, y=0)
    
    new_order_button = ctk.CTkButton(root, text="New Order", command=new_order)
    new_order_button.place(relx=0.93, rely=0.95, anchor=ctk.CENTER)


    root.mainloop()
    
def new_order():
    print("New Order button clicked")

create_root()
