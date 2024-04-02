import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_default_color_theme("green")

class Menu():
    def __init__(self,root_tk):
        self.root_tk = root_tk
        self.root_tk.geometry("800x800")
        self.root_tk.title("Menu")
        self.root_tk.config(bg="#f2e4dc")
        fontType=("Verdana",20)
        extras_Font=("Verdana",16)
    

        imagelogo = ctk.CTkImage(Image.open("logo2.png"), size=(180, 180))
        logo = ctk.CTkLabel(master=root_tk, text="", corner_radius=10, image=imagelogo,bg_color="#f2e4dc")
        
        logo.place(x=0, y=0)

        small = ctk.CTkButton(master=root_tk, text="Small",corner_radius=10,height=85,width=150,font=fontType,fg_color="#f2785c",bg_color="#f2e4dc")
        small.place(relx=0.125, rely=0.35, anchor=ctk.CENTER)

        medium = ctk.CTkButton(master=root_tk, text="Medium",corner_radius=10,font=fontType,height=85,width=150,bg_color="#f2e4dc",fg_color="#f2785c") 
        medium.place(relx=0.125, rely=0.50, anchor=ctk.CENTER)
        
        large = ctk.CTkButton(master=root_tk, text="Large", width=150,corner_radius=10,height=85,font=fontType,bg_color="#f2e4dc",fg_color="#f2785c")
        large.place(relx=0.125, rely=0.65, anchor=ctk.CENTER)
        #====================================================================================================================================================

        margherita = ctk.CTkButton(master=root_tk, text="Margherita",corner_radius=10,height=125,width=125,font=fontType,fg_color="#F2A007",bg_color="#f2e4dc")
        margherita.place(relx=0.4, rely=0.22, anchor=ctk.CENTER)

        pepperoni = ctk.CTkButton(master=root_tk, text="Pepperoni",corner_radius=10,font=fontType,height=125,width=130,bg_color="#f2e4dc",fg_color="#F2A007") 
        pepperoni.place(relx=0.4, rely=0.42, anchor=ctk.CENTER)
        
        fourSeasons = ctk.CTkButton(master=root_tk, text="Four\nSeasons", width=130,corner_radius=10,height=125, font=fontType,bg_color="#f2e4dc",fg_color="#F2A007")
        fourSeasons.place(relx=0.4, rely=0.622, anchor=ctk.CENTER)

        icon=ctk.CTkImage(Image.open("checked.png"),size=(90,90))
        confirm=ctk.CTkButton(master=root_tk,text="",width=800,height=20,image=icon,bg_color="#f2e4dc",fg_color="#3ac25c",corner_radius=0,border_color="#f2e4dc",border_width=0)
        confirm.place(relx=0.5,rely=0.8,anchor=ctk.CENTER)



        #====================================================================================================================================================
        
        Rucola = ctk.CTkButton(master=root_tk, text="Rucola",corner_radius=10,height=65,width=150,font=extras_Font,fg_color="#F27649",bg_color="#f2e4dc")
        Rucola.place(relx=0.6, rely=0.35, anchor=ctk.CENTER)

        Mushrooms = ctk.CTkButton(master=root_tk, text="Mushrooms",corner_radius=10,height=65,width=150,font=extras_Font,fg_color="#F27649",bg_color="#f2e4dc")
        Mushrooms.place(relx=0.6, rely=0.45, anchor=ctk.CENTER)

        garlic = ctk.CTkButton(master=root_tk, text="Garlic dip",corner_radius=10,height=65,width=150,font=extras_Font,fg_color="#F27649",bg_color="#f2e4dc")
        garlic.place(relx=0.6, rely=0.55, anchor=ctk.CENTER)

        mayo = ctk.CTkButton(master=root_tk, text="Spicy garlic mayo",corner_radius=10,height=65,width=150,font=extras_Font,fg_color="#F27649",bg_color="#f2e4dc")
        mayo.place(relx=0.6, rely=0.65, anchor=ctk.CENTER)

        coke = ctk.CTkButton(master=root_tk, text="Coke",corner_radius=10,height=65,width=150,font=extras_Font,fg_color="#F27649",bg_color="#f2e4dc")
        coke.place(relx=0.8, rely=0.35, anchor=ctk.CENTER)

        fanta = ctk.CTkButton(master=root_tk, text="Fanta",corner_radius=10,height=65,width=150,font=extras_Font,fg_color="#F27649",bg_color="#f2e4dc")
        fanta.place(relx=0.8, rely=0.45, anchor=ctk.CENTER)

        sprite = ctk.CTkButton(master=root_tk, text="Sprite",corner_radius=10,height=65,width=150,font=extras_Font,fg_color="#F27649",bg_color="#f2e4dc")
        sprite.place(relx=0.8, rely=0.55, anchor=ctk.CENTER)

        water = ctk.CTkButton(master=root_tk, text="Water",corner_radius=10,height=65,width=150,font=extras_Font,fg_color="#F27649",bg_color="#f2e4dc")
        water.place(relx=0.8, rely=0.65, anchor=ctk.CENTER)


root_tk=ctk.CTk()
app=Menu(root_tk)
root_tk.mainloop()
    
