from collections import deque  # importing required libraires

class Solution:  # Defining class
    def __init__(self,char_1,char_2,row,col):
        # Defining variable for entries
        self.char_1 = char_1
        self.char_2 = char_2
        self.char_temp = "Y"
        self.row=row
        self.col=col
        self.board=[]

    # BFS Approach
    def solve_bfs(self):
        # When board is empty
        if self.board == []:
            return self.board
        # Dimensions for the board
        self.m, self.n = self.row,self.col
        # Loading a queue
        queue = deque()
        # Exception handling block
        try:
            # Traversing the borders and storing the cells with entry 'O' in queue
            # Traversing [0][0] to [m-1][0] and [0][n-1] to [m-1][n-1]
            for i in range(self.m):
                if self.board[i][0] == self.char_2:
                    queue.append((i, 0))
                if self.board[i][self.n - 1] == self.char_2:
                    queue.append((i, self.n - 1))
            # Traversing [m-1][0] to [m-1][n-1] and [0][0] to [0][n-1]
            for j in range(self.n):
                if self.board[0][j] == self.char_2:
                    queue.append((0, j))
                if self.board[self.m - 1][j] == self.char_2:
                    queue.append((self.m - 1, j))
            # Implementation of Breadth First Search using Queue loaded above
            while queue:
                # Popinng the vertices from left end of queue and explore it.
                x, y = queue.popleft()
                # If we come across any 'O' in border we mark it as Y as we cannot capture it.
                if (
                    0 <= x < self.m
                    and 0 <= y < self.n
                    and self.board[x][y] == self.char_2
                   ):
                    self.board[x][y] = self.char_temp
                    # We explore its directions and repeat the manpulation
                    queue.append((x - 1, y))  # Moving Up
                    queue.append((x + 1, y))  # Moving Down
                    queue.append((x, y - 1))  # Moving Left
                    queue.append((x, y + 1))  # Moving Right
            # Traversing every element in board and If we come across Y we make it 'O' else we make it. X.
            for i in range(self.m):
                for j in range(self.n):
                    if self.board[i][j] == self.char_temp:
                        self.board[i][j] = self.char_2
                    else:
                        self.board[i][j] = self.char_1
        # Exception handler for handling exceptions
        except Exception as e:
            print("An error occurred:", e)

    # DFS Approach
    def solve_dfs(self):
        # When board is empty
        if self.board == []:
            return self.board
        # Dimensions of board
        self.a, self.b = self.row,self.col
        # Exception handling block
        try:

            def dfs(m, n):
                # Base condition if we exceeded the limit or traversed through X we do nothing
                if (
                    n < 0
                    or m < 0
                    or n == len(self.board[0])
                    or m == len(self.board)
                    or self.board[m][n] != self.char_2
                ):
                    return
                # Else we change it to temporary variable Y
                self.board[m][n] = self.char_temp
                # We explore its directions and repeat the manpulation
                dfs(m + 1, n)  # Moving Down
                dfs(m, n + 1)  # Moving Right
                dfs(m - 1, n)  # Moving Up
                dfs(m, n - 1)  # Moving Left
            # Traversing every element in board and If we come across 'O' we move it to dfs and explore its neighbours.
            for i in range(self.a):
                for j in range(self.b):
                    # If element is 'O; and is in borders of board we move it to dfs
                    if self.board[i][j] == self.char_2 and (
                        i in [0, self.a - 1] or j in [0, self.b - 1]
                    ):
                        dfs(i, j)
                # Traversing every element in board and If we come across Y we make it 'O' else we make it. X.
            for i in range(self.a):
                for j in range(self.b):
                    if self.board[i][j] == self.char_2:
                        self.board[i][j] = self.char_1
                    if self.board[i][j] == self.char_temp:
                        self.board[i][j] = self.char_2
        # Exception handler for handling exceptions
        except Exception as e:
            print("An error occurred:", e)

    def print_board(self):
        for r in self.board:
            for c in r:
                print(c, end=" ")
            print()
    
    def validator(self):
        # try block for validating the input
        try:
            for g in range(len(self.board)):
                for h in range(len(self.board[0])):
                    if self.board[g][h] not in (self.char_1, self.char_2):
                        raise Exception("Invalid Input")
        # Catching the exception if any occurs
        except IndexError as e:
            print("An error occured, board is not in shape, ",e)
        except Exception as e:
            print("An error",e)
