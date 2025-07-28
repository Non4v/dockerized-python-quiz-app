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

answer = input(" What does "URL" stand for?")
if answer.lower() == ("Uniform Resource Locator"):
    print("Correct!")
    score += 1
else:
    print("incorrect")

answer = input("What does IP address stand for? ")
if answer.lower() == ("Internal Protocol adress"):
    print("Correct!")
    score += 1
else:
    print("incorrect")

answer = input("What language is primarily used for web page structure? ")
if answer.lower() == ("HTML"):
    print("Correct!")
    score += 1
else:
    print("incorrect")

answer = input("What does CI/CD stand for? ")
if answer.lower() == (" Continuous Integration / Continuous Deployment"):
    print("Correct!")
    score += 1
else:
    print("incorrect")

print("You got  " + str(score) + " questions correct! ")

print("It's " + str((score/5)*100) + "%")
