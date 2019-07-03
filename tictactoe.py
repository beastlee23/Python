#imports
import random
import os

#Program code
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_board(my_board):
	print(my_board[6]+'|'+my_board[7]+'|'+my_board[8])
	print('-----')
	print(my_board[3]+'|'+my_board[4]+'|'+my_board[5])
	print('-----')
	print(my_board[0]+'|'+my_board[1]+'|'+my_board[2])

def clearMethod():
	print('\n'*100)

def getMarkerPlayer1():
	val = ''
	while(val != 'X' and val !='O'):
		val = input("Please pick a mark 'X' or 'O: ")
	return val

def getMarkerPlayer2(player1):
	if(player1 == 'X'):
		return 'O'
	else:
		return 'X'

def getPosition():
	num = int(input('Please enter a number (1-9): '))
	if num not in [1,2,3,4,5,6,7,8,9]:
		num = int(input('Please enter a number (1-9): '))
	return num


def place_marker(board, marker, position):
	newPos = position - 1
	board[newPos] = marker

def win_check(board, marker):
	if board[0] == marker and board[1] == marker and board[2] == marker:
		return True
	elif board[3] == marker and board[4] == marker and board[5] == marker:
		return True
	elif board[6] == marker and board[7] == marker and board[8] == marker:
		return True
	elif board[6] == marker and board[4] == marker and board[2] == marker:
		return True
	elif board[0] == marker and board[4] == marker and board[8] == marker:
		return True
	elif board[6] == marker and board[3] == marker and board[0] == marker:
		return True
	elif board[7] == marker and board[4] == marker and board[1] == marker:
		return True
	elif board[8] == marker and board[5] == marker and board[1] == marker:
		return True
	else:
		return False

def choose_first():
	return random.randint(1,2)

def space_check(board, position):
	if(board[position-1] == ' '):
		return True
	else:
		return False

def full_board_check(board):
    count = 0
    while count < 9:
    	if board[count] == ' ':
    		return False
    	count += 1
    return True

def player_choice(board):
	choice = getPosition()
	while space_check(board,choice) == False:
		choice = getPosition()
	return choice

def replay():
	val = ''
	while(val != 'Y' and val !='N'):
		val = input("Do you want to play again (Y/N)? ")
	return val


#RUN PROGRAM

def program():
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

	print('Welcome to Tic Tac Toe!')
	print()

	print_board(board)
	print()

	player1 = getMarkerPlayer1()
	player2 = getMarkerPlayer2(player1)
	print("Player 1 marker: "+player1)
	print("Player 2 marker: "+player2)
	print()

	while full_board_check(board) == False and win_check(board, player1) == False and win_check(board, player1) == False:
		print()
		print('Player 1')
		pos = player_choice(board)
		place_marker(board,player1,pos)
		print_board(board)
		print('Player 1 turn over')
		print()
		if full_board_check(board) != True:
			if win_check(board, player1) == False:
				print('Player 2')
				pos = player_choice(board)
				place_marker(board,player2,pos)
				print_board(board)
				print('Player 2 turn over')
				print()

	else:
		if win_check(board, player1) == True:
			print('Congratulations Player 1 - you have won!')
		elif win_check(board, player2) == True:
			print('Congratulations Player 2 - you have won!')
		else:
			print('Board is Full - no one wins')
			playAgain = replay()
			if playAgain == 'Y':
				program()
			else:	
				print('Tic Tac Toe Terminating')

program()

