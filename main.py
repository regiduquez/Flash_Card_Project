import tkinter as tk
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

french_raw_df = pandas.read_csv("data/french_words.csv")

try:
    to_learn_df = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    dictionary = french_raw_df.to_dict(orient="records")
else:
    dictionary = to_learn_df.to_dict(orient="records")
current_card = {}

def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary)
    canvas.itemconfig(canvas_language, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=front_card)
    window.after(3000, flip_card)



def flip_card():
    canvas.itemconfig(canvas_img, image=back_card)
    canvas.itemconfig(canvas_language, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")

def update_dict():
    card_index = dictionary.index(current_card)
    dictionary.remove(dictionary[card_index])
    words_to_learn = dictionary
    df_words = pandas.DataFrame(words_to_learn)
    df_words.to_csv("data/words_to_learn.csv", index=False)


def update_generate():
    update_dict()
    generate_word()




window = tk.Tk()
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
front_card = tk.PhotoImage(file="images/card_front.png")
back_card = tk.PhotoImage(file="images/card_back.png")
canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 260, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

# CANVAS TEXT
canvas_language = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

flip_timer = window.after(5000, generate_word)





# BUTTONS
wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, border=0.0,
                         activebackground=BACKGROUND_COLOR, command=generate_word)
wrong_button.grid(column=0, row=1)


right_img = tk.PhotoImage(file="images/right.png",)
right_button = tk.Button(image=right_img, highlightthickness=0, border=0.0,
                         activebackground=BACKGROUND_COLOR, command=update_generate,)
right_button.grid(column=1, row=1)


window.mainloop()
