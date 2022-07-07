from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")


def new_french_word():
    french_word = random.choice(words)["French"]
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(canvas_word, text=french_word)


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 283, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
# canvas.create_text(400, 283, text="trouve", font=("Ariel", 60, "bold"))


check_img = PhotoImage(file="images/right.png")
correct_button = Button(image=check_img, highlightthickness=0, command=new_french_word)
correct_button.grid(row=1, column=1)

cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=new_french_word)
wrong_button.grid(row=1, column=0)

window.mainloop()