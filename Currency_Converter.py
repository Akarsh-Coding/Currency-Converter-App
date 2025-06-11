from currency_converter import CurrencyConverter

import tkinter as tk
from tkinter import ttk, font as tkfont,messagebox
from PIL import Image,ImageTk


class CurrencyConverterApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("500x600")
        self.root.resizable(False,False)
        self.root.config(bg="#1C1C1C")


        # App Title
        lab_title=tk.Label(self.root,text="Currency Converter",bg= "#1C1C1C",fg= "#00FF00" ,
        font=("Harlow Solid Italic",40,) if "Harlow Solid Italic" in tkfont.families() else ("Times New Roman",38,"bold"),)
        lab_title.place(x=0, y=10, height=60, width=500)


        # Displaying top image banner
        img_1 = Image.open("img_2.png")
        img_1 = img_1.resize((512,150), Image.Resampling.LANCZOS)
        self.photo_1 = ImageTk.PhotoImage(img_1)

        l_lbl = tk.Label(self.root, image=self.photo_1, bg="#D3D3D3")
        l_lbl.place(x=0, y=85,width=500,height=150)
        l_lbl.config(anchor="center")


        # Instructional message
        lbl_msg=tk.Label(self.root, 
                        font= ("Times New Roman", 16,),bg= "#1C1C1C",fg= "#0DE3EA",
                        text="Convert amounts between currencies quickly and easily.",)
        lbl_msg.place(x=0, y=245, width=500)


        # Frame for currency dropdowns
        frame_currency = tk.Frame(self.root, bg="#1c1c1c")
        frame_currency.place(y=290,x=8)


        # Dictionary of currency codes and full names
        currency_full_names = {"AUD":"Australian Dollar","BGN":"Bulgarian Lev","BRL":"Brazilian Real",
    "CAD":"Canadian Dollar","CHF":"Swiss Franc","CNY":"Chinese Yuan","CYP":"Cypriot Pound",
    "CZK":"Czech Koruna","DKK":"Danish Krone","EEK":"Estonian Kroon","EUR":"Euro",
    "GBP":"British Pound Sterling","HKD":"Hong Kong Dollar","HRK":"Croatian Kuna",
    "HUF":"Hungarian Forint","IDR":"Indonesian Rupiah","ILS":"Israeli New Shekel","INR":"Indian Rupee",
    "ISK":"Icelandic Krona","JPY":"Japanese Yen","KRW":"South Korean Won","LTL":"Lithuanian Litas",
    "LVL":"Latvian Lats","MTL":"Maltese Lira","MXN":"Mexican Peso","MYR":"Malaysian Ringgit",
    "NOK":"Norwegian Krone","NZD":"New Zealand Dollar","PHP":"Philippine Peso","PLN":"Polish Zloty",
    "ROL":"Romanian Leu (Old)","RON":"Romanian Leu","RUB":"Russian Ruble","SEK":"Swedish Krona",
    "SGD":"Singapore Dollar","SIT":"Slovenian Tolar","SKK":"Slovak Koruna","THB":"Thai Baht",
    "TRL":"Turkish Lira (Old)","TRY":"Turkish Lira","USD":"United States Dollar","ZAR":"South African Rand"}
        currency_options = [f"{code} - {name}" for code, name in currency_full_names.items()]   # Format currency options for dropdown


        # "From" Currency Label & Combobox
        from_lbl =tk.Label(frame_currency,
                            text="From:",font=("Arial", 14, "bold"),fg="#ffffff",bg='#1c1c1c')
        from_lbl.grid(row=0, column=0, padx=8)

        self.comb_from=ttk.Combobox(frame_currency,font=("Arial",12),width=15,
                                    value=currency_options,state="readonly")
        self.comb_from.grid(row=1, column=0, padx=5)
        self.comb_from.set("INR - Indian Rupee") 

        # Interchange Button and Icon
        img_IC = Image.open("interchange.png")
        img_IC = img_IC.resize((80,45), Image.Resampling.LANCZOS)
        self.photo_IC = ImageTk.PhotoImage(img_IC)

        btn_interchange=tk.Button(frame_currency,image=self.photo_IC,width=80,height=45,relief="flat",
                                    command=self.interchange_currency)
        btn_interchange.grid(row=1, column=1, padx=5)

        # "To" Currency Label & Combobox
        to_lbl =tk.Label(frame_currency,
                            text="To:",font=("Arial", 14, "bold"),fg="#ffffff",bg='#1c1c1c')
        to_lbl.grid(row=0, column=2, padx=8)

        self.comb_to = ttk.Combobox(frame_currency,font=("Arial",12),width=15,
                                    value=currency_options,state="readonly")
        self.comb_to.grid(row=1, column=2, padx=5)
        self.comb_to.set("USD - United States Dollar") 

        # Amount Input Label & Entry
        amount_lbl=tk.Label(self.root,
            text="Enter Amount here:",font=("Arial", 14, "bold"),fg="#ffffff",bg='#1c1c1c')
        amount_lbl.place(x=10,y=400)
        self.amount_entry= ttk.Entry(self.root,font=("Arial", 14, "bold"))
        self.amount_entry.place(x=200,y=400)


        # Output Labels
        self.output_lbl_1 = tk.Label(self.root,font= ("Times New Roman", 16,),bg= "#1c1c1c", 
                            fg= "#0DE3EA",text="Enter amount and click Convert",)
        self.output_lbl_1.place(x=0, y=460, width=500)

        self.output_lbl_2 = tk.Label(self.root, 
                            text=" ",bg= "#1c1c1c",
                            font= ("Times New Roman", 20,"bold"),fg= "#0DE3EA" )
        self.output_lbl_2.place(x=0, y=490, width=500)

        # Convert Button
        btn_convert = tk.Button(self.root, text="Convert",font=("Arial", 14, "bold"),bg="#2196F3",
            fg="#FFFFFF",activebackground="#2196F3",activeforeground="#FFFFFF",
                                command=self.convert_currency)
        btn_convert.place(rely=0.955,relx=0.5,anchor="center")



        # Function to swap the selected currencies
    def interchange_currency(self):
        from_curr = self.comb_from.get()
        to_curr = self.comb_to.get()
        self.comb_from.set(to_curr)
        self.comb_to.set(from_curr)


        # Function to perform currency conversion
    def convert_currency(self):
        # If amount is not enter
        if not self.amount_entry.get().strip():
            messagebox.showwarning("⚠️ Input Required", "Please enter an amount to convert.")
            return

        try:
            # Retrieve amount and selected currencies
            amount = float(self.amount_entry.get())
            from_curr = self.comb_from.get().split(" - ")[0]
            to_curr = self.comb_to.get().split(" - ")[0]
            # Use CurrencyConverter library to get the result
            converter = CurrencyConverter()
            result = converter.convert(amount, from_curr, to_curr)
            # Update output labels
            self.output_lbl_1.config(text=f"{amount} {self.comb_from.get().split(' - ')[1]} equals to")
            self.output_lbl_2.config(text=f"{result:.2f} {self.comb_to.get().split(' - ')[1]}")
            self.amount_entry.delete(0, tk.END)     # Clear input
        # If amount is not numeric
        except ValueError:
            messagebox.showerror("❌ Invalid Input", "⚠️ Please enter a valid number amount (e.g., 100.00).")
            self.amount_entry.delete(0, tk.END)
        # Handle other exceptions
        except Exception as e:
            messagebox.showerror("❌ Conversion Failed", f"⚠️ Unable to convert currency.\nDetails: {str(e)}")



if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
