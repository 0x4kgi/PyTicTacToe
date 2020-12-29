from board import Board

# 3x3, row equal test
a = Board(3, 3)
a.inputToCell(0, 0, "a")
a.inputToCell(0, 1, "a")
a.inputToCell(0, 2, "a")
a.inputToCell(1, 0, "b")
a.inputToCell(1, 1, "b")
a.inputToCell(1, 2, "b")
a.inputToCell(2, 0, "c")
a.inputToCell(2, 1, "c")
a.inputToCell(2, 2, "c")
a.printTable()
print(f"Row: 0 // {a.checkRowEquality(0)}")
print(f"Row: 1 // {a.checkRowEquality(1)}")
print(f"Row: 2 // {a.checkRowEquality(2)}")
print(f"Column: 0 // {a.checkColumnEquality(0)}")
print(f"Column: 1 // {a.checkColumnEquality(1)}")
print(f"Column: 2 // {a.checkColumnEquality(2)}")

# 3x3, column equal test
b = Board(3, 3)
b.inputToCell(0, 0, "a")
b.inputToCell(0, 1, "b")
b.inputToCell(0, 2, "c")
b.inputToCell(1, 0, "a")
b.inputToCell(1, 1, "b")
b.inputToCell(1, 2, "c")
b.inputToCell(2, 0, "a")
b.inputToCell(2, 1, "b")
b.inputToCell(2, 2, "c")
b.printTable()
print(f"Row: 0 // {b.checkRowEquality(0)}")
print(f"Row: 1 // {b.checkRowEquality(1)}")
print(f"Row: 2 // {b.checkRowEquality(2)}")
print(f"Column: 0 // {b.checkColumnEquality(0)}")
print(f"Column: 1 // {b.checkColumnEquality(1)}")
print(f"Column: 2 // {b.checkColumnEquality(2)}")

# 10x10, row equal test
c = Board(10, 10)
for col in range(10):
    c.inputToCell(0, col, "a")
c.printTable()
print(f"Row 0 // {c.checkRowEquality(0)}")
print(f"Column 0 // {c.checkColumnEquality(0)}")

# 10x10, column equal test
d = Board(10, 10)
for row in range(10):
    d.inputToCell(row, 0, "a")
d.printTable()
print(f"Row 0 // {d.checkRowEquality(0)}")
print(f"Column 0 // {d.checkColumnEquality(10)}")
