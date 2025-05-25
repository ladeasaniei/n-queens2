class BacktrackingSolver:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n

    def is_safe(self, row, col):
        for r in range(row):
            if self.board[r] == col or abs(self.board[r] - col) == abs(r - row):
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            return self.board[:]
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                solution = self.solve(row + 1)
                if solution:
                    return solution
                self.board[row] = -1
        return None
