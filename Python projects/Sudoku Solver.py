board = [[3,0,0,8,0,1,0,0,2],
         [2,0,1,0,3,0,6,0,4],
         [0,0,0,2,0,4,0,0,0],
         [8,0,9,0,0,0,1,0,6],
         [0,6,0,0,0,0,0,5,0],
         [7,0,2,0,0,0,4,0,9],
         [0,0,0,5,0,9,0,0,0],
         [9,0,4,0,8,0,7,0,5],
         [6,0,0,1,0,7,0,0,3]
]

def print_board(board):
        i = 0
        for x in board:
            print(x[0],x[1],x[2],"|",x[3],x[4],x[5],"|",x[6],x[7],x[8])
            i+=1
            if i==3 or i==6:
                print("-"*21)
                
def find_empty(board):
    for row,numbers in enumerate(board):
        for element in numbers:
            if element == 0:
                return row,numbers.index(element) #returns row, column of empty element
    return False #false if board is no longer empty

#check for horizontal, vertical, 3x3 squares
def check_valid(board,row,col,num):
    #checking horizontal
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False
    
    #checking vertical
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False
    
    #checking each box
    box_x = col//3
    box_y = row//3
    
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i,j)!=(row,col):
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row,col = find
    
    for num in range(1,10):
        if check_valid(board,row,col,num):
            board[row][col] = num
            
            if solve(board):
                return True
            
            board[row][col] = 0
    return False

print("SUDOKU SOLVER".center(21,'-'))
print_board(board)
print("|".center(21))
print("|".center(21))
print("v".center(21))
solve(board)
print_board(board)