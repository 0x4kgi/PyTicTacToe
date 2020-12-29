class Board:
    def __init__(self, rowCount, columnCount):
        self.rows = ["-"] * rowCount
        self.table = [self.rows] * columnCount
        # self.cols = [self.rows] * columnCount
        # self.table = self.cols

    def returnBoard(self):
        return self.table

    def printTable(self):
        table = self.table

        for row in table:
            separator = " | "
            print("| " + separator.join(row) + " |")

    def inputToCell(self, x, y, data):
        self.table[x][y] = data

        self.printTable()


b = Board(15, 15)
b.inputToCell(0, 10, "a")
