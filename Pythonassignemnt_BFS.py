def solve(self, board):
    # Dimensions for the board 
    m, n = len(board), len(board[0])
    # Loading a queue
    queue = deque()
    # Traversing the borders and storing the cells with entry 'O' in queue
    # Traversing [0][0] to [m-1][0] and [0][n-1] to [m-1][n-1]
    for i in range(m):
        if board[i][0] == 'O':
            queue.append((i, 0))
        if board[i][n-1] == 'O':
            queue.append((i, n-1))
    # Traversing [m-1][0] to [m-1][n-1] and [0][0] to [0][n-1]
    for j in range(n):
        if board[0][j] == 'O':
            queue.append((0, j))
        if board[m-1][j] == 'O':
            queue.append((m-1, j))
    # Implementation of Breadth First Search using Queue loaded above 
    while queue:
        # Popinng the vertices from left end of queue and explore it.
        x, y = queue.popleft()
        # If we come across any 'O' in border we mark it as Y as we cannot capture it.
        if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
            board[x][y] = 'Y'
            # We explore its directions and repeat the manpulation
            queue.append((x-1, y)) # Moving Up
            queue.append((x+1, y)) # Moving Down
            queue.append((x, y-1)) # Moving Left
            queue.append((x, y+1)) # Moving Right
    # Traversing every element in board and If we come across Y we make it 'O' else we make it. X.
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'Y':
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'
