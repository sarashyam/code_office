import tkinter as tk
import subprocess
import pywhatkit
import pandas as pd
from datetime import datetime



def run_code():
    df = pd.read_csv("C:\\Users\\user105\Desktop\\SAS_training\\birthday_data.xlsx")
    today = datetime.today().date()
    #tk.Label(text="enter filename ").pack()
#     # Execute your Python code here
#     subprocess.call(["python", "C:\\Users\\user105\\Downloads\\vba learning\\see.py"])

# Create the main window
window = tk.Tk()
window.geometry("100x100")

# Create a button
button = tk.Button(window, text="Run Code", command=run_code)
button.pack()

# Start the main event loop
window.mainloop()


