from tkinter import *

def create_window():
	# top/master window
	root = Tk()
	canvas_height = 300
	canvas_width = 300
	division = 100
	screen = Canvas(root, height=canvas_height, width=canvas_width)
	screen.pack()
	
	# draw vertical lines
	screen.create_line(100, 0, 100, 300)
	screen.create_line(200, 0, 200, 300)
	# draw horizontal lines
	screen.create_line(0, 100, 300, 100)
	screen.create_line(0, 200, 300, 200)
	
	# create message box
	message = Message(root, text="Let's Play TIC-TAC-TOE", width=300)
	message.pack()
	return root


if __name__ == '__main__':
	# main game logic
	board = create_window()
	board.mainloop()
	
