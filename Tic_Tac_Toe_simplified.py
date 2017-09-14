
def Tic_Tac_Toe():
	
	if raw_input("Player1. do you want to play the game (Y/N)? ")== 'N' or raw_input("Player2. do you want to play the game (Y/N)? ")== 'N':
		print "Game Over"
		return
	player1Positions =[]
	player2Positions =[]
					
	while True:
		position1 = raw_input('Player1, enter your next position: ').split(',')
		temp = [int(position1[0]),int(position1[1])]

		check_occupied("player1", temp, player1Positions, player2Positions)
		
		if check_win(player1Positions) == True:
			print "Player1 Wins!! Congratulations!!!"
			Tic_Tac_Toe()
		
		position2 = raw_input('Player2, enyou your next position: ').split(',')
		temp = [int(position2[0]),int(position2[1])]

		check_occupied("player2", temp, player2Positions, player1Positions)
		if check_win(player2Positions) == True:
			print "Player2 Wins!! Congratulations!!!"
			Tic_Tac_Toe()
			
def check_occupied(pos, positionlist1, positionlist2):
	if pos not in positionlist1 and pos not in positionlist2:
			positionlist1.append(pos)
			
	else:
		while pos in positionlist1 or pos in positionlist2:
			print "This position was already accupied, please re-enter a new one"
			newPosition = raw_input("Reenter your next position: ").split(',')
			pos = [int(newPosition[0]),int(newPosition[1])]
		positionlist1.append(pos)		
	positionlist1.sort()
	print positionlist1
		
def check_win(positionlist):
	for position in positionlist:
		if [position[0]+1,position[1]+1] in positionlist and [position[0]+2,position[1]+2] in positionlist:
			return True
	return False	
			
			
def setUpGame():
	canvas_size = 100
	
	
	
