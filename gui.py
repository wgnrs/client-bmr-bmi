import tkinter as tk
from client import Client
from formulas import *


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        """" Initialize the graphic user interface"""
        super().__init__(master)
        self.master = master
        self.master.title("calculator of bmi and bmr")
        # We used pack() to pack the widgets in the window
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.age_label = tk.Label(self, text="Your age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        self.height_label = tk.Label(self, text="Your height (cm):")
        self.height_label.pack()
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        self.weight_label = tk.Label(self, text="Your weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        self.sex_label = tk.Label(self, text="Your sex (M/F):")
        self.sex_label.pack()
        self.sex_entry = tk.Entry(self)
        self.sex_entry.pack()

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def calculate(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        height = int(self.height_entry.get())
        weight = int(self.weight_entry.get())
        sex = self.sex_entry.get()

        client = Client(name, age, height, weight, sex)

        bmi = calculate_bmi(client)
        bmr = calculate_bmr(client)

        result_text = f"BMI: {bmi:.2f}\nBMR: {bmr:.2f} calories per day"
        self.result_label.config(text=result_text)


root = tk.Tk()
app = MainWindow(master=root)
# The function mainloop() keeps the gui in execution and watch the events from the user
app.mainloop()
