import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cisc179.game import Game


def getRandomWordFromFile(file_name):
    try:
        with open(file_name, 'r') as file:
            words_list = file.read().splitlines()
            return random.choice(words_list)
    except:
        # unable to open file
        return "word"


def on_restart_button():
    global game
    global game_ended
    global hangman_canvas

    game = Game(getRandomWordFromFile("words_list.txt"))
    # Clear the canvas
    hangman_canvas.delete("all")
    initialize_hangman()
    error_message.config(text="")
    wrong_guesses.config(text="Wrong guesses: " + game.get_wrong_guesses())
    lives.config(text="Lives remaining: " + str(game.get_lives()))
    fill_in_blanks.config(text=game.get_fill_in_blanks())
    game_ended = False


def on_submit_button():
    global game
    global game_ended
    if game_ended:
        return
    try:
        error_message.config(text="")
        game.process_input(user_input.get(1.0, "end-1c"))
    except ValueError as e:
        error_message.config(text=str(e))

    draw_hangman()
    wrong_guesses.config(text="Wrong guesses: " + game.get_wrong_guesses())
    lives.config(text="Lives remaining: " + str(game.get_lives()))
    fill_in_blanks.config(text=game.get_fill_in_blanks())
    if game.has_won():
        messagebox.showinfo("You won!", "You won! Amazing!")
        game_ended = True
    if game.has_lost():
        messagebox.showinfo("You Lost!", "You Lost! \n Your word was: " + game.word_to_guess)
        # error_message.config(text="You Lost!!!")
        game_ended = True


def initialize_hangman():
    global hangman_canvas
    # Draw the Hangman's scaffold
    hangman_canvas.create_line(20, 250, 180, 250)
    hangman_canvas.create_line(100, 250, 100, 50)
    hangman_canvas.create_line(100, 50, 200, 50)
    hangman_canvas.create_line(200, 50, 200, 80)
    # Update the canvas
    hangman_canvas.pack()


def draw_hangman():
    global hangman_canvas
    if game.get_lives() == 5:
        # Draw the head
        hangman_canvas.create_oval(180, 80, 220, 120)

    if game.get_lives() == 4:
        # Draw the body
        hangman_canvas.create_line(200, 120, 200, 200)

    if game.get_lives() == 3:
        # Draw the left arm
        hangman_canvas.create_line(200, 140, 160, 160)

    if game.get_lives() == 2:
        # Draw the right arm
        hangman_canvas.create_line(200, 140, 240, 160)

    if game.get_lives() == 1:
        # Draw the left leg
        hangman_canvas.create_line(200, 200, 180, 240)

    if game.get_lives() == 0:
        # Draw the right leg
        hangman_canvas.create_line(200, 200, 220, 240)

    # Update the canvas
    hangman_canvas.pack()


window = Tk()
window.geometry("800x550")
window.title("HangMan")
canvas = Canvas(window, bg='blue')

game_ended = False
game = Game(getRandomWordFromFile("words_list.txt"))

user_input = Text(window, width=10, height=5)
user_input.insert(END, "type here")
user_input.pack()

submit = ttk.Button(window, text="Submit", command=on_submit_button)
submit.pack()

restart = ttk.Button(window, text="Restart", command=on_restart_button)
restart.pack()

fill_in_blanks = Label(window, text=game.get_fill_in_blanks())
fill_in_blanks.pack()

lives = Label(window, text="Lives remaining: " + str(game.get_lives()))
lives.pack()

wrong_guesses = Label(window, text="Wrong guesses: " + game.get_wrong_guesses())
wrong_guesses.pack()

error_message = Label(window, text="")
error_message.pack()

hangman_canvas = Canvas(window, width=400, height=400)
initialize_hangman()

window.mainloop()
