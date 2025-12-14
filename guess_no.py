import random
number = 1

print ("Welcome to no guessing game.we have a nummber that needs to be guessed. you have 10 attempts.")
print("The secret number is between1 and 50")
secret_number = random.randint(1,50)
# secret_number = 28
attempts = 10
is_guess_correct = False

while number <= 10:
    print(f"you have {attempts} attempts remaining.")
    user_number =int(input ("Enter your guess: "))
    if user_number == secret_number:
        print("congrates its matched")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower ="lower"
        print(f"Your guess is wrong! Try{higher_or_lower} number.")

    number += 1
    attempts -= 1
if is_guess_correct == False:
    print("Bad luck")
print(f"The secrete numbers was{secret_number}. Game Over!!")