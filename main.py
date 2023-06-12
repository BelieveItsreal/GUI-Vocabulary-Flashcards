from tkinter import *   #type: ignore
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_learn = {}
#reading the data file and making it into dictionary
try:
    data = pandas.read_csv("D:\\coding\\python_in_hole\\python code\\flash-card\\data\\to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("D:\\coding\\python_in_hole\\python code\\flash-card\\data\\french_words.csv")
    word_learn = original_data.to_dict(orient="records")
else:
    word_learn = data.to_dict(orient="records")


#changing the card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_learn)
    canvas.itemconfig(canva_text, text="French", fill = "black")
    canvas.itemconfig(canva_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canva_text, text="English", fill = "white")
    canvas.itemconfig(canva_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    word_learn.remove(current_card)
    data = pandas.DataFrame(word_learn)
    data.to_csv("D:\\coding\\python_in_hole\\python code\\flash-card\\data\\to_learn.csv", index=False)
    next_card()

window= Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file="D:\\coding\\python_in_hole\\python code\\flash-card\\images\\card_back.png")
card_front_img = PhotoImage(file="D:\\coding\\python_in_hole\\python code\\flash-card\\images\\card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canva_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

#buttons
cross_image = PhotoImage(file="D:\\coding\\python_in_hole\\python code\\flash-card\\images\\wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

right_image = PhotoImage(file="D:\\coding\\python_in_hole\\python code\\flash-card\\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()