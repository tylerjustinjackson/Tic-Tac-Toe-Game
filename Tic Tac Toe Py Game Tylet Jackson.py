"""
This is a tic tac toe game that will try to win against you using a basic algorithm 
While most of the coding is from myself, I did use the following citation as inspiration
Citation: https://github.com/Nuhagh/Tic-Tac-Toe-Single-Player-Python/blob/master/tic_tac_toe.py
"""
import random
from time import sleep

def select_x_or_o():
    user=""
    comp=""
    #tells user to select a letter (X or O)
    while(user != "x" and user != "o"):
        user=input("Select X or O: ").replace(" ","").strip().lower()
        if user == "x":
            comp="o"
        else:
            comp="x"
    return user, comp

#to prepare a clear board for the game
def clearboard():
    board=[" " for _ in range(10)]
    return board

#to check if board is full
def boardfull(board):
    return board.count(" ")==0

#to insert a letter (X or O) in a specific position
def letterinsert(board,letter,pos):
    board[pos]=letter

#to take computer moves
def computermove(board,letter):
    computerletter=letter
    possiblemoves=[]
    availablecorners=[]
    availableedges=[]
    availablecenter=[]
    position=-1

    #all possible moves
    for i in range(1,len(board)):
        if board[i] ==" ":
            possiblemoves.append(i)

    #if the position can make X or O wins!
    #the computer will choose it to win or ruin a winning of the user
    for moves in ["x","o"]:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i] = moves
            if winnerwinner(boardcopy,moves):
                position=i


    #if computer cannot win or ruin a winning, then it will choose a random position starting
    if position == -1:
        for i in range(len(board)):
            #an empty index on the board
            if board[i]==" ":
                if i in [1,3,7,9]:
                    availablecorners.append(i)
                if i == 5:
                    availablecenter.append(i)
                if i in [2,4,6,8]:
                    availableedges.append(i)
        #check corners first
        if len(availablecorners)>0:
            print("it comes here")
            #select a random position in the corners
            position=random.choice(availablecorners)
        #then check the availability of the center
        elif len(availablecenter)>0:
            #select the center as the position
            position=availablecenter[0]
        #lastly, check the availability of the edges
        elif len(availableedges)>0:
            #select a random position in the edges
            position=random.choice(availableedges)
    #fill the position with the letter
    board[position]=computerletter

#to draw the board
def drawboard(board):
    board[0]=-1
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-----")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----")
    print(board[7]+"|"+board[8]+"|"+board[9])
    return board

#to check if a specific player is the winner
def winnerwinner(board,letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
    (board[4] == letter and board[5] == letter and board[6] == letter) or \
    (board[7] == letter and board[8] == letter and board[9] == letter) or \
    (board[1] == letter and board[4] == letter and board[7] == letter) or \
    (board[2] == letter and board[5] == letter and board[8] == letter) or \
    (board[3] == letter and board[6] == letter and board[9] == letter) or \
    (board[1] == letter and board[5] == letter and board[9] == letter) or \
    (board[3] == letter and board[5] == letter and board[7] == letter)

#to repeat the game
def repeatgame():

    while True:
        repeat=input("Do you want to play again? (y/n): ").strip().lower()
        if repeat == "y" or repeat =="yes":
            return repeat
        elif repeat =="n" or repeat=="no":
            exit()
        else:
            print("Invalid input...")
            sleep(.5)
            continue

#to play the game
def startgame():
    #letter is your letter, computerleteer is what computer will use against you
    letter, computerletter= select_x_or_o()
    board=clearboard() #makes sure board is clear before starting
    board=drawboard(board)

    while boardfull(board) == False: #check if there are empty positions on the board
        try:
            position=int(input(f"Select a position (1-9) to place an {letter} : " ))
            if board[position] != " " or position not in range(1,10):
                position=int(input(f"Please, choose an empty position to place an {letter} from 1 to 9: "))
        except:
            position=int(input("Enter position using NUMBERS from 1-9: "))

        #put the letter in the selected position & computer plays then draw the board
        letterinsert(board,letter,position)
        #computer move
        computermove(board,computerletter)
        #draw the board
        board=drawboard(board)

        if winnerwinner(board,letter):
            print("Congratulations! You're a WINNER.")
            return repeatgame()
        elif winnerwinner(board,computerletter):
            print("The computer beat you! How unfortunate...")
            return repeatgame()

    if boardfull(board):
        print("Looks like your're as smart a computer. Congrats you tied!")
        return repeatgame()

#Start the game
print("You're about to play Tic Tac Toe")
repeat="y"
while(repeat=="y"):
    repeat=startgame()