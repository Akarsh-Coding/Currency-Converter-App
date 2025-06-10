from currency_converter import CurrencyConverter
from currency_converter import CURRENCY_FILE

import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from PIL import Image,ImageTk


class CurrencyConverterApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("500x600")
        self.root.resizable(False,False)



        # title
        lab_title=tk.Label(self.root, 
                            text="Currency Converter",
                            font= ("Harlow Solid Italic", 40,) if "Harlow Solid Italic" in tkfont.families() else ("Times New Roman", 38, "bold"), 
                            bg= "#1C1C1C", 
                            fg= "#00FF00" )
        lab_title.place(x=0, y=10, height=60, width=500)



        # Display image
        img_1 = Image.open("img_2.png")
        img_1 = img_1.resize((512,150), Image.Resampling.LANCZOS)
        self.photo_1 = ImageTk.PhotoImage(img_1)

        l_lbl = tk.Label(self.root, image=self.photo_1, bg="#D3D3D3")
        l_lbl.place(x=0, y=85,
                    width=500,
                    height=150)
        l_lbl.config(anchor="center")



        # message
        lbl_msg=tk.Label(self.root, 
                            text="Convert amounts between currencies quickly and easily.",
                            font= ("Times New Roman", 16,) ,
                            bg= "#1C1C1C", 
                            fg= "#0DE3EA" )
        lbl_msg.place(x=0, y=245, width=500)



        # Currency Selection Frame
        frame_currency = tk.Frame(self.root, bg="#1c1c1c")
        frame_currency.place(y=290,x=8)

        # list_text = list(currency)

        from_lbl =tk.Label(frame_currency,
                            text="From:",font=("Arial", 14, "bold"),fg="#ffffff",bg='#1c1c1c')
        from_lbl.grid(row=0, column=0, padx=10)

        self.comb_from = ttk.Combobox(frame_currency, 
                                # value=list_text, 
                                font=("Arial", 14), width=12)
        self.comb_from.grid(row=1, column=0, padx=10)
        self.comb_from.set("INR") 

        img_IC = Image.open("interchange.png")
        img_IC = img_IC.resize((80,45), Image.Resampling.LANCZOS)
        self.photo_IC = ImageTk.PhotoImage(img_IC)

        btn_interchange=tk.Button(frame_currency,
                            image=self.photo_IC,
                            width=80,height=45,relief="flat")
        
        btn_interchange.grid(row=1, column=1, padx=10)

        to_lbl =tk.Label(frame_currency,
                            text="To:",font=("Arial", 14, "bold"),fg="#ffffff",bg='#1c1c1c')
        to_lbl.grid(row=0, column=2, padx=10)

        self.comb_to = ttk.Combobox(frame_currency, 
                                # value=list_text,
                                font=("Arial", 14), width=12)
        self.comb_to.grid(row=1, column=2, padx=10)
        self.comb_to.set("USD") 

        amount_lbl=tk.Label(self.root,
                            text="Enter Amount here:",font=("Arial", 14, "bold"),fg="#ffffff",bg='#1c1c1c')
        amount_lbl.place(x=10,y=400)
        self.amount_entery= ttk.Entry(self.root,font=("Arial", 14, "bold"))
        self.amount_entery.place(x=200,y=400)


        output_lbl_1 = tk.Label(self.root, 
                            text="1 United States Dollar equals",
                            font= ("Times New Roman", 16,) ,
                            bg= "#1c1c1c", 
                            fg= "#0DE3EA" )
        output_lbl_1.place(x=0, y=460, width=500)

        output_lbl_2 = tk.Label(self.root, 
                            text="85.62 Indian Rupee",
                            font= ("Times New Roman", 20,"bold") ,
                            bg= "#1c1c1c", 
                            fg= "#0DE3EA" )
        output_lbl_2.place(x=0, y=490, width=500)


        btn_convert = tk.Button(self.root, text="Convert", 
                                    font=("Arial", 14, "bold"),
                                    bg="#2196F3", fg="#FFFFFF",
                                    activebackground="#2196F3",
                                    activeforeground="#FFFFFF",
                                # command=data
                                        )
        btn_convert.place(rely=0.955,relx=0.5,anchor="center")





if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="#1C1C1C")
    app = CurrencyConverterApp(root)
    root.mainloop()


