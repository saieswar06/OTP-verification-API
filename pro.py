import twilio.rest
import random
import tkinter as tk
from tkinter import messagebox

# Creating Window
root = tk.Tk()
root.title("OTP Verification")
root.geometry("600x550")

# Twilio account details
account_sid = "AC4b7e709104b8c5b5046f031f298d3abb"
auth_token = "245cbef2ea13ba07219616c625319ba3"

# Global variable to store OTP
n = None

# resend the OTP
def resendOTP():
    global n
    n = random.randint(1000, 9999)
    client = twilio.rest.Client(account_sid, auth_token)
    client.messages.create(to="+919492925732", from_="+15417228624", body=f"Your OTP is {n}")

# Checking the OTP
def checkOTP():
    global n
    try:
        user_input = int(user.get("1.0", "end-1c"))
        if user_input == n:
            messagebox.showinfo("Info", "Login Success")
            n = "done"
        elif n == "done":
            messagebox.showinfo("Info", "Already entered")
        else:
            messagebox.showinfo("Info", "Wrong OTP")
    except ValueError:
        messagebox.showinfo("Info", "Invalid OTP")

# Drawing the canvas
c = tk.Canvas(root, bg="white", width=400, height=300)
c.place(x=100, y=60)

# Label widget
login = tk.Label(root, text="OTP Verification", font=("bold", 20), bg="white")
login.place(x=210, y=90)

# Entry widget
user = tk.Text(root, borderwidth=2, wrap="word", width=29, height=2)
user.place(x=190, y=160)

# Sending the OTP
resendOTP()

# Submit button
submit_button = tk.Button(root, text="Submit", command=checkOTP, font=('bold', 15))
submit_button.place(x=258, y=250)

# Resend Button
resend_button = tk.Button(root, text="Resend OTP", command=resendOTP, font=("bold", 15))
resend_button.place(x=240, y=400)

# Event Loop
root.mainloop()
