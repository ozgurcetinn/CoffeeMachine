import tkinter as tk
from tkinter import messagebox

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def report():
    report_text = (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${money}"
    )
    messagebox.showinfo("Report", report_text)

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            messagebox.showwarning("Resource Error", f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    try:
        quarters = int(quarters_entry.get()) * 0.25
        dimes = int(dimes_entry.get()) * 0.10
        nickels = int(nickles_entry.get()) * 0.05
        pennies = int(pennies_entry.get()) * 0.01
        return quarters + dimes + nickels + pennies
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for coins.")
        return 0

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global money
        change = round(money_received - drink_cost, 2)
        messagebox.showinfo("Transaction", f"Here is ${change} in change.")
        money += drink_cost
        money_label.config(text=f"Money Earned: ${money}")
        return True
    else:
        messagebox.showwarning("Transaction Error", "Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    messagebox.showinfo("Enjoy", f"Here is your {drink_name}. Enjoy!")
    clear_coin_entries()

def clear_coin_entries():
    quarters_entry.delete(0, tk.END)
    dimes_entry.delete(0, tk.END)
    nickles_entry.delete(0, tk.END)
    pennies_entry.delete(0, tk.END)

def order_drink(drink_name):
    drink = MENU[drink_name]
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        if is_transaction_successful(payment, drink["cost"]):
            make_coffee(drink_name, drink["ingredients"])

# GUI Setup
root = tk.Tk()
root.title("Coffee Machine")
root.geometry("400x400")

# Labels and Buttons
tk.Label(root, text="Select a drink:", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=3, pady=10)

tk.Button(root, text="Espresso", command=lambda: order_drink("espresso"), font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
tk.Button(root, text="Latte", command=lambda: order_drink("latte"), font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Cappuccino", command=lambda: order_drink("cappuccino"), font=("Helvetica", 12)).grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="Insert coins:", font=("Helvetica", 14)).grid(row=2, column=0, columnspan=3, pady=10)

tk.Label(root, text="Quarters:", font=("Helvetica", 12)).grid(row=3, column=0, padx=5, pady=5)
quarters_entry = tk.Entry(root, font=("Helvetica", 12))
quarters_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Dimes:", font=("Helvetica", 12)).grid(row=4, column=0, padx=5, pady=5)
dimes_entry = tk.Entry(root, font=("Helvetica", 12))
dimes_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Nickles:", font=("Helvetica", 12)).grid(row=5, column=0, padx=5, pady=5)
nickles_entry = tk.Entry(root, font=("Helvetica", 12))
nickles_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Pennies:", font=("Helvetica", 12)).grid(row=6, column=0, padx=5, pady=5)
pennies_entry = tk.Entry(root, font=("Helvetica", 12))
pennies_entry.grid(row=6, column=1, padx=5, pady=5)

money_label = tk.Label(root, text=f"Money Earned: ${money}", font=("Helvetica", 14))
money_label.grid(row=7, column=0, columnspan=3, pady=10)

tk.Button(root, text="Report", command=report, font=("Helvetica", 12)).grid(row=8, column=0, columnspan=2, pady=10)
tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12)).grid(row=8, column=2, columnspan=2, pady=10)

root.mainloop()
