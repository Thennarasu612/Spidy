from PIL import Image, ImageTk,ImageDraw
import tkinter as tk
#background
window = tk.Tk()
window.geometry("400x600")
background_image = Image.open('back.jpg')
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#logo
pil_img = Image.open('co.jpeg')
pil_img = pil_img.resize((150, 150))
pil_img = pil_img.convert("RGBA")
mask = Image.new('L', pil_img.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + pil_img.size, fill=255)
pil_img.putalpha(mask)
logo_photo = ImageTk.PhotoImage(pil_img)
logo_label = tk.Label(window, image=logo_photo, bg=None)
logo_label.place(relx=0.88, rely=0.01)
#menu
menu_label = tk.Label(window, text="Hello, welcome to Asian food page!", font=("Impact", 24, "bold underline"), bg=None, highlightthickness=0, borderwidth=0)
menu_label.place(relx=0.3,rely=0.01)
menu_description_label = tk.Label(window, text="Select your meal:", font=("Arial", 16,"bold"),bg=None)
menu_description_label.place(relx=0.5, rely=0.27, anchor="s")
order_var = tk.StringVar()
options = ["Briyani", "Parotta set", "Quater meals", "Half meals", "Full meals", "Curd rice", "Lemon rice", "Tomato rice"]
dropdown = tk.OptionMenu(window, order_var, *options)
dropdown.place(relx=0.5, rely=0.3, anchor="center")
order_status_label = tk.Label(window,text="", font=("Arial", 14,"bold"), wraplength=400)
order_status_label.place(relx=0.5, rely=0.73, anchor="center")
#logical statement
def submit_order():
    order = order_var.get()
    if order == "Briyani":
        order_status_label.config(text="Your order is placed....payable amount is 160 dollar.....Thank you for visit Taste your food have a nice day",font=("Didot", 12),bg=None)
    elif order == "Parotta set":
        order_status_label.config(text="Your order is placed....payable amount is 50 dollar.......Thanks you for visit ....Taste your food...Have a nice day",font=("Arial", 12, "bold"),bg=None)
    elif order == "Quater meals":
        order_status_label.config(text="Your order is placed....payable amount is 70 dollar.......Thanks you for visit ....Taste your food...Have a nice day",font=("Arial", 12, "bold"),bg=None)
    elif order == "Half meals":
        order_status_label.config(text="Your order is placed....payable amount is 140 dollar.......Thanks you for visit ....Taste your food...Have a nice day",font=("Arial", 12, "bold"),bg=None)
    elif order == "Full meals":
        order_status_label.config(text="Your order is placed....payable amount is 210 dollar.......Thanks you for visit ....Taste your food...Have a nice day",font=("Arial", 12, "bold"),bg=None)
    elif order == "Curd rice":
        order_status_label.config(text="Your order is placed....payable amount is 60 dollar.......Thanks you for visit ....Taste your food...Have a nice day",font=("Arial", 12, "bold"),bg=None)
    elif order == "Lemon rice":
        order_status_label.config(text="Your order is placed....payable amount is 60 dollar.......Thanks you for visit ....Taste your food...Have a nice day",font=("Arial", 12, "bold"),bg=None)
    elif order == "Tomato rice":
        order_status_label.config(text="Your order is placed....payable amount is 60 dollar.......Thanks you for visit ....Taste your food...Have a nice day",font=("Arial", 12, "bold"),bg=None)
    else:
        order_status_label.config(text="i could not catch you this time. sorry for the delay",font=("Didot", 12, "bold"),bg=None)
# drink menu
drinks_label = tk.Label(window, text="select your drinks please",font=("Arial", 16, "bold"))
drinks_label.place(relx=0.5, rely=0.5, anchor='center')
drink_order_var = tk.StringVar()
drinks_options = ["Tea", "Coffee", "Lemon tea"]
drinks_dropdown = tk.OptionMenu(window, drink_order_var, *drinks_options)
drinks_dropdown.place(relx=0.50, rely=0.54, anchor='center')
drinks_status_label = tk.Label(window,text="", wraplength=400)
drinks_status_label.place(relx=0.5, rely=0.8, anchor="center")
# logical statement
def submit_drink_order():
    drink_order = drink_order_var.get()
    if drink_order == "Coffee":
        drinks_status_label.config(text="Thank you your order is placed...Total amount payable is 12 dollar",font=("Didot", 12 ),bg=None)
    elif drink_order == "Tea":
        drinks_status_label.config(text="Thank you your order is placed...Total amount payable is 10 dollar",font=("Arial", 12 ),bg=None)
    elif drink_order == "Lemon tea":
        drinks_status_label.config(text="Thank you your order is placed...Total amount payable is 10 dollar",font=("Arial", 12),bg=None)
    else:
        drinks_status_label.config(text="The drink is not available here..sorry",font=("Didot", 12),bg=None)

def single_submit():
    submit_order()
    submit_drink_order()
submit_button = tk.Button(window, text="Submit Order", command=single_submit, font=("Times New Roman", 16, "bold"), padx=20, pady=10)
submit_button.place(relx=0.5, rely=0.9, anchor='center')
window.mainloop()
