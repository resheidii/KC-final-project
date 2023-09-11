def check_guess(guess, answer) :
    global score
    still_gussing = True
    attempt = 0
    while still_gussing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_gussing = False
        else :
            if attempt < 2 :
                guess = input("Sorry Wrong Answer, try again") 
                attempt = attempt + 1
            if attempt == 3:
                 print("The Correct Answer is" , answer ) 

level = 1
score = 0
print("Guess the Animal")
print("first Level")
guess1 = input("Which bear lives at the Nourth Pole ?")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal?")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal?")
check_guess(guess3, "Blue whale")
print("Your Score is " + str(score))


print("Guess the Animal")
print("second Level")
print("your score is " + str(score))
guess4 = input("Which is the only land animal that cannot jump ?")
check_guess(guess4, "Elephant")
guess5 = input("Which animal never sleeps?")
check_guess(guess5, "Bullfrog")
guess6 = input(" Which birds eye is bigger than its brain?")
check_guess(guess6, "Ostrich")
print("Game is over , great job !")
print("Your Score is " + str(score))
