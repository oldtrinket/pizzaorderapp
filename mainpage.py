import tkinter as tk
#from PIL import Image, ImageTk

class PizzaOrderingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Old Henry Pizza")

        # create and display the welcome message
        welcome_label = tk.Label(root, text="Welcome to Old Henry Pizza")
        welcome_label.pack(pady=10)

        # create and display the register button
        register_button = tk.Button(root, text="Register", font=("Arial", 14), bg="white", fg="blue", activebackground="green")
        register_button.pack(pady=10)

        # create and display the login button
        login_button = tk.Button(root, text="Login", font=("Arial", 14), bg="white", fg="blue", activebackground="green")
        login_button.pack(pady=10)

        # create and display the order button
        order_button = tk.Button(root, text="Order a Pizza", font=("Arial", 16), bg="white", fg="blue", activebackground="green", command=self.show_pizza_menu)
        order_button.pack(pady=30)

        # create and display the image holder
        image_holder = tk.Label(root, bg="white", width=400, height=300)
        image_holder.pack(pady=10)

        # create and display the insert image button
        insert_image_button = tk.Button(root, text="Insert Image", font=("Arial", 14), bg="white", fg="blue", activebackground="green")
        insert_image_button.pack(pady=10)

    def show_pizza_menu(self):
        # create a new window for the pizza menu
        pizza_menu_window = tk.Toplevel(self.root)
        pizza_menu_window.title("Pizza Menu")

        # create and display the pizza flavors and descriptions
        classic_label = tk.Label(pizza_menu_window, text="Classic Pizza - Tomato sauce, mozzarella cheese, and pepperoni")
        classic_label.pack(pady=5)

        gourmet_label = tk.Label(pizza_menu_window, text="Gourmet Pizza - Pesto sauce, goat cheese, and sun-dried tomatoes")
        gourmet_label.pack(pady=5)

        vegetarian_label = tk.Label(pizza_menu_window, text="Vegetarian Pizza - Marinara sauce, mushrooms, onions, and green peppers")
        vegetarian_label.pack(pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    app = PizzaOrderingApp(root)
    root.mainloop()
