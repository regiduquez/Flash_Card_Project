import tkinter as tk
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
my_image = tk.PhotoImage(file="images/card_front.png")
canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 260, image=my_image)
canvas.grid(row=0, column=0, columnspan=2)

# ..........................................WORD GENERATOR............................................

french_raw_df = pandas.read_csv("data/french_words.csv")
french_english_dict = french_raw_df.to_dict(orient="records")
# print(french_english_dict[0]['French'])


def generate_word():
    random_num = random.randint(0, 101)
    french_word = french_english_dict[random_num]['French']
    english_word = french_english_dict[random_num]['English']
    word_label.config(text=french_word)
    print(english_word)


# LABEL

language_label = tk.Label(text="French", font=("Ariel", 40, "italic"), background="white")
language_label.place(x=400, y=150, anchor="center")

word_label = tk.Label(text="bonjour", font=("Ariel", 60, "bold"), background="white")
word_label.place(x=400, y=263, anchor="center")


# BUTTONS
wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, border=0.0,
                         activebackground=BACKGROUND_COLOR, command=generate_word)
wrong_button.grid(column=0, row=1)


right_img = tk.PhotoImage(file="images/right.png",)
right_button = tk.Button(image=right_img, highlightthickness=0, border=0.0,
                         activebackground=BACKGROUND_COLOR, command=generate_word)
right_button.grid(column=1, row=1)


window.mainloop()
