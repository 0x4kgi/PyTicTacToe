class Board:
    def __init__(self, rowCount, columnCount):
        self.rows = rowCount
        self.columns = columnCount
        self.table = [["-"] * rowCount for _ in range(columnCount)]

    # def __init__

    def returnBoard(self):
        return self.table

    # def returnBoard

    def printTable(self):
        table = self.table

        for row in table:
            separator = " | "
            print("| " + separator.join(row) + " |")

    # def printTable

    def inputToCell(self, x, y, data, isIndexed=True):
        if x > self.rows:
            print("Invalid X range")
            return False

        if y > self.columns:
            print("Invalid Y range")
            return False

        if isIndexed == False:
            x -= 1
            y -= 1

        self.table[x][y] = data

    # def inputToCell

    def checkRowEquality(self, rowIndex):
        row = self.table[rowIndex]

        if row.count(row[0]) == len(row):
            return True

        return False

    # def checkRowEquality

    def checkColumnEquality(self, columnIndex):
        base = self.table[0][columnIndex]

        for rowIndex in range(self.columns):
            if base != self.table[rowIndex][columnIndex]:
                return False

        return True

    # def checkColumnEquality


# class Board

"""
TESTS
"""

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