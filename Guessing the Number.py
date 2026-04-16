#Guessing the Number 

secret= 25
count=0
max_attempts=5

while count < max_attempts:       #infinite loop 
    guess=int(input("Enter the number:"))
    count+=1
    if guess < secret:
        print("Too Low! Try again. 😞")

    elif guess > secret:
        print("Too High! Try again 😞")

    else:
        print("COREECT GUESS 🥳")
        print("Attempets", count)
        break

if count == max_attempts and guess != secret:
    print("Game Over 😢")
    print("The correct number was:", secret)   
    