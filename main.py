
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PURPLE = "#B2A4FF"
FONT_NAME = "Century Gothic"
FONT_NAME2 = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

from tkinter import *

window = Tk()
window.title("Nazif's Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer_Label = Label(text="Timer", fg=GREEN, font=("Century Gothic", 40, "bold"), bg=YELLOW)
timer_Label.grid(row=0, column=1)
tomato_img = PhotoImage(file ="tomato.png")


canvas= Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
canvas.create_image(100,100, image = tomato_img)
canvas.create_text(100, 130, text=f'00:00', font=(FONT_NAME, 35, "bold"), fill = "white")
canvas.grid(row=1,column=1)



start_button = Button(text="START", fg="white", bg=PURPLE, highlightthickness=0,width=10,height=2, font=(FONT_NAME,10,"bold"))
start_button.grid(row=2, column=0)
reset_button = Button(text="RESET", fg="white", bg=PURPLE, highlightthickness=0,width=10,height=2, font=(FONT_NAME,10,"bold"))
reset_button.grid(row=2, column=2)
check_mark = Label(text="✔️",fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 18, "bold"))
check_mark.grid(row=3, column=1)
window.mainloop()