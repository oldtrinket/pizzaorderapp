import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class OldHenryPizzaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Old Henry Pizza")
        self.geometry("500x800")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Top Frame (35%)
        top_frame = tk.Frame(self, height=int(0.35*self.winfo_screenheight()), bg="white")
        top_frame.pack(fill=tk.BOTH, expand=True)
        
        welcome_label = tk.Label(top_frame, text="Welcome to Old Henry Pizza", font=("Arial", 24, "bold"), fg="blue", bg="white")
        welcome_label.pack(pady=20)
        
        # Middle Frame (50%)
        middle_frame = tk.Frame(self, height=int(0.5*self.winfo_screenheight()), bg="white")
        middle_frame.pack(fill=tk.BOTH, expand=True)
        
        img = Image.open("pizza.png")  # Replace "pizza.jpg" with the filename of your image
        pizza_image = ImageTk.PhotoImage(img)
        pizza_label = tk.Label(middle_frame, image=pizza_image, bg="white")
        pizza_label.image = pizza_image  # Keep a reference to the image to avoid garbage collection
        pizza_label.pack()
        
        # Bottom Frame (15%)
        bottom_frame = tk.Frame(self, height=int(0.15*self.winfo_screenheight()), bg="white")
        bottom_frame.pack(fill=tk.BOTH, expand=True)
        
        register_button = ttk.Button(bottom_frame, text="Register", command=self.register)  # Add the registration functionality
        register_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        login_button = ttk.Button(bottom_frame, text="Login", command=self.login)  # Add the login functionality
        login_button.pack(side=tk.RIGHT, padx=20, pady=20)
        
        instructions_label = tk.Label(bottom_frame, text="New customers, please register. Returning customers, please login.", bg="white")
        instructions_label.pack(pady=10)
    
    def register(self):
        # Add the registration functionality here
        pass
    
    def login(self):
        # Add the login functionality here
        pass

if __name__ == "__main__":
    app = OldHenryPizzaApp()
    app.mainloop()


