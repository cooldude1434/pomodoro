import math
from tkinter import *




# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.09
SHORT_BREAK_MIN = 0.09
LONG_BREAK_MIN = 0.09
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label_heading.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_tick.config(text=" ")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)

    if reps % 8 == 0:
        count_down(60 * SHORT_BREAK_MIN)
        label_heading.config(text="Long Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(60 * LONG_BREAK_MIN)
        label_heading.config(text="Break",fg=RED)
    else:
        count_down(60 * WORK_MIN)
        label_heading.config(text="Focus", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    print(count_min, count_sec)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"

        label_tick.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro by Sudarsan Bala")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_heading = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label_heading.grid(column=1, row=0)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0,command = reset_timer)
button_reset.grid(column=2, row=2)

label_tick = Label(fg=GREEN, bg=YELLOW)
label_tick.grid(column=1, row=3)

window.mainloop()
