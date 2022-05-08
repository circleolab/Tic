class Player:
    def __init__(self):

        self.count = 0
        self.row = None
        self.column = None
        self.row_column = None

    def player_input(self):
        if self.count % 2 == 0:
            self.row = int(input("亲爱的X玩家，请选择您放置的行数（一共3行）： "))
            self.column = int(input("亲爱的X玩家，请选择您放置的列数（一共3列）： "))

        else:
            self.row = int(input("亲爱的O玩家，请选择您放置的行数（一共3行）： "))
            self.column = int(input("亲爱的O玩家，请选择您放置的列数（一共3列）： "))
        self.count += 1
        self.row_column = [self.row, self.column]
