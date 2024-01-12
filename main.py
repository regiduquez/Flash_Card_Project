BACKGROUND_COLOR = "#B1DDC6"
import tkinter as tk


window = tk.Tk()
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
my_image = tk.PhotoImage(file="images/card_front.png")
canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR,highlightthickness=0)
canvas.create_image(400,260, image=my_image)
canvas.grid(row=0,column=0, columnspan=2)


#LABEL

language_label = tk.Label(text="French", font=("Ariel", 40, "italic"),background="white")
language_label.place(x=400, y=150, anchor="center")

word_label = tk.Label(text="trouve", font=("Ariel", 60, "bold"), background="white")
word_label.place(x=400, y=263, anchor="center")



# BUTTONS
wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0,border=0.0,activebackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)


right_img = tk.PhotoImage(file="images/right.png",)
right_button = tk.Button(image=right_img, highlightthickness=0,border=0.0,activebackground=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)












window.mainloop()

