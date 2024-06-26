import customtkinter as ctk
from PIL import Image, ImageTk
from page1 import DeliveryCollection as DC
import random
import csv
import phonenumbers





ctk.set_appearance_mode("light")


#=====================================================================================================================================
        


class delivery():
    def __init__(self, root_tk):
        self.root_tk = root_tk
        self.root_tk.geometry("700x700")
        self.root_tk.title("Details")
        placeholder_font=("Verdana",16)
        self.address=[]
        

        self.fname_entry=ctk.CTkEntry(master=root_tk,placeholder_text="First Name:",corner_radius=10,height=50,width=150,font=placeholder_font,border_width=0)
        self.fname_entry.place(relx=0.27,rely=0.04)

        self.lname_entry=ctk.CTkEntry(master=root_tk,placeholder_text="Last Name:",corner_radius=10,height=50,width=150,font=placeholder_font,border_width=0)
        self.lname_entry.place(relx=0.6,rely=0.04)

        self.area_code=ctk.CTkEntry(master=root_tk,placeholder_text="Area Code",corner_radius=10,height=50,width=100,font=placeholder_font,border_width=0)
        self.area_code.place(relx=0.27,rely=0.15)
        
        self.number=ctk.CTkEntry(master=root_tk,placeholder_text="Phone Number",corner_radius=10,height=50,width=150,font=placeholder_font,border_width=0)
        self.number.place(relx=0.6,rely=0.15)

        self.streetno=ctk.CTkEntry(master=root_tk,placeholder_text="Street No.",font=placeholder_font,corner_radius=10,height=50,width=100,border_width=0)
        self.streetno.place(relx=0.05,rely=0.26)

        self.addressline1=ctk.CTkEntry(master=root_tk,placeholder_text="Address Line 1.",font=placeholder_font,corner_radius=10,height=50,width=200,border_width=0)
        self.addressline1.place(relx=0.27,rely=0.26)

        self.addressline2=ctk.CTkEntry(master=root_tk,placeholder_text="Address Line 2.",font=placeholder_font,corner_radius=10,height=50,width=200,border_width=0)
        self.addressline2.place(relx=0.6,rely=0.26)

        self.city=ctk.CTkEntry(master=root_tk,placeholder_text="City",font=placeholder_font,corner_radius=10,height=50,width=100,border_width=0)
        self.city.place(relx=0.27,rely=0.36)

        self.eircode=ctk.CTkEntry(master=root_tk,placeholder_text="Eircode",font=placeholder_font,corner_radius=10,height=50,width=100,border_width=0)
        self.eircode.place(relx=0.6,rely=0.36)



        self.ordernotes=ctk.CTkEntry(master=root_tk,placeholder_text="ORDER NOTES:",corner_radius=10,height=100,width=250,font=placeholder_font,border_width=2)
        self.ordernotes.place(relx=0.15,rely=0.5)

        self.customernotes=ctk.CTkEntry(master=root_tk,placeholder_text="CUSTOMER NOTES:",font=placeholder_font,corner_radius=10,height=100,width=250,border_width=2)
        self.customernotes.place(relx=0.55,rely=0.5)
        

        self.submit_button=ctk.CTkButton(master=root_tk,text="Submit",command=self.submit)
        self.submit_button.place(relx=0.4,rely=0.7)
        
        



        self.img=ctk.CTkImage(Image.open("logo2.png"),size=(150,150))
        self.logo=ctk.CTkLabel(master=root_tk,text="",corner_radius=10,image=self.img)
        self.logo.place(x=0,y=0)

    def submit(self):
        #Check if the inputs for first and last name are good
        fname_valid = self.validation_name_checker(self.fname_entry.get())
        lname_valid = self.validation_name_checker(self.lname_entry.get())

        # Check if the inputs for area code and number are valid
        area_code_valid = self.validate_area_code(self.area_code.get())
        number_valid = self.validate_phone_number(self.number.get())#

        address_valid=self.address_check(self.streetno.get(),self.addressline1.get(),self.addressline2.get(),self.city.get(),self.eircode.get())


        # If all inputs are valid, proceed
        if fname_valid and lname_valid and area_code_valid and number_valid and address_valid:
            receipt_number = self.generate_receipt_number()
            address=(f'{self.streetno.get()},{self.addressline1.get()},{self.addressline2.get()},{self.city.get()},{self.eircode.get()}')
    
            print("True")
    


            # Collect all valid inputs
            data = {
                "Receipt Number": receipt_number,
                "First Name": self.fname_entry.get(),
                "Last Name": self.lname_entry.get(),
                "Area Code": self.area_code.get(),
                "Phone Number": self.number.get(),
                "Address": address
            }

            # Write data to CSV file
            with open('customer-details.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())

                # If the file is empty, write headers
                if file.tell() == 0:
                    writer.writeheader()

                # Write data to the file
                writer.writerow(data)
       
    
    def validate_area_code(self, country_input):
        try:
            # Check if the country code is valid
            if not phonenumbers.region_code_for_country_code(int(country_input)):
                return False
        except ValueError:
            return False
        return True
    
    def validate_phone_number(self, number):
        if not number.isdigit() or len(number) != 9:
            return False
        return True

    def get_customer_info_by_receipt(self, receipt_number):
        # Search for customer information by receipt number
        with open('customer-details.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Receipt Number"] == receipt_number:
                    return {
                        "Receipt Number": row["Receipt Number"],
                        "First Name": row["First Name"],
                        "Last Name": row["Last Name"],
                        "Area Code": row["Area Code"],
                        "Phone Number": row["Phone Number"]
                    }
        return None  # Return None if receipt number not found

    def generate_receipt_number(self):
        # Generate a random receipt number between 1 and 10000
        receipt_number = random.randint(1, 10000)
        return receipt_number
    
    def validation_name_checker(self, name):
        if len(name.strip()) > 30 or len(name.strip()) == 0:
            #We can change this print statement to something else later
            print("\nSorry your name is too long long.")
            return False
        return True
    
    def address_check(self,streetNo,addressLine1,addressLine2,city,eircode):
        count=0
        while count<3:
            if streetNo.isdigit():
                print(True)
                count+=1

            else:
                print("Please enter a valid numerical input!")
            if len(addressLine1) and len(addressLine2) and len(city) > 0:
                print("True2")
                count+=1
        
            else:
                print("Please enter a valid address!")
            if len(eircode.upper())==7:
                count+=1
                print("True3")
               
            else:
                print("Please enter a valid Eircode!")
        if count ==3:
            return True
        
        
        
    




root_tk=ctk.CTk()
app=delivery(root_tk)
root_tk.mainloop()