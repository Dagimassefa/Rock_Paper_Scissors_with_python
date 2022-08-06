import random
import os


#------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------Menu before starting the game--------------------------------------------------
print(" \t \t \t \t \t \t \t MENU")
print("\t \t \t \t \t Press 1 to start playing the game")
print("\t \t \t \t \t Press 2 to if you seek a walkthrough")
print("\t \t \t \t \t Press 3 to see your scores")
print("\t \t \t \t \t Press 0 to Exit")
menu_response=int(input("Please enter your choice: "))
#-----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------function for starting the game------------------------------------------------


def start_playing():
    counter=0
    high_score=0
    count_score=0
    while True and counter <5:
        choices=['rock','paper','scissors']
        computer=random.choice(choices)
        player=None
        while player not in choices:
            player=input("Rock,Paper or Scissors?: ").lower()
            if player==computer:
                print("The computer has chossen a "+computer)
                print("You have chossen a "+player)
                print("Both you and the computer has chossen "+player+", It is a TIE!")
            elif player=='rock':
                if computer=='paper':
                    print("The computer has chossen a "+computer)
                    print("You have chossen a "+player)
                    print("You have LOST the game!")
                elif computer=='scissors':
                    print("The computer has chossen a "+computer)
                    print("You have chossen a "+player)
                    print("You have WON the game!")
                    count_score+=1
            elif player=='scissors':
                if computer=='paper':
                    print("The computer has chossen a "+computer)
                    print("You have chossen a "+player)
                    print("You have WON the game!")
                    count_score+=1
                elif computer=='rock':
                    print("The computer has chossen a "+computer)
                    print("You have chossen a "+player)
                    print("You have LOST the game!")
            elif player=='paper':
                if computer=='rock':
                    print("The computer has chossen a "+computer)
                    print("You have chossen a "+player)
                    print("You have WON the game!")
                    count_score+=1
                elif computer=='scissors':
                    print("The computer has chossen a "+computer)
                    print("You have chossen a "+player)
                    print("You have LOST the game!")
                    continue
            counter+=1
            while counter==5:
                print("Score = "+str(count_score))
                with open('score.txt','a') as file:
                    file.write("Score = "+str(count_score)+"\n")
                play_again=input("Do you want to play again press yes to continue or press no to exit? yes/no: ").lower()
                while play_again !="no" and play_again !="yes":
                    print("Please enter only yes to continue playing or no to exit!")
                    play_again=input("Do you want to play again press yes to continue or press no to exit? yes/no: ").lower()
                if play_again=="yes":
                    count_score=0
                    counter=0
                    continue
                elif play_again =="no":
                    break
    print("It was a good game!")


#-------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------function explaining how to play the game----------------------------------------------   
def rules():
    print("\t \t \t \t \t RULES (the parameters of gameplay)")
    print("\t \t \t \t 1. Each round, each of two players simultaneously chooses between Rock, Paper and Scissors.")
    print("\t \t \t \t 2. If they choose the same, the game is a tie")
    print("\t \t \t \t 3. Paper beats rock (covering rock).")
    print("\t \t \t \t 4. Rock beats scissors (crushing scissors).")
    print("\t \t \t \t 5. Scissors beats paper (cutting paper).")
    print("\t \t \t \t 6. A player wins a round by throwing a winning symbol.")
    print("\t \t \t \t \t \t \t \t I wish you good luck!")


#--------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------function for reading the scores--------------------------------------------------
def Highscore():
    try:
        with open('score.txt') as file:
            print(file.read())
    except  FileNotFoundError:
        print("file not found")
def exit_game():
    with open('score.txt','w') as file:
        file.write("Enjoy playing the game.\nYou can leave ur comment at kuku.assefa18@gmail.com")
    print("See you soon i hope you enjoyed the game!")

while menu_response !=1 and menu_response !=2 and menu_response !=3 and menu_response !=0 :
    print("Please enter a choice from the menu :)")
    menu_response=int(input("Please enter your choice: "))
if menu_response==1:
    start_playing()
elif menu_response==2:
    rules()
elif menu_response==3:
    Highscore()
elif menu_response==0:
    exit_game()




