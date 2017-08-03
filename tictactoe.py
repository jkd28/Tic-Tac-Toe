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
				
	def get_sector_tops(self, sector):
		return {
			1: {'left_x':0,'left_y':0,  'right_x':100, 'right_y':0},
			2: {'left_x':100,'left_y':0,  'right_x':200, 'right_y':0},
			3: {'left_x':200,'left_y':0,  'right_x':300, 'right_y':0},
			4: {'left_x':0,'left_y':100,  'right_x':100, 'right_y':100},
			5: {'left_x':100,'left_y':100,  'right_x':200, 'right_y':100},
			6: {'left_x':200,'left_y':100,  'right_x':300, 'right_y':100},
			7: {'left_x':0,'left_y':200,  'right_x':100, 'right_y':200},
			8: {'left_x':100,'left_y':200,  'right_x':200, 'right_y':200},
			9: {'left_x':200,'left_y':200,  'right_x':300, 'right_y':200}
		}[sector]
	 
	def get_sector_bottoms(self, sector):
		return {
			1: {'left_x':0,'left_y':100, 'right_x':100, 'right_y':100},
			2: {'left_x':100,'left_y':100, 'right_x':200, 'right_y':100},
			3: {'left_x':200,'left_y':100, 'right_x':300, 'right_y':100},
			4: {'left_x':0,'left_y':200, 'right_x':100, 'right_y':200} ,
			5: {'left_x':100,'left_y':200, 'right_x':200, 'right_y':200},
			6: {'left_x':200,'left_y':200, 'right_x':300, 'right_y':200},
			7: {'left_x':0,'left_y':300, 'right_x':100, 'right_y':300},
			8: {'left_x':100,'left_y':300, 'right_x':200, 'right_y':300},
			9: {'left_x':200,'left_y':300, 'right_x':300, 'right_y':300}
		}[sector]
	
	def draw_x_in(self, sector, event):
		top = self.get_sector_tops(sector)
		bottom = self.get_sector_bottoms(sector)
		print('Drawing line')
		print('(' + str(top['left_x']) + ', ' + str(top['left_y']) + ') to (' + str(bottom['left_x']) + ', ' + str(bottom['left_y']) + ')')
		event.widget.create_line(top['left_x'], top['left_y'], bottom['left_x'], bottom['left_y'], fill="black")
		self.update()
			
	def draw_o_in(self, sector, event):
		#print('Will draw Circle')
		return 
		
	def screen_click(self, event):
		sector = self.determine_sector(event.x, event.y)
		set_sector(sector, event)
	
def set_sector(sector, event):
	global current_player, game_tiles
	sector_index = sector - 1
	
	if current_player%2 == 0:
		to_set = 'x'
		my_game.draw_x_in(sector, event)
	else:
		to_set = 'o'
		my_game.draw_o_in(sector, event)

	game_tiles[sector_index] = to_set
	
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
	
	global my_game
	my_game = TicTacToe(None)
	my_game.title("Tic Tac Toe")
	my_game.mainloop()
