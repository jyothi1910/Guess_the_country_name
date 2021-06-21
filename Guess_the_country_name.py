
import random
Country_names=["India","Korea","Japan","China","USA"]
print(Country_names)
randomName = random.choice(Country_names)
for guessTaken in range(1,4):
    guess=input("Take a guess:")
    if guess != randomName:
        print("Your guess is wrong, try another guess")
    elif guess == randomName:
        print("Well done you guess is correct, you guessed country name in ",end="")
        print(str(guessTaken)+" guess")
        break
else:
    print("Nope, The correct country name is "+randomName)
