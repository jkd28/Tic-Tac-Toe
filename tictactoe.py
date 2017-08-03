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
		board.bind("<Button-1>", self.screen_click)
		
		self.game_board = board
		
		# display a change-able message
		display_message = tkinter.StringVar()
		display_message.set("Let's play Tic-Tac-Toe!")	
		message = tkinter.Label(self, textvariable=display_message, width=100)
		message.grid(column=0, row=1)
		
		# disable resizing
		self.resizable(False, False)
	
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

	def screen_click(self, event):
		sector = self.determine_sector(event.x, event.y)
		set_sector(sector)
	
	#def draw_x_in(self, sector)
	#def draw_o_in(self, sector)
	
def set_sector(sector):
	global current_player, game_tiles
	sector_index = sector - 1
	
	if current_player%2 == 0:
		to_set = 'x'
	else:
		to_set = 'o'

	game_tiles[sector_index] = to_set
	#TODO draw shape on canvas 
	current_player += 1
	check_win_condition()

def check_win_condition():
	global game_tiles
	#TODO add win condition check
	
if __name__ == '__main__':
	global current_player
	current_player = 0
	
	global game_tiles
	game_tiles = [i for i in range(1,10)]
	
	my_game = TicTacToe(None)
	my_game.title("Tic Tac Toe")
	my_game.mainloop()
