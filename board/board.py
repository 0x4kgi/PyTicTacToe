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
