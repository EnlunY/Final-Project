import turtle
from turtle import Turtle, Screen, mainloop
import random

bob = turtle.Turtle()
bob.speed(-1)
count = 0
turtle.bgcolor("#bf693d")
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 24
add = ["2", "3", "4", "5", "6"]
minus = ["10", "J", "Q", "K", "A"]
random.shuffle(deck)


def drawCard(card, x, y, faceDown=False):
    bob.up()
    bob.goto(x, y)
    bob.down()
    bob.color("black")
    bob.begin_fill()
    bob.setheading(0)
    bob.forward(100)
    bob.setheading(300)
    bob.forward(5)
    bob.setheading(270)
    bob.forward(152)
    bob.setheading(240)
    bob.forward(5)
    bob.setheading(180)
    bob.forward(100)
    bob.setheading(120)
    bob.forward(5)
    bob.setheading(90)
    bob.forward(152)
    bob.setheading(60)
    bob.forward(5)
    bob.color("white")
    bob.end_fill()
    bob.up()
    if not faceDown:
        bob.setheading(0)
        bob.forward(55)
        bob.setheading(270)
        bob.forward(76)
        bob.color("black")
        bob.write(card, align="center", font=("Arial", 50, "normal"))


def playerDeal():
    global playerCardLoc
    global playerTotal
    global count
    card = deck[0]
    deck.pop(0)
    if card in minus:
        playerTotal += 10
        count -= 1
    elif card in add:
        playerTotal += int(card)
        count += 1
    else:
        playerTotal += int(card)

    drawCard(card, playerCardLoc, -100)
    playerCardLoc += 120


def dealerDeal(faceDown=False):
    global dealerCardLoc
    global dealerTotal
    global count
    dealerCard = deck[0]
    deck.pop(0)
    if dealerCard in minus:
        dealerTotal += 10
        count -= 1
    elif dealerCard in add:
        dealerTotal += int(dealerCard)
        count += 1
    else:
        dealerTotal += int(dealerCard)
    drawCard(dealerCard, dealerCardLoc, 200, faceDown) 
    if not faceDown: 
        dealerCardLoc += 120
    return dealerCard


def playBlackjack(deck):
    playerBust = False
    faceDown = False
    global dealerCardLoc
    global playerTotal
    global dealerTotal
    global count

    for i in range(2):
        playerDeal()

        # Gives out card to dealer, second one facedown
        if faceDown:
            dealerCard = dealerDeal(faceDown)
        else:
            dealerDeal()
            faceDown = True

    # Player's turn
    while True:
        # Allows user to hit or stand
        decision = input("Hit (h/hit) or Stand (s/stand): ")
        if decision in ["h", "hit", "H", "Hit"]:
            playerDeal()
            if playerTotal > 21:
                drawCard(dealerCard, dealerCardLoc, 200)  
                print("Bust, you lose")
                playerBust = True
                break

        elif decision in ["s", "stand", "S", "Stand"]:
            break
        else:
            print("Invalid entry")
    
    # Dealer's turn
    if not playerBust:
        # Redraws facedown card
        drawCard(dealerCard, dealerCardLoc, 200)  
        dealerCardLoc += 120      
        while True:  
            # Draws card if total is < 17
            if dealerTotal < 17:
                dealerDeal()
            elif dealerTotal > 21:
                print("Dealer bust, you win")
                break       
            elif dealerTotal > playerTotal:
                print("You lose")
                break
            elif dealerTotal < playerTotal:
                print("You win")
                break
            elif dealerTotal == playerTotal:
                print("Tie")
                break
                

while True:
    playerCardLoc = -200
    dealerCardLoc = -200
    dealerTotal = 0
    playerTotal = 0
    playBlackjack(deck)
    
    # Count request?
    countReq = input("Display count? (y/yes) or (n/no): ")
    if countReq in ["y", "yes", "Y", "Yes"]:
        print("Count:", count)
    
    # Keep playing?
    again = input("Keep playing? (y/yes) or (n/no): ")
    if again in ["y", "yes", "Y", "Yes"]:
        bob.clear()
        continue
    elif again in ["n", "no", "N", "No"]:
        break


def table():
    bob.up()
    bob.goto(-500,250)
    bob.down()
    bob.color("green")
    for i in range(4):
        bob.begin_fill()
        bob.forward(1000)
        bob.right(90)
        bob.forward(600)
        bob.right(90)
        bob.end_fill()
    
table()




