
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

from tkinter import *

window = Tk()
window.title("Nazif's Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file ="tomato.png")

canvas= Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
canvas.create_image(100,112, image = tomato_img)
canvas.create_text(100, 130, text=f'00:00', font=(FONT_NAME, 35, "bold"), fill = "white")
canvas.pack()

start_button = Button(text="start")
start_button.pack(side="left")
reset_button = Button(text="reset")
reset_button.pack(side="right")

window.mainloop()