import random

def play():
    while True:  # ← GAME LOOP
        secret = random.randint(1, 100)
        tries = 0
        print("Guess a number between 1 and 100.")

        while True:
            guess = input("Your guess: ").strip()
            if not guess.isdigit():
                print("Enter a whole number.")
                continue

            guess = int(guess)
            tries += 1

            if guess < secret:
                print("Too low.")
            elif guess > secret:
                print("Too high.")
            else:
                print(f"Correct! It took you {tries} tries.")
                break

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break  # exits GAME LOOP

if __name__ == "__main__":
    play()
