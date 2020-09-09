n = 4

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


def can_queen_be_placed(n, row, queens_pos):
    if(n == row):
        return True
    for col in range(n):
        can_be_placed = True
        for queen in range(row):
            if queens_pos[queen].col == col or queens_pos[queen].row + queens_pos[queen].col == row + col or queens_pos[queen].row - queens_pos[queen].col == row - col :
                can_be_placed = False
                break
        if(can_be_placed):
            queen = Position(row, col)
            queens_pos[row] = queen
            # print(row, col)
            if(can_queen_be_placed(n, row+1, queens_pos)):
                return True
    return False



queens_pos = []
for i in range(n):
    queens_pos.append(Position(0,0))


if(can_queen_be_placed(4, 0, queens_pos)):
    for queen in queens_pos:
        print(queen.row, queen.col)

