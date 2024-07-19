from random_word import RandomWords
# Import the required library, using "pip install random-word"
pip install random-word

class WordGenerator:
    def __init__(self):
        self.random_words = RandomWords()

    def get_random_word(self):
        word = self.random_words.get_random_word().lower()
        if not word.isalpha():
            return self.get_random_word() # Recurse if the word is not alphabetic
        return word

class Player:

    def __init__(self, name):
        self.name = name


    def get_guess(self, guessed_letters):
        while True:
            guess = input(f"{self.name}, guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
                return guess
            print("Invalid guess. Please enter a single letter you have not guessed yet.")


class Scoreboard:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def record(self, outcome):
        if outcome == "win":
            self.wins += 1
        elif outcome == "lose":
            self.losses += 1    

class Hangman:
    def __init__(self):
        self.word_generator = WordGenerator()
        self.secret_word = self.word_generator.get_random_word()
        self.player_name = input("Enter your name to start the game: ")
        self.player = Player(self.player_name)
        self.scoreboard = Scoreboard()
        self.word_length = len(self.secret_word)
        self.remaining_guesses = 5
        self.display_word = ["_"] * self.word_length
        self.guessed_letters = set()
        self.hangman_parts = [
            "  ________",
            "  |      |",
            "  |      O",
            "  |     /|\\",
            "__|__   / \\",
        ]

    def start_game(self):
        print(f"Hi {self.player_name}! Welcome to Hangman!")

    def display_hangman(self):
        for i in range(self.remaining_guesses, 5):
            print(self.hangman_parts[i])

    def play_round(self):
        self.start_game()
        achievement = "Your achievement so far"
        wins = f"Wins: {game.scoreboard.wins}"
        losses = f"Losses: {game.scoreboard.losses}"
        max_length = max(len(achievement), len(wins), len(losses))
        border = '*' * (max_length + 4)  # Add 4 for padding
        print(border)
        print(f"* {achievement:{max_length}} *")
        print(f"* {wins:{max_length}} *")
        print(f"* {losses:{max_length}} *")
        print(border)

        while "_" in self.display_word and self.remaining_guesses > 0:
            print(f"This word contains {len(self.secret_word)} letters!")
            print(f"Guesses remaining: {self.remaining_guesses}")
            self.display_hangman()

            # Print word with guessed letters
            print(self.format_word_with_guesses())

            guess = self.player.get_guess(self.guessed_letters)
            self.make_guess(guess)
           

        if "_" not in self.display_word:
            outcome = "win"
            print(f"Congrats {self.player_name}, you win!")
        else:
            outcome = "lose"
            print(f"You lose! The word was: {self.secret_word}")  
        
        self.scoreboard.record(outcome)


    def make_guess(self, letter):
        if letter in self.secret_word:
            print("Correct!")
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == letter:
                    self.display_word[i] = letter
        else:
            print("Incorrect!")
            self.remaining_guesses -= 1
        self.guessed_letters.add(letter)

    def format_word_with_guesses(self):
        return " ".join(self.display_word)

if __name__ == "__main__":
    game = Hangman()
    
    while True:
        game.play_round()

        # Ask if the user wants to continue playing
        play_again = input("Do you want to play again? (type yes to continue/no to exit): ").lower()
        if not play_again:
            break  

        # Reset the game for a new round        
        game.secret_word = game.word_generator.get_random_word()
        game.display_word = ["_"] * len(game.secret_word)
        game.remaining_guesses = 5
        game.guessed_letters = set()  # Reset guessed letters for a new round
