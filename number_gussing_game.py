import random
import os # nayi line

def load_highscore( level ):
    if os.path.exists( "highscore.txt" ):
        with open("highscore.txt", "r") as f:
            for line in f:
                name, score = line.strip().split(",")
                if name == level:
                    return int(score)
    return 0

def save_highscore(level, score):
    highscores = {}
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            for line in f:
                name, s = line.strip().split(",")
                highscores[name] = int(s)

    if score > highscores.get(level, 0):
        highscores[level] = score

    with open("highscore.txt", "w") as f:
        for name, s in highscores.items():
            f.write(f"{name} , {s}\n")


def play_game(max_number, attempts):
    secret = random.randint(1, max_number)
    score = 100
    points_per_wrong = 100 // attempts
    
    print("I am a Computer, Not human like you ('_')")
    print("Total score is 100, and every wrong attempt points will decrease")
    print(f"Remember, you have only {attempts} chances to guess right.")
    print("I have chosen a number, tell me which nomber is that??")
    
    count_A=0
    while attempts:
        try:
            guess=int(input())
            if (guess > max_number) or (guess < 1):
                print(f"Please enter nomber between 1 to {max_number}")
                continue
                
        except ValueError:
            print("Give Only nomber ")
            continue        
        
        if guess==secret:
            print(f"🎉 Congratulations! You guessed my secret number.\nYour final score is {score}.")
            break
        else:        
             attempts -= 1
             score -= points_per_wrong
             score = max(0, score)
             count_A += 1
             
        if guess > secret:
            print(f"Choose small⬇️ nomber, now only {attempts} chances are remaining.\nYour score is {score}, because this was your {count_A} attempt ")
        
        else:       
            print(f"Choose grester⬆️ nomber, now only {attempts} chances are remaining.\nYour score is {score} because this was your {count_A} attempt")
        
    if attempts == 0 and secret != guess:
        print(f"Sorry, Game over. The nomber was: {secret}\nYour score is {score} because this was your {count_A} last attempt")
while True:             
    try:
         print("1. Easy")
         print("2. Medium")
         print("3. Hard")
         choice = int(input("Choose difficulty: "))
         if choice == 1:
             play_game(10, 5)
         elif choice == 2:
             play_game(50, 7)
         elif choice == 3:
             play_game(100, 10)
         else:
             print("Invalid choice")
    except:    
        print("Play w1ith numbers only")
    try:
         ans=input("Do you want to Play again? yes/no").lower()
    except ValueError:
         print("it must be an intiger")


    
     
