from checkerboard import CheckerBoard
from player import Player

is_game_on = True
checkerboard = CheckerBoard()
player = Player()
judgement = True


def game_begin():
    new_checkerboard = CheckerBoard()
    new_player = Player()
    print("棋盘如下所示：有三行三列")
    new_checkerboard.print_borad()
    while new_checkerboard.game_on:
        new_player.player_input()
        # print(player.count, player.row, player.column)
        new_checkerboard.update_board(r_c_list=new_player.row_column, count=new_player.count)
        new_checkerboard.print_borad()
        new_checkerboard.judgment(count=new_player.count)


if __name__ == "__main__":
    '''
    这是一个名为 Tic Tac Toe 的游戏，游戏规则为某玩家率先达成 三个棋子水平，竖直或对焦线，则胜利
    v1： 该版本实现了两人工玩家的，对抗性比赛
    V2: 想要添加 某玩家输入已被选过位置 提示重选功能， 超出范围重选提示功能，通过raise去做
    V3： 想要添加AI，随机生成位置，玩家可以选择游戏模式
    '''

    while is_game_on:
        game_begin()
        if (input("还想继续游戏吗？ Yes or No: ")).upper() != "YES":
            is_game_on = False
