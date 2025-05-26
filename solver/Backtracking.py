class BacktrackingSolver:
    def __init__(self, size):
        self.size = size
        self.positions = [-1] * size

    def can_place(self, current_row, candidate_col):
        for previous_row in range(current_row):
            if self.positions[previous_row] == candidate_col or \
               abs(self.positions[previous_row] - candidate_col) == abs(previous_row - current_row):
                return False
        return True

    def find_solution(self, current_row=0):
        if current_row == self.size:
            return self.positions[:]

        for candidate_col in range(self.size):
            if self.can_place(current_row, candidate_col):
                self.positions[current_row] = candidate_col
                result = self.find_solution(current_row + 1)
                if result:
                    return result
                self.positions[current_row] = -1
        return None
