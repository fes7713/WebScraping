import random

answer = random.randint(0, 9999)
print(answer)
name = input("What is ur name : ")
attemptLimit = int(input("Type attempt limit :"))
currentTry = 0

commentWrong = ["Wrong!!", "Try Again!!", "Not Even Close!!", "Another One!"]
commentClose = ["Getting Close!!", "That was Close One", "What!!", "Keep Trying!"]
commentVeryClose = ["One More Try!!", "Bit More!", "You can Do it!"]

print("\n" * 2)
while True:
    print("Player :" +
          name + "\t"*4 +
          "Remaining Try {0}".format(attemptLimit-currentTry))

    if attemptLimit < currentTry:
        print("Game Over")

    inputNum = int(input("Type ur guess : \t"))

    print()

    diffNum = abs(answer - inputNum) > 9999//4
    if diffNum < 9999//4:
        print("\t" * 2 + "*" * 5 + commentClose[random.randint(0, len(commentClose))] + "*" * 5)
    elif diffNum < 9999//32:
        print("\t" * 2 + "*" * 5 + commentVeryClose[random.randint(0, len(commentVeryClose))] + "*" * 5)
    else:
        print("\t" * 2 + "*" * 5 + commentWrong[random.randint(0, len(commentWrong))] + "*" * 5)

    if answer == inputNum:
        print("Game clear : Answer was {}".format(answer))
        break
    elif answer > inputNum:
        print("\tAnswer is more than your guess!!" + "\n" * 2)
    else:
        print("\tAnswer is less than your guess!!" + "\n" * 2)

    currentTry += 1