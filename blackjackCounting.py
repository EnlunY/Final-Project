import turtle
from turtle import Turtle, Screen, mainloop
import random

bob = turtle.Turtle()
bob.speed(-1)
turtle.bgcolor("#bf693d")
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 24
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

def playerDraw(playerTotal):
    print("Hello")
def playerStand(playerTotal):
    pass

def dealerPlay(card, dealerTotal):
    pass

def playBlackjack(deck):
    dealerTotal = 0
    playerTotal = 0
    playerTurn = True
    faceDown = False
    playerCard = -200
    dealerCard = -200

    for i in range(2):
            
            # Gives out card to player
            card = deck[0]
            deck.pop(0)
            if card in ["A", "J", "Q", "K"]:
                playerTotal += 10
            else:
                playerTotal += int(card)
            drawCard(card, playerCard, -100)
            playerCard += 120

            # Gives out card to dealer, second one facedown
            if faceDown:
                card = deck[0]
                deck.pop(0)
                if card in ["A", "J", "Q", "K"]:
                    dealerTotal += 10
                else:
                    dealerTotal += int(card)
                drawCard(card, dealerCard, 200, faceDown)   
                faceDown = False
                dealerCard += 120
            else:
                card = deck[0]
                deck.pop(0)
                if card in ["A", "J", "Q", "K"]:
                    dealerTotal += 10
                else:
                    dealerTotal += int(card)
                drawCard(card, dealerCard, 200)  
                faceDown = True
                dealerCard += 120

    screen = Screen()
    while True:
        # Check if deck is empty
        if not deck:
            break

        if playerTurn:
            turtle.onkey(playerDraw(playerTotal), "h")
            turtle.onkey(playerStand, "s")
            turtle.listen()
            mainloop()




playBlackjack(deck)
turtle.done()

#ahhhhh