from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
list_index = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

words = data.to_dict(orient="records")
print(words)


def new_french_word():
    global list_index, flip_timer
    window.after_cancel(flip_timer)
    list_index = random.choice(words)
    french_word = list_index["French"]
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(canvas_title, text="French", fill="#000000")
    canvas.itemconfig(canvas_word, text=french_word, fill="#000000")
    flip_timer = window.after(3000, change_card_side)


def change_card_side():
    global list_index
    canvas.itemconfig(canvas_img, image=card_back_img)
    english_word = list_index["English"]
    canvas.itemconfig(canvas_title, text="English", fill="#ffffff")
    canvas.itemconfig(canvas_word, text=english_word, fill="#ffffff")


def remove_card():
    global list_index
    words.remove(list_index)
    print(len(words))
    df = pandas.DataFrame(words)
    df.to_csv("data/words_to_learn.csv", index=False)
    new_french_word()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 283, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

flip_timer = window.after(3000, change_card_side)


check_img = PhotoImage(file="images/right.png")
correct_button = Button(image=check_img, highlightthickness=0, command=remove_card)
correct_button.grid(row=1, column=1)

cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=new_french_word)
wrong_button.grid(row=1, column=0)

new_french_word()

window.mainloop()
