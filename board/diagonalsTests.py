from board import Board

size = 3

diag = Board(size, size)

diag.inputToCell(0, 0, 'X')
diag.inputToCell(1, 1, 'X')
diag.inputToCell(2, 2, 'X')

diag.printTable()

if diag.checkDiagonalsEquality(1, 1):
    print("yeah")
else:
    print("nop")

diag.inputToCell(0, 2, 'X')
diag.inputToCell(1, 1, 'X')
diag.inputToCell(2, 0, 'X')

diag.printTable()

if diag.checkDiagonalsEquality(1, 1):
    print("yeah")
else:
    print("nop")
