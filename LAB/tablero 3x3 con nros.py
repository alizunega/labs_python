board = [['' for i in range(3)] for j in range(3)]
print(board)
n = 0
for i in range(3):
    for j in range(3):
        n+=1
        board[i][j] = n

print(board)        