from cisc179.base import NAME

from _pytest.python_api import raises

from cisc179.game import Game


def testGameWin():
    game = Game("ses")
    assert game.get_lives() == 6
    assert game.get_fill_in_blanks() == "_ _ _"
    assert game.get_wrong_guesses() == ""
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("s")
    assert game.get_lives() == 6
    assert game.get_fill_in_blanks() == "s _ s"
    assert game.get_wrong_guesses() == ""
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("e")
    assert game.get_lives() == 6
    assert game.get_fill_in_blanks() == "s e s"
    assert game.get_wrong_guesses() == ""
    assert game.has_won() == True
    assert game.has_lost() == False


def testGameLose():
    game = Game("se")
    assert game.get_lives() == 6
    assert game.get_fill_in_blanks() == "_ _"
    assert game.get_wrong_guesses() == ""
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("s")
    assert game.get_lives() == 6
    assert game.get_fill_in_blanks() == "s _"
    assert game.get_wrong_guesses() == ""
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("a")
    assert game.get_lives() == 5
    assert game.get_fill_in_blanks() == "s _"
    assert game.get_wrong_guesses() == "a"
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("b")
    assert game.get_lives() == 4
    assert game.get_fill_in_blanks() == "s _"
    assert game.get_wrong_guesses() == "a b"
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("c")
    assert game.get_lives() == 3
    assert game.get_fill_in_blanks() == "s _"
    assert game.get_wrong_guesses() == "a b c"
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("d")
    assert game.get_lives() == 2
    assert game.get_fill_in_blanks() == "s _"
    assert game.get_wrong_guesses() == "a b c d"
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("f")
    assert game.get_lives() == 1
    assert game.get_fill_in_blanks() == "s _"
    assert game.get_wrong_guesses() == "a b c d f"
    assert game.has_won() == False
    assert game.has_lost() == False

    game.process_input("g")
    assert game.get_lives() == 0
    assert game.get_fill_in_blanks() == "s _"
    assert game.get_wrong_guesses() == "a b c d f g"
    assert game.has_won() == False
    assert game.has_lost() == True


def testGameException():
    game = Game("se")
    game.process_input("s")
    with raises(ValueError, match = "Letter is already guessed!"):
        game.process_input("s")

    game.process_input("g")
    with raises(ValueError, match = "Letter is already guessed!"):
        game.process_input("g")

    with raises(ValueError, match="Please enter a single alphabet letter!"):
        game.process_input("1")

    with raises(ValueError, match="Please enter a single alphabet letter!"):
        game.process_input("ee")
