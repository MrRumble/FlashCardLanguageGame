from tkinter import *
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"


try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    df_dict = df.to_dict(orient="records")
else:
    df_dict = df.to_dict(orient="records")



# ---------------------------- BUTTON METHODS ------------------------------- #

def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = r.choice(df_dict)
    french = random_word.get('French')
    canvas.itemconfig(current_image, image=card_front)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(french_word, text=french)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    english = random_word.get("English")
    canvas.itemconfig(current_image, image=card_back) 
    canvas.itemconfig(card_title, text = 'English')
    canvas.itemconfig(french_word, text = english)

def correct_card():
    df_dict.remove(random_word)
    next_card()

def end_of_game():
    words_to_learn = pd.DataFrame(df_dict)
    words_to_learn.to_csv('data/words_to_learn.csv', index = False)
        
        

    #If the user presses YES, we remove the row from the french_rows
# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR)
current_image = canvas.create_image(400, 263, image=card_front)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
french_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_button = Button(image=wrong_image,highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, command=correct_card)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
end_of_game()