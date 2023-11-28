import turtle
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
    bob.color("white")
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
    bob.end_fill()
    if not faceDown:
        bob.setheading(0)
        bob.forward(55)
        bob.setheading(270)
        bob.forward(76)
        bob.color("black")
        bob.write(card, align="center", font=("Arial", 50, "normal"))
    bob.up()

def playerPlay(card, playerTotal):
    pass

def dealerPlay(card, dealerTotal):
    pass

def playBlackjack(deck):
    dealerTotal = 0
    playerTotal = 0
    faceDown = False
    while True:
        if not deck:
            break
        
        for i in range(2):
            card = deck[0]
            deck.pop(0)
            if card in ["A", "J", "Q", "K"]:
                playerTotal += 10
            else:
                playerTotal += int(card)
            drawCard(card, -50, 50)
            if faceDown:
                card = deck[0]
                deck.pop(0)
                if card in ["A", "J", "Q", "K"]:
                    dealerTotal += 10
                else:
                    dealerTotal += int(card)
                drawCard(card, -50, 50, faceDown)   
                faceDown = False
            else:
                card = deck[0]
                deck.pop(0)
                if card in ["A", "J", "Q", "K"]:
                    dealerTotal += 10
                else:
                    dealerTotal += int(card)
                drawCard(card, -50, 50)  
                faceDown = True  

        if playerTotal < 21:
            playerPlay(card, playerTotal)







        






playBlackjack(deck)
turtle.done()