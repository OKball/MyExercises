theBoard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
            'ml': ' ', 'mm': ' ', 'mr': ' ',
            'll': ' ', 'lm': ' ', 'lr': ' '}



def printBoard(board):
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['ll'] + '|' + board['lm'] + '|' + board['lr'])



def overlapVerification(presentTurn):
    print("Turn " + str(presentTurn) + " - choose position")
    move = input()
    while True: 
            if move not in theBoard or theBoard[move] == 'X' or theBoard[move] == 'O':
                print('incorrect value, please input proper value')
                move = input()
                continue
            else:
                theBoard[move] = presentTurn
                break



def comparasion(boardPosition1, boardPosition2, boardPosition3):
    if theBoard[boardPosition1] == theBoard[boardPosition2] == theBoard[boardPosition3] != ' ':
        return True
    else:
        return False



def winningCondition():
    if comparasion("tl", "tm", "tr") == True:
        return True
    elif comparasion("ml", "mm", "mr"):
        return True
    elif comparasion("ll", "lm", "lr"):
        return True
    elif comparasion("tl", "ml", "ll"):
        return True
    elif comparasion("tm", "mm", "lm"):
        return True
    elif comparasion("tr", "mr", "lr"):
        return True
    elif comparasion("tl", "mm", "lr"):
        return True
    elif comparasion("ll", "mm", "tr"):
        return True
    else:
        return False
    


Turn = 'X'
for i in range(9):
    if Turn == 'X':
        overlapVerification("X")
        print(" ")
        printBoard(board=theBoard)
        print(" ")
        if winningCondition() == True:
            print("you won :)")
            break 
        Turn = "O"
    else:
        overlapVerification("O")
        print(" ")
        printBoard(board=theBoard)
        print(" ")
        if winningCondition() == True:
            print("you won :)")
            break 
        Turn = 'X'



print('end')
input()