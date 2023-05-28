
import random
class Game:
    def __init__(self, word_to_guess):
        self.lives_remaining = 6
        self.word_to_guess = word_to_guess # self.word_list = word_list from another file & .get_random_word() from file
        self.wrong_guesses = []
        self.fill_in_blank = ["_"] * len(self.word_to_guess)

    def get_lives(self):
        return self.lives_remaining
        # print("Number of lives left:", self.lives_remaining)

    def get_fill_in_blanks(self):
        return " ".join(self.fill_in_blank)
        # print(" ".join(self.fill_in_blank))

    def get_wrong_guesses(self):
        return " ".join(self.wrong_guesses)
        # print("wrong tries:", self.wrong_guesses)

    def process_input(self, input_char):
        if self.has_won() or self.has_lost():
            return
        # validation for more than one word or alphabet
        if len(input_char) != 1 or not input_char.isalpha():
            raise ValueError("Please enter a single alphabet letter!")

        # validation for repeated letter
        if input_char in self.wrong_guesses:
            raise ValueError("Letter is already guessed!")

        if input_char in self.fill_in_blank:
            raise ValueError("Letter is already guessed!")

        # validation for wrong guesses
        if input_char not in self.word_to_guess:
            self.wrong_guesses.append(input_char)
            self.lives_remaining -= 1
            return

        for indx, char in enumerate(self.word_to_guess):
            if input_char == char:
                self.fill_in_blank[indx] = input_char


    def has_won(self):
        return "_" not in self.fill_in_blank

    def has_lost(self):
        return self.lives_remaining == 0
