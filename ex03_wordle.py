"""Wordle game."""
__author__ = "730678249"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word_search: str, single_char: str) -> bool:
    """To check of a single character is found in any index of the second string."""
    assert len(single_char) == 1
    if single_char in word_search:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis whose color determines whether or not the letters in guess are in the correct spots or not."""
    assert len(guess) == len(secret)
    index: int = 0
    emoji: str = ""
    while index < len(secret):
        if secret[index] == guess[index]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """It will ask the user for a guess and keep asking for one until its the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret_word: str = "codes"
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(5)
        emoji_result = emojified(secret_word, guess)
        print(emoji_result)
        if guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
