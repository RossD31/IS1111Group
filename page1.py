import customtkinter as ctk

import tkinter as tk

from PIL import Image, ImageTk



class DeliveryCollection(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Delivery and Collection")

        self.geometry("1400x800")



        self.buttons()



    def buttons(self):

        delivery_button = ctk.CTkButton(master=self, text="Delivery", corner_radius=10, command=self.deliver_order,

                                        width=360, height=600, border_width=0,

                                        fg_color=("lightblue"),  

                                        font=("Helvetica", 40, "bold"))  

        delivery_button.place(relx=0.4, rely=0.55, anchor=ctk.CENTER)



        collection_button = ctk.CTkButton(master=self, text="Collection", corner_radius=10, command=self.collect_order,

                                          width=360, height=600, border_width=0,

                                          fg_color=("lightgreen"), 

                                          font=("Helvetica", 40, "bold"))  

        collection_button.place(relx=0.7, rely=0.55, anchor=ctk.CENTER)



        image_logo = Image.open("logo2.png")

        imagelogo = ctk.CTkImage(image_logo, size=(180, 180))

        logo = ctk.CTkLabel(master=self, text="", corner_radius=10, image=imagelogo)

        logo.place(x=0, y=0)

        

        self.area=ctk.CTkEntry(master=self,placeholder_text="Area Code",corner_radius=10,border_width=0, width=90)

        self.area.place(relx=0.44, rely=0.08, anchor=ctk.CENTER)

        

        self.number_entry=ctk.CTkEntry(master=self,placeholder_text="Customers Phone Number",corner_radius=10,border_width=0, width=200)

        self.number_entry.place(relx=0.55, rely=0.08, anchor=ctk.CENTER)

        

        submit_button = ctk.CTkButton(master=self, text="Submit", command=self.submit_phone, width=10,corner_radius=10)

        submit_button.place(relx=0.65, rely=0.08, anchor=ctk.CENTER)





    

    def deliver_order(self):

        print("Delivery button clicked")



    def collect_order(self):

        print("Collection button clicked")

        

    def submit_phone(self):

        

        area_code = self.area.get()

        if area_code.strip() == "" or not area_code.isdigit() or len(area_code) != 3:

            tk.messagebox.showerror("Error", "Please enter a valid area code with 3 digits.")

            return

        

        phone_number = self.number_entry.get()

        if phone_number.strip() == "" or not phone_number.isdigit() or len(phone_number) != 9:

            tk.messagebox.showerror("Error", "Please enter a valid phone number with 9 digits.")

            return





        print("Area code:", area_code)

        print("Phone number:", phone_number)





if __name__ == "__main__":

    app = DeliveryCollection()

    app.mainloop()

