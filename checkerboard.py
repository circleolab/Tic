def judgement_h_v(list_j, words):
    dict_repeat_count = {i: list_j.count(i) for i in list_j}
    for i in dict_repeat_count:
        if dict_repeat_count[i] >= 3:
            print(words)
            return True
        else:
            return False


class CheckerBoard:
    '''
    实现棋盘的初始化，更新，相关坐标记录， 棋局胜负判定的功能
    带修饰的staticsmethod 与 staticmethod(被导入到主模块中的类，可以直接调用原模块中的静态方法，而主方法中不能直接访问。）
    类变量是最佳"全局变量"，如果不使用类变量，为了变更某一状态量，可能需要层层return回去，不易理解。真正的全局变量容易被交叉影响，带来不可估计后果
    '''

    def __init__(self):
        self.items = [["   ", "|", "   ", "|", "   "],
                      ["-----------"],
                      ["   ", "|", "   ", "|", "   "],
                      ["-----------"],
                      ["   ", "|", "   ", "|", "   "]]
        self.x_o = [" X ", " O "]
        self.symbol_X = []
        self.symbol_O = []
        self.diagonal_1 = [(1, 1), (2, 2), (3, 3)]
        self.diagonal_2 = [(1, 3), (2, 2), (3, 1)]

        self.game_on = True

    def update_board(self, r_c_list, count):
        player_index = (count - 1) % 2
        row = r_c_list[0]
        column = r_c_list[1]
        player_symbol = self.x_o[player_index]  # 若是偶数，则是 X
        row_to_change = self.index_map(row)  # 默认玩家从1数起
        column_to_change = self.index_map(column)
        self.items[row_to_change][column_to_change] = player_symbol

        if player_symbol == " X ":
            self.symbol_X.append((row, column))
            print(self.symbol_X)
        else:
            self.symbol_O.append((row, column))

    @staticmethod
    def index_map(num):
        if num == 1:
            return 0
        elif num == 2:
            return 2
        elif num == 3:
            return 4

    def print_borad(self):
        for line in range(len(self.items)):
            print("".join(self.items[line]))

    def judgment(self, count):

        if count > 9:
            print('游戏结束，没有赢家')
            self.game_on = False

        elif count > 4:
            x_symbol_X = [i[0] for i in self.symbol_X]
            y_symbol_X = [i[1] for i in self.symbol_X]
            x_symbol_O = [i[0] for i in self.symbol_O]
            y_symbol_O = [i[1] for i in self.symbol_O]
            if judgement_h_v(x_symbol_X, "X是赢家"):
                self.game_on = False
            elif judgement_h_v(y_symbol_X, "X是赢家"):
                self.game_on = False
            elif judgement_h_v(x_symbol_O, "O是赢家"):
                self.game_on = False
            elif judgement_h_v(y_symbol_O, "O是赢家"):
                self.game_on = False
            elif self.judgement_diagonal(self.symbol_X, "X是赢家"):
                self.game_on = False
            elif self.judgement_diagonal(self.symbol_O, "O是赢家"):
                self.game_on = False

    def judgement_diagonal(self, list_tuple, words):
        condition_1 = all(items in list_tuple for items in self.diagonal_1)
        condition_2 = all(items in list_tuple for items in self.diagonal_2)
        if condition_1 or condition_2:
            print(words)
            return True
        else:
            return False
