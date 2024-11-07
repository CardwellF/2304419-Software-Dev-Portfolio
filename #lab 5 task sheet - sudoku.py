'''generate board and answer'''
board=[
    [8,0,5,6,7,0,0,4,2],
    [6,9,0,5,2,3,7,1,8],
    [0,0,2,1,0,8,6,5,0],
    [4,8,0,7,0,6,5,2,1],
    [1,2,6,0,0,0,9,7,3],
    [9,0,0,0,0,0,0,0,0],
    [0,4,0,0,5,7,0,0,0],
    [0,6,0,8,0,0,0,3,7],
    [0,7,0,3,6,4,0,9,0],
]
answer=[
    [8,1,5,6,7,9,3,4,2],
    [6,9,4,5,2,3,7,1,8],
    [7,3,2,1,4,8,6,5,9],
    [4,8,3,7,9,6,5,2,1],
    [1,2,6,4,8,5,9,7,3],
    [9,5,7,2,3,1,8,6,4],
    [3,4,1,9,5,7,2,8,6],
    [5,6,9,8,1,2,4,3,7],
    [2,7,8,3,6,4,1,9,5],
]
run=True       
'''imputs'''
while run:
    '''display board'''
    for row in board:
        print(" ".join(map(str, row)))
    '''inputs for number'''
    number=int(input("enter a number 1 - 9: "))
    '''number validation raising error if conditions met'''
    if number == 0 or number>9:
        print("error")
        continue
    '''inputs for row and column -1 for indexing'''
    row=int(input("enter a row number 1 - 9: "))-1
    column=int(input("enter a column number 1 - 9: "))-1
    '''checks for number in answer[cords] and checks the board[cords] position is 0'''
    if number == answer[row][column] and board[row][column]==0:
        '''sents board[row input][column input] to the number input'''
        board[row][column]=number
    else:
        '''prints error if conditions not met'''
        print("error")
    '''checks if board is complete'''
    if board == answer:
        replay=None
        while replay not in ("yes", "no"):
            try:
                replay=input("whould you like to play again (yes or no): ")
                if replay == "yes":
                    run=True
                if replay == "no":
                    run=False
            except:
                print("answer not acceptable")
    else:
        continue