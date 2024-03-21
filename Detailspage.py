import customtkinter as ctk
from PIL import Image, ImageTk
from page1 import DeliveryCollection as DC





ctk.set_appearance_mode("light")

class GUI_badnumber():
    
    def __init__(self,root_tk):
        self.root_tk=root_tk
        self.root_tk.geometry("700x700")
        self.root_tk.title("CustomTkinter Test")
        placeholder_font=("Verdana",16)
        

        self.fname_entry=ctk.CTkEntry(master=root_tk,placeholder_text="First Name:",corner_radius=10,height=50,width=150,font=placeholder_font,border_width=0)
        self.fname_entry.place(relx=0.3,rely=0.04)

        self.lname_entry=ctk.CTkEntry(master=root_tk,placeholder_text="Last Name:",corner_radius=10,height=50,width=150,font=placeholder_font,border_width=0)
        self.lname_entry.place(relx=0.57,rely=0.04)

        self.area_code=ctk.CTkEntry(master=root_tk,placeholder_text="Area Code",corner_radius=10,height=50,width=100,font=placeholder_font,border_width=0)
        self.area_code.place(relx=0.3,rely=0.15)
        
        self.number=ctk.CTkEntry(master=root_tk,placeholder_text="Phone Number",corner_radius=10,height=50,width=150,font=placeholder_font,border_width=0)
        self.number.place(relx=0.57,rely=0.15)

        

        self.submit_button=ctk.CTkButton(master=root_tk,text="Submit",command=self.submit)
        self.submit_button.place(relx=0.4,rely=0.28)



        self.img=ctk.CTkImage(Image.open("logo2.png"),size=(150,150))
        self.logo=ctk.CTkLabel(master=root_tk,text="",corner_radius=10,image=self.img)
        self.logo.place(x=0,y=0)

    def submit(self):
        first_name=self.fname_entry.get()
        last_name=self.lname_entry.get()
        if first_name and last_name:
            print(first_name,last_name)
        else:
            print("False")

        

        


class GUI_numberConfirmed():
    def __init__(self,root_tk):
        self.root_tk=root_tk



if True:
    root_tk=ctk.CTk()

    app=GUI_badnumber(root_tk)
    root_tk.mainloop()
