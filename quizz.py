print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("okay lets play")
score = 0

answer = input("What does CPU mean?")
if answer.lower() == ("central processing unit "):
    print("Correct!")
    score += 1

else:
    print("incorrect")

answer = input("Which is bigger: sun or moon?")
if answer.lower() == ("sun"):
    print("Correct!")
    score += 1
else:
    print("incorrect")

answer = input("What is water? ")
if answer.lower() == ("liquid"):
    print("Correct!")
    score += 1
else:
    print("incorrect")

answer = input("what is biggest continent ")
if answer.lower() == ("asia"):
    print("Correct!")
    score += 1
else:
    print("incorrect")

answer = input("when was first world war ")
if answer.lower() == ("1914"):
    print("Correct!")
    score += 1
else:
    print("incorrect")

print("You got  " + str(score) + " questions correct! ")

print("It's " + str((score/5)*100) + "%")
