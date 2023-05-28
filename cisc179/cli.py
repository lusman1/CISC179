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
    game = Game(getRandomWordFromFile("words_list.txt"))
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

    wrong_guesses.config(text="Wrong guesses: " + game.get_wrong_guesses())
    lives.config(text="Lives remaining: " + str(game.get_lives()))
    fill_in_blanks.config(text=game.get_fill_in_blanks())
    if game.has_won():
        error_message.config(text="You Won!!!")
        game_ended = True
    if game.has_lost():
        error_message.config(text="You Lost!!!")
        game_ended = True


window = Tk()
window.geometry("800x300")
window.title("Hang Man")
canvas = Canvas(window, bg='gray')
game_ended = False
game = Game(getRandomWordFromFile("words_list.txt"))

user_input = Text(window, width=20, height=5)
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

wrong_guesses = Label(window, text="Wrong guesses: "+game.get_wrong_guesses())
wrong_guesses.pack()

error_message = Label(window, text="")
error_message.pack()

window.mainloop()
