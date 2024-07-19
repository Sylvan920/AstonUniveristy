# Hangman Game

This is a simple command-line implementation of the classic Hangman game in Python. 

## Installation

First, install the required library:

```bash
pip install random-word
```

## Classes

### WordGenerator

Generates a random word for the game.

- `__init__()`: Initializes the RandomWords instance.
- `get_random_word()`: Returns a random, lowercase alphabetic word.

### Player

Represents a player in the game.

- `__init__(name)`: Initializes the player with a given name.
- `get_guess(guessed_letters)`: Prompts the player to guess a letter, ensuring it's valid and not already guessed.

### Scoreboard

Keeps track of the player's wins and losses.

- `__init__()`: Initializes wins and losses to zero.
- `record(outcome)`: Updates the scoreboard based on the game outcome.

### Hangman

The main game logic.

- `__init__()`: Sets up the game, including generating a random word, initializing the player, and setting initial game states.
- `start_game()`: Greets the player.
- `display_hangman()`: Displays the hangman figure based on remaining guesses.
- `play_round()`: Plays a round of Hangman, managing guesses, checking for wins/losses, and updating the scoreboard.
- `make_guess(letter)`: Updates the game state based on the player's guess.
- `format_word_with_guesses()`: Formats and returns the word with correct guesses shown and underscores for remaining letters.

## How to Play

1. Run the script.
2. Enter your name to start the game.
3. Guess letters to uncover the secret word.
4. You have 5 guesses. Each incorrect guess adds a part to the hangman figure.
5. Win by guessing all letters correctly before running out of guesses. Lose by failing to guess the word within the allowed guesses.
6. The game keeps track of your wins and losses.
7. After each round, you can choose to play again or exit.

## Example Usage

To start the game, run:

```python
if __name__ == "__main__":
    game = Hangman()
    
    while True:
        game.play_round()
        play_again = input("Do you want to play again? (type yes to continue/no to exit): ").lower()
        if not play_again:
            break  
        game.secret_word = game.word_generator.get_random_word()
        game.display_word = ["_"] * len(game.secret_word)
        game.remaining_guesses = 5
        game.guessed_letters = set()
```

Enjoy playing Hangman!
