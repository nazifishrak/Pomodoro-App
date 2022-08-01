
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
counter =1
cycle =0
timer = None
state = False #For sticky mode
from math import floor
from tkinter import *
from playsound import playsound  # use version 1.2.2 otherwise doesnt work


# Plays sound
def playsound_command():
    playsound('./mixkit-correct-answer-tone-2870.wav')
# ------------------------Timer--------------------------
def start_counter():
    global reps
    reps+=1
    # if reps 1,3,5... then its work time
    if  reps%2!=0:
        timer_Label.config(text="WORK",font=("Century Gothic", 40, "bold"), fg=GREEN)
        # window.attributes("-topmost", True)
        count_down(WORK_MIN*60)
    elif reps%8==0:
        timer_Label.config(text="BREAK",font=("Century Gothic", 40, "bold"), fg= RED)
        count_down(LONG_BREAK_MIN*60)
        global cycle
        cycle+=1
        window.title(f"Nazif's Pomodoro Cycles Completed {cycle}")
    else:
        timer_Label.config(text="BREAK", font=("Century Gothic", 40, "bold"), fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    
def count_down(count):
    count_min = floor(count/60)
    count_sec = int(count%60)
    if count_sec <=9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, lambda : count_down(count-1))
    else:
        start_counter()
        if reps %2 ==0:
            global counter
            ticks ="✔️"
            ticks =counter*"✔️"
            check_mark.config(text=f"{ticks} ")
            playsound_command()
            counter+=1
            if counter>=4:
                counter =0

def reset():

    window.after_cancel(timer)
    global cycle, reps, counter
    reps = 0
    counter =1
    cycle =0
    canvas.itemconfig(timer_text, text=f"00: 00")
    window.title(f"Nazif's Pomodoro Cycles Completed {cycle}")
    timer_Label.config(text="Timer")
    check_mark.config(text="")

    
    

def sticky():
    global state
    if state == False:
        window.attributes("-topmost", True)
        state = True
    else:
        window.attributes("-topmost", False)
        state = False




# -----------------------UI------------------------------------------
window = Tk()
window.title(f"Nazif's Pomodoro Cycles Completed {cycle}")
window.config(padx=20, pady=20, bg=YELLOW)
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
check_mark = Label(text="",fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 18, "bold"))
check_mark.grid(row=4, column=1)


sticky_button = Button(text="STICK", fg="white", bg=PURPLE, highlightthickness=0,width=10,height=2, font=(FONT_NAME,10,"bold"),command=sticky)
sticky_button.grid(row=2, column=1)
window.mainloop()