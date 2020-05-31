# Snake Water Gun Game
import random
import sys
a = 0
b = ["S" , "W" , "G"]
count = 0           # When Computer Wins
count1 = 0          # When User Wins
count2 = 0          # When Draw
while a < 10:
    print("Enter 'S' for Snake")
    print("Enter 'W' for Water")
    print("Enter 'G' for Gun")
    c = input("Enter Your Choice:- ")
    if c == "S":
        d = random.choice(b)
        if d == "S":
            count2 = count2 + 1
        elif d == "W":
            count1 = count1 + 1
        elif d == "G":
            count = count + 1
    elif c == "W":
        d = random.choice(b)
        if d == "S":
            count2 = count2 + 1
        elif d == "W":
            count1 = count1 + 1
        elif d == "G":
            count = count + 1
    elif c == "G":
        d = random.choice(b)
        if d == "S":
            count2 = count2 + 1
        elif d == "W":
            count1 = count1 + 1
        elif d == "G":
            count = count + 1
    else:
        print("Enter Correct Choice")
        sys.exit()
    a = a + 1
print("Computer Wins " , count , " Times")
print("User Wins " , count1 , " Times")
print("Draw " , count2 , " Times")
if count > count1:
    if count > count2:
        print("Final Result:- Computer Wins")
elif count1 > count:
    if count1 > count2:
        print("Final Result:- User Wins")
else:
    print("Final Result:- Draw")