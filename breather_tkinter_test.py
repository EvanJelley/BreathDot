#### This was an attempt at begining using the tkinter library. After doing a bit of research I determined it was a better use of my time to use the PySide6 library. ####

import tkinter as tk

# Create window
window = tk.Tk()

# Create greeting
greeting = tk.Label(
    text="Let's do some breathing :)",
    font=("Times New Roman", 20),
    fg="#E7D7C6",
    bg="#082D48",
    width=40,
    height=8,
)

# Create a button with an on-click event function
def startOnClick(event):
    inTime = breath_in.get()
    outTime = breath_out.get()
    print(f"Breath in time: {inTime}, Breath out time: {outTime}")

def quit(event):
    window.destroy()

startButton = tk.Label(
    window,
    text="Start",
    font=("Times New Roman", 20),
    width=40,
    height=5,
    fg="#E7D7C6",
    bg="#082D48",
)

quitButton = tk.Label(
    window,
    text="Quit",
    font=("Times New Roman", 10),
    width=40,
    height=2,
    fg="#E7D7C6",
    bg="#082D48",
)

quitButton.bind("<Button-1>", quit)

startButton.bind("<Button-1>", startOnClick)

# Get the breath in and breath out desired times
breath_in_label = tk.Label(
    text="How many seconds do you want to breath in?",
    font=("Times New Roman", 20),
    fg="#E7D7C6",
    bg="#082D48",
    height=5,
    width=40,
)
breath_in = tk.Entry()

breath_out_label = tk.Label(
    text="How many seconds do you want to breath out?",
    font=("Times New Roman", 20),
    fg="#E7D7C6",
    bg="#082D48",
    height=5,
    width=40,
)
breath_out = tk.Entry()

# Pack the widgets
greeting.pack()
breath_in_label.pack()
breath_in.pack()
breath_out_label.pack()
breath_out.pack()
startButton.pack()
quitButton.pack()

# Configure window
window.configure(bg="#082D48")

# Run the application
window.mainloop()


