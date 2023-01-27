def solve(self, board):
    # Dimensions for the board 
    m=len(board)
    n=len(board[0])
    # Defining a function for dfs
    def dfs(m,n):
        # Base condition if we exceeded the limit or traversed through X we do nothing
        if n <0 or m<0 or n == len(board[0]) or m == len(board) or board[m][n]!='O':
            return
        # Else we change it to temporary variable Y
        board[m][n]='Y'
        # We explore its directions and repeat the manpulation
        dfs(m+1,n) # Moving Down
        dfs(m,n+1) # Moving Right
        dfs(m-1,n) # Moving Up
        dfs(m,n-1) # Moving Left
    # Traversing every element in board and If we come across 'O' we move it to dfs and explore its neighbours.
    for i in range(m):
        for j in range(n):
            #If element is 'O; and is in borders of board we move it to dfs
            if (board[i][j]=='O' and (i in [0,m-1] or j in [0,n-1])):
                dfs(i,j)
    # Traversing every element in board and If we come across Y we make it 'O' else we make it. X.
    for i in range(m):
        for j in range(n):
            if board[i][j]=='O':
                board[i][j]='X'
            if board[i][j]=='Y':
                board[i][j]='O  
