from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
french_dict = {}

try:
    french_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    french_dict = original_data.to_dict(orient="records")
else:
    french_dict = french_df.to_dict(orient='records')




def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    french_dict.remove(current_card)
    data = pd.DataFrame(french_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command= next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, borderwidth=0, command = is_known)
known_button.grid(row=1, column=1)



#You'll need to use pandas to access the CSV file and generate a data frame.
# To get all the words/translation rows out as a list of dictionaries e.g.
# [{french_word: english_word}, {french_word2: english_word2},
# {french_word3: english_word3}]

# DataFrame.to_dict(orient="records")

next_card()

window.mainloop()