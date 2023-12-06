import tkinter as tk
from tkinter import *

root = Tk()
root.title("Гриль №2")
root.geometry("600x400")

class ShaurmaOrder:
    def __init__(self, sauce, shaurma_type, price, payment, ready_time):
        self.sauce = sauce
        self.shaurma_type = shaurma_type
        self.price = price
        self.payment = payment
        self.ready_time = ready_time

sauces = {
    "Ketchup": 1.25, "Cheesy": 0.99, "Spicy": 0.50
}

shaurma_types = {
    "Spicy": 4.25, "Meat": 4.50, "Mix": 4.00
}

total_price = 0.00

def calculate_price():
    global total_price
    total_price = sauces[sauce_var.get()] + shaurma_types[type_var.get()]
    price_label.config(text=f"Total Price: ${total_price:.2f}")
    root.after(6000, show_order_ready)  # Добавляем задержку в 6000 миллисекунд (6 секунд)

def show_order_ready():
    order_ready_label = tk.Label(root, text="Your Shaurma is Ready!", fg="green", font=("Arial", 16, "bold"))
    order_ready_label.pack()

    if payment_var.get() == "Card":
        payment_info = tk.Label(root, text="Thank you for your purchase. Payment has been processed.", font=("Arial", 12))
        payment_info.pack()
    else:
        payment_option = tk.Label(root, text="Please pay with cash", font=("Arial", 12))
        payment_option.pack()

def place_order():
    order = ShaurmaOrder(sauce_var.get(), type_var.get(), total_price, payment_var.get(), ready_time_var.get())
    print(f"Order placed - Shaurma with {order.sauce} sauce and {order.shaurma_type} type for ${order.price:.2f} paying by {order.payment}. Ready in {order.ready_time} seconds")

sauce_label = tk.Label(root, text="Choose your sauce:", font=("Arial", 12))
sauce_label.pack()
sauce_var = tk.StringVar()
for sauce in sauces:
    tk.Radiobutton(root, text=sauce, variable=sauce_var, value=sauce).pack()

type_label = tk.Label(root, text="Choose your shaurma type:", font=("Arial", 12))
type_label.pack()
type_var = tk.StringVar()
for shaurma_type in shaurma_types:
    tk.Radiobutton(root, text=shaurma_type, variable=type_var, value=shaurma_type).pack()

payment_label = tk.Label(root, text="Select payment method:", font=("Arial", 12))
payment_label.pack()
payment_var = tk.StringVar()
payment_var.set("Cash")
payment_menu = tk.OptionMenu(root, payment_var, "Cash", "Card")
payment_menu.pack()

calculate_button = tk.Button(root, text="Calculate Price", command=calculate_price, bg="orange", fg="white", font=("Arial", 12))
calculate_button.pack()

place_order_button = tk.Button(root, text="Place Order", command=place_order, bg="blue", fg="white", font=("Arial", 12))
place_order_button.pack()

price_label = tk.Label(root, text="Total Price: $0.00", font=("Arial", 12))
price_label.pack()

root.mainloop()