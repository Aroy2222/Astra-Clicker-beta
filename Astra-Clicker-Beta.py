import tkinter as tk #library

score = 0 #score variable
click_power = 1 #click power variable
price = 30 #price variable
#mainclick function
def click():
    global score
    score += click_power
    label.config(text=f"Score: {score}")
#upgrade click power function
def upgrade_click():
    global click_power, price, score #added score to global to modify it
    if score >= price:
        score -= price
        click_power += 1
        price *= 2 #double the price for next upgrade
        label.config(text=f"Score: {score}") #update label to show new score
        button2.config(text=f"Increase Click Power (Power: {click_power})(Price: {price})") #update button text to show new click power and price
def togglefullscreen():
    window.attributes("-fullscreen", True)
    window.bind("<F11>", exit_fullscreen)
def exit_fullscreen(event):
    window.attributes("-fullscreen", False)
window = tk.Tk()
window.title("program")#title
window.geometry("400x400")#Window size

window.configure(bg="gray")#background color

label = tk.Label(window, text="Welcome to the game!", font=("Arial", 16), fg="white", bg="gray") #white text on gray background
label.pack(pady=100)#the label

button = tk.Button(window, text="click", command=click, font=("Arial", 14), fg="white", bg="gray") #white text on gray background
button.pack(pady=10)#main button

button2 = tk.Button(window, text=f"Increase Click Power (Price: {price})", command=upgrade_click, font=("Arial", 14), fg="white", bg="gray") #white text on gray background
button2.pack(pady=10)#increase click power 
fullscreen_button = tk.Button(window, text="Fullscreen", command=togglefullscreen, font=("Arial", 14), fg="white", bg="gray") #white text on gray background
fullscreen_button.pack(pady=10)#fullscreen button

window.mainloop() #window loop
