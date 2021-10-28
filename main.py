import random
import json
import datetime

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list[:3]))


secret = random.randint(1, 30)
attempts = 0
name = input("What's your name?: ")
wrong_guesses = []


while True:

    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    current_time = datetime.datetime.now()
    wrong_guesses.append(guess)

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name,
                           "wrong_guesses": wrong_guesses})

        with open("score_list.json", "w") as score_file:
            sorted_score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]  # ne dela in ne najdem razloga
            score_file.write(json.dumps(score_list))

            for score_dict in score_list:
                print("attempts: " + (str(score_dict["attempts"]) + ", date: " +
                                      score_dict.get("date") + " player: " 
                                      + (str(name) + ", wrong guesses:" 
                                      + str((score_dict["wrong_guesses"])))))

        print("You've guessed it " + str(name) + ", congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
