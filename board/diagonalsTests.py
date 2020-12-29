from board import Board

size = 10

diag = Board(size, size)

for row in range(size):
    for col in range(size):
        if diag.checkDiagonalsEquality(row, col):
            diag.inputToCell(row, col, 'X')

diag.printTable()
