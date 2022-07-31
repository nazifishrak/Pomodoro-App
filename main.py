
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
reps = 0
from math import floor
from tkinter import *

# ------------------------Timer--------------------------
def start_counter():
    global reps
    reps+=1
    # if reps 1,3,5... then its work time
    if  reps%2!=0:
        timer_Label.config(text="WORK")
        count_down(WORK_MIN*60)
    elif reps%8==0:
        timer_Label.config(text="LONG BREAK",font=("Century Gothic", 30, "bold"))
        count_down(LONG_BREAK_MIN*60)
    else:
        timer_Label.config(text="SHORT BREAK", font=("Century Gothic", 30, "bold"))
        count_down(SHORT_BREAK_MIN*60)
    
def count_down(count):
    count_min = floor(count/60)
    count_sec = int(count%60)
    if count_sec <=9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    if count>0:
        window.after(2, lambda : count_down(count-1))
    else:
        start_counter()

def reset():
    global reps
    reps =0
    start_counter()






# -----------------------UI------------------------------------------
window = Tk()
window.title("Nazif's Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer_Label = Label(text="Timer", fg=GREEN, font=("Century Gothic", 40, "bold"), bg=YELLOW)
timer_Label.grid(row=0, column=1)
tomato_img = PhotoImage(file ="tomato.png")


canvas= Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
canvas.create_image(100,100, image = tomato_img)
timer_text=canvas.create_text(100, 130, text=f'00:00', font=(FONT_NAME, 35, "bold"), fill = "white")
canvas.grid(row=1,column=1)



start_button = Button(text="START", fg="white", bg=PURPLE, highlightthickness=0,width=10,height=2, font=(FONT_NAME,10,"bold"), command=start_counter)
start_button.grid(row=2, column=0)
reset_button = Button(text="RESET", fg="white", bg=PURPLE, highlightthickness=0,width=10,height=2, font=(FONT_NAME,10,"bold"),command=reset)
reset_button.grid(row=2, column=2)
check_mark = Label(text="✔️",fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 18, "bold"))
check_mark.grid(row=3, column=1)
window.mainloop()