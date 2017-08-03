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
		
		# display a change-able message
		display_message = tkinter.StringVar()
		display_message.set("Let's play Tic-Tac-Toe!")	
		message = tkinter.Label(self, textvariable=display_message, width=100)
		message.grid(column=0, row=1)
		
		# disable resizing
		self.resizable(False, False)

if __name__ == '__main__':
	my_game = TicTacToe(None)
	my_game.title("Tic Tac Toe")
	my_game.mainloop()
