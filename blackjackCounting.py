import turtle
from turtle import Turtle, Screen, mainloop
import random

bob = turtle.Turtle()
tom = turtle.Turtle()
tom.speed(-1)
bob.speed(-1)
count = 0
turtle.bgcolor("#bf693d")
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 24
add = ["2", "3", "4", "5", "6"]
minus = ["10", "J", "Q", "K"]
bank = 1000
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
    global playerCards
    card = deck[0]
    deck.pop(0)

    if card == "A":
        if playerTotal + 11 > 21:
            playerTotal += 1
            count -= 1
            playerCards.append(card)
        else:
            playerTotal += 11
            count -= 1
            playerCards.append(card)

    # Facecard
    elif card in minus:
        playerTotal += 10
        count -= 1
        playerCards.append(card)
    elif card in add:
        playerTotal += int(card)
        count += 1
        playerCards.append(card)
    else:
        playerTotal += int(card)
        playerCards.append(card)

    drawCard(card, playerCardLoc, -100)
    playerCardLoc += 120


def dealerDeal(faceDown=False, upcard=False):
    global dealerCardLoc
    global dealerTotal
    global count
    global dealerCards
    global dealerUpcard
    dealerCard = deck[0]
    deck.pop(0)
    if dealerCard == "A":
        if dealerTotal + 11 > 21:
            dealerTotal += 1
            count -= 1
            playerCards.append(dealerCard)
            if upcard:
                dealerUpcard["A"] = 1
        else:
            dealerTotal += 11
            count -= 1
            playerCards.append(dealerCard)
            if upcard:
                dealerUpcard["A"] = 11

    # Facecard
    elif dealerCard in minus:
        dealerTotal += 10
        count -= 1
        dealerCards.append(dealerCard)
        if upcard:
            dealerUpcard[dealerCard] = 10
    elif dealerCard in add:
        dealerTotal += int(dealerCard)
        count += 1
        dealerCards.append(dealerCard)
        if upcard:
            dealerUpcard[dealerCard] = int(dealerCard)
    else:
        dealerTotal += int(dealerCard)
        dealerCards.append(dealerCard)
        if upcard:
            dealerUpcard[dealerCard] = int(dealerCard)

    drawCard(dealerCard, dealerCardLoc, 200, faceDown) 
    if not faceDown: 
        dealerCardLoc += 120
    return dealerCard


def optimalMove(playerTotal, dealerTotal):
    upcard = list(dealerUpcard.values())
    if "A" not in playerCards:
        if playerTotal >= 17 or (playerTotal in [13, 14, 15, 16] and upcard[0] >= 2 and upcard[0] <= 6) or (playerTotal == 12 and upcard[0] >= 4 and upcard[0] <= 6):
            return ["s", "stand", "S", "Stand"]
        elif playerTotal == 11 or playerTotal == 10 and upcard[0] <= 9 or (playerTotal == 9 and upcard[0] <= 6 and upcard[0] >= 3):
            return ["d", "double", "D", "Double"]
        else:
            return ["h", "hit", "H", "Hit"]
    else:
        if playerTotal == 20 or playerTotal == 19 and upcard[0] != 6 or (playerTotal == 18 and upcard[0] == 7 or upcard[0] == 8):
            return ["s", "stand", "S", "Stand"]



def playBlackjack(bet):
    playerBust = False
    faceDown = False
    double = False
    global playerCards
    global dealerCards
    global dealerCardLoc
    global playerTotal
    global dealerTotal
    global count
    global bank

    for i in range(2):
        playerDeal()

        # Gives out card to dealer, second one facedown
        if faceDown:
            dealerCard = dealerDeal(faceDown)
        else:
            dealerDeal(False, True)
            faceDown = True
                

    # Player's turn
    while True:
        # Allows user to hit or stand
        decision = input("Hit (h/hit), Stand (s/stand), or Double (d/double): ")
        if decision in optimalMove(playerTotal, dealerTotal):
            print("Correct decision")
        else:
            print("Wrong decision")

        if decision in ["h", "hit", "H", "Hit"]:
            playerDeal()
            if playerTotal > 21:
                if "A" in playerCards[0] or "A" in playerCards[1]:
                    playerCards.remove("A")
                    playerTotal -= 10
                    continue
                else:
                    drawCard(dealerCard, dealerCardLoc, 200)  
                    print("Bust, you lose")
                    playerBust = True
                    if double:
                        bank -= bet * 2
                    else:
                        bank -= bet
                    break
        elif decision in ["d", "double", "D", "Double"]:
            double = True
            playerDeal()
            if playerTotal > 21:
                if "A" in playerCards[0] or "A" in playerCards[1]:
                    playerCards.remove("A")
                    playerTotal -= 10
                    continue
                else:
                    drawCard(dealerCard, dealerCardLoc, 200)  
                    print("Bust, you lose")
                    playerBust = True
                    if double:
                        bank -= bet * 2
                    else:
                        bank -= bet
                    break
        elif decision in ["s", "stand", "S", "Stand"]:
            break
        else:
            print("Invalid entry")
    
    # Dealer's turn and finishes the play
    if not playerBust:
        # Reveals facedown card
        drawCard(dealerCard, dealerCardLoc, 200)  
        dealerCardLoc += 120      
        while True:  
            # Draws card if total is < 17
            if dealerTotal == 21 and "A" in dealerCards:
                if playerTotal == 21 and "A" in playerCards:
                    print("Tie")
                    break
                else:
                    print("You lose")
                    if double:
                        bank -= bet * 2
                    else:
                        bank -= bet
                    break
            elif playerTotal == 21 and "A" in playerCards:
                if dealerTotal == 21 and "A" in dealerCards:
                    print("Tie")
                    break
                else:
                    print("You win")
                    if double:
                        bank += bet * 2 * 1.5
                    else:
                        bank -= bet
                    break
            elif dealerTotal < 17:
                dealerDeal()
            elif dealerTotal > 21:
                if "A" in dealerCards:
                    dealerCards.remove("A")
                    dealerTotal -= 10
                    continue
                else:
                    print("Dealer bust, you win")
                    if double:
                        bank += bet * 2 * 1.5
                    else:
                        bank += bet * 1.5
                    break       
            elif dealerTotal > playerTotal:
                print("You lose")
                if double:
                    bank -= bet * 2
                else:
                    bank -= bet
                break
            elif dealerTotal < playerTotal:
                print("You win")
                if double:
                    bank += bet * 2 * 1.5
                else:
                    bank += bet * 1.5
                break
            elif dealerTotal == playerTotal:
                print("Tie")
                break
def table():
    tom.up()
    tom.goto(-500,250)
    tom.down()
    tom.color("green")
    for i in range(4):
        tom.begin_fill()
        tom.forward(1000)
        tom.right(90)
        tom.forward(600)
        tom.right(90)
        tom.end_fill()


# Runs blackjack until the user says to stop
table()
while True:
    playerCardLoc = -200
    dealerCardLoc = -200
    dealerTotal = 0
    playerTotal = 0
    playerCards = []
    dealerCards = []
    dealerUpcard = {}
    print("Bank:", bank)
    while True:
        bet = int(input("How much do you want to bet? (Max: 500): "))
        if bet > 500 or bet < 1:
            print("Invalid bet")
        else:
            break
    playBlackjack(bet)
    print("Bank:", bank)

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






