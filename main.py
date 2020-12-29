class Board:
    def __init__(self, rowCount, columnCount):
        self.rows = rowCount
        self.columns = columnCount
        self.table = [["-"] * rowCount for _ in range(columnCount)]

    def returnBoard(self):
        return self.table

    def printTable(self):
        table = self.table

        for row in table:
            separator = " | "
            print("| " + separator.join(row) + " |")

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


b = Board(3, 3)
b.inputToCell(2, 2, "a")
b.inputToCell(2, 1, "b")
b.inputToCell(2, 0, "c")
b.inputToCell(1, 0, "d")
b.printTable()
