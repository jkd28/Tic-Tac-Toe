#!/usr/bin/env python3
import tkinter
from time import sleep


class TicTacToe(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        canvas_height = 300
        canvas_width = 300
        division = 100
        # ceate the game board
        board = tkinter.Canvas(self, height=canvas_height, width=canvas_width)
        board.grid(column=0, row=0)

        # draw vertical lines
        board.create_line(100, 0, 100, 300)
        board.create_line(200, 0, 200, 300)
        # draw horizontal lines
        board.create_line(0, 100, 300, 100)
        board.create_line(0, 200, 300, 200)

        # bind the left mouse click event to the board
        board.bind('<Button-1>', self.screen_click)

        # display a change-able message
        self.display_message = tkinter.StringVar()
        self.display_message.set('Let\'s play Tic-Tac-Toe!')
        message = tkinter.Label(self, textvariable=self.display_message, width=100)
        message.grid(column=0, row=1)

        # disable resizing
        self.resizable(False, False)

    def setDisplayMessage(self, message):
        self.display_message.set(message)

    def determine_sector(self, x, y):
        if x < 100:
            if y < 100:
                return 1
            elif y < 200:
                return 4
            else:
                return 7
        elif x < 200:
            if y < 100:
                return 2
            elif y < 200:
                return 5
            else:
                return 8
        else:
            if y < 100:
                return 3
            elif y < 200:
                return 6
            else:
                return 9

    def get_sector_tops(self, sector):
        return {
            1: {'left_x': 0, 'left_y': 0,  'right_x': 100, 'right_y': 0},
            2: {'left_x': 100, 'left_y': 0,  'right_x': 200, 'right_y': 0},
            3: {'left_x': 200, 'left_y': 0,  'right_x': 300, 'right_y': 0},
            4: {'left_x': 0, 'left_y': 100,  'right_x': 100, 'right_y': 100},
            5: {'left_x': 100, 'left_y': 100,  'right_x': 200, 'right_y': 100},
            6: {'left_x': 200, 'left_y': 100,  'right_x': 300, 'right_y': 100},
            7: {'left_x': 0, 'left_y': 200,  'right_x': 100, 'right_y': 200},
            8: {'left_x': 100, 'left_y': 200,  'right_x': 200, 'right_y': 200},
            9: {'left_x': 200, 'left_y': 200,  'right_x': 300, 'right_y': 200}
        }[sector]

    def get_sector_bottoms(self, sector):
        return {
            1: {'left_x': 0, 'left_y': 100, 'right_x': 100, 'right_y': 100},
            2: {'left_x': 100, 'left_y': 100, 'right_x': 200, 'right_y': 100},
            3: {'left_x': 200, 'left_y': 100, 'right_x': 300, 'right_y': 100},
            4: {'left_x': 0, 'left_y': 200, 'right_x': 100, 'right_y': 200},
            5: {'left_x': 100, 'left_y': 200, 'right_x': 200, 'right_y': 200},
            6: {'left_x': 200, 'left_y': 200, 'right_x': 300, 'right_y': 200},
            7: {'left_x': 0, 'left_y': 300, 'right_x': 100, 'right_y': 300},
            8: {'left_x': 100, 'left_y': 300, 'right_x': 200, 'right_y': 300},
            9: {'left_x': 200, 'left_y': 300, 'right_x': 300, 'right_y': 300}
        }[sector]

    def draw_x_in(self, sector, event):
        top = self.get_sector_tops(sector)
        bottom = self.get_sector_bottoms(sector)

        event.widget.create_line(top['left_x'], top['left_y'], bottom['right_x'], bottom['right_y'], fill='black', width=1.5)
        event.widget.create_line(top['right_x'], top['right_y'], bottom['left_x'], bottom['left_y'], fill='black', width=1.5)

        self.update()

    def draw_o_in(self, sector, event):
        top = self.get_sector_tops(sector)
        bottom = self.get_sector_bottoms(sector)

        event.widget.create_oval(top['left_x'], top['left_y'], bottom['right_x'], bottom['right_y'], width=1.5)
        event.widget.create_oval(top['right_x'], top['right_y'], bottom['left_x'], bottom['left_y'], width=1.5)

        self.update()

    def screen_click(self, event):
        sector = self.determine_sector(event.x, event.y)
        set_sector(sector, event)


def set_sector(sector, event):
    global current_player, game_tiles, my_game
    sector_index = sector - 1

    if game_tiles[sector_index] == 'x' or game_tiles[sector_index] == 'o':
        my_game.setDisplayMessage('That space is taken! Pick again')
        return

    to_set = ''

    if current_player == 0:
        to_set = 'x'
        my_game.draw_x_in(sector, event)
    elif current_player == 1:
        to_set = 'o'
        my_game.draw_o_in(sector, event)
    else:
        my_game.quit()
        print(current_player)
        print('ERROR: Something went wrong.')
        exit(1)

    game_tiles[sector_index] = to_set

    if win_condition_met():
        event.widget.unbind('<Button-1>')
        my_game.setDisplayMessage('We have a Winner!! \n' + to_set + '\'s win!\n' +'GAME OVER')
        return
    else:
        current_player = (current_player + 1) % 2
        my_game.setDisplayMessage('')


def check_lines_for_win(line_group):
    for line in line_group:
        if game_tiles[line[0]-1] == game_tiles[line[1]-1] == game_tiles[line[2]-1]:
            return True
    return False


def win_condition_met():
    global game_tiles

    horizontals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    verticals = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    diagonals = [[1, 5, 9], [3, 5, 7]]

    return check_lines_for_win(horizontals) or check_lines_for_win(verticals) or check_lines_for_win(diagonals)


if __name__ == '__main__':
    global current_player
    current_player = 0

    global game_tiles
    game_tiles = [i for i in range(1, 10)]

    global my_game
    my_game = TicTacToe(None)
    my_game.title('Tic Tac Toe')
    my_game.mainloop()
