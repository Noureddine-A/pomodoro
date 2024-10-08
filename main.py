import datetime
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
repetition = 1
work_reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    global repetition
    global work_reps

    repetition = 1
    work_reps = 0

    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")


def start_timer():
    global repetition

    if repetition % 8 == 0:
        count_down(LONG_BREAK_MIN * 60, "break")
        label.config(text="Break", fg=RED)
    elif repetition % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60, "break")
        label.config(text="Break", fg=PINK)
    elif repetition % 2 != 0:
        count_down(WORK_MIN * 60, "work")
        label.config(text="Work", fg=GREEN)

    repetition += 1


def count_down(count, mode):
    converted_time = str(datetime.timedelta(seconds=count))

    canvas.itemconfig(timer_text, text=converted_time[2:])
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, mode)
    else:
        if mode == "work":
            global work_reps
            work_reps += 1

            checkmark_text = ""

            for i in range(work_reps):
                checkmark_text = checkmark_text + "✓"

            check_mark.config(text=checkmark_text)
        start_timer()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=2, row=1)

label = Label(fg=GREEN, font=(FONT_NAME, 36), text="Timer", bg=YELLOW)
label.grid(column=2, row=0)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(column=2, row=3)

window.mainloop()
