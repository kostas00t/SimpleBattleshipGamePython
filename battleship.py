# Konstantinos Tsampiras,  A.M. 4508    #
# 1st Semester, Academic Year 2018-2019 #
#########################################

### Importing of required libraries
import random
import os
### Defining of the posprinter (position/board printer) function
def posprinter(position, symbol):
    y_axis = ('a','b','c','d','e')
    pos_id = list(position)
    pos_id[0] = int(chr(ord(pos_id[0])-49))
    pos_id[1] = int(pos_id[1])-1 
    if player_id%2 == 0:
        Board1[pos_id[0]][pos_id[1]] = symbol           
    elif player_id%2 == 1:
        Board2[pos_id[0]][pos_id[1]] = symbol
    BS1 = [''.join(i) for i in Board1]
    BS2 = [''.join(i) for i in Board2]
    zippedBoardstr = [' '.join(i) for i in zip(y_axis, BS1, y_axis, BS2)]
    print('   P1      P2')
    print('  12345   12345')
    print(*zippedBoardstr, sep = '\n')
### Starting values 
validPositions = ('a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5')
Board1 = [[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
Board2 = [[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
num = ('no 1', 'no 2', 'no 3', 'no 4', 'no 5')
num_id1 = 0
num_id2 = 0
player1positions = []
player2positions = []
thrownmissiles1 = []
thrownmissiles2 = []
nplayers = ''
try:
### Game launch
	print('BATTLESHIP GAME \nThe objective is to sink the opponent\'s ships before the opponent sinks yours')
	while nplayers != '1' and nplayers != '2': 
	    nplayers = str(input('Input 1 for 1-player game or 2 for 2-player game: '))
	nplayers = int(nplayers)
### For single player mode (a player vs the computer/CPU). Position assignment of Player 1 and random position assignment of CPU
	if nplayers == 1:
	    while len(player1positions) != 5:
	        x = input('Player 1 enter the position for your ship '+num[num_id1]+': ')
	        while x not in validPositions or x in player1positions:
	            x = input('Invalid Position, or position already taken. Try again: ')
	        else:
	            player1positions.append(x)
	            num_id1 += 1
	    player2positions = random.sample(validPositions, 5)
### For multi player mode (a player vs another player). Position assignment of Player 1 and position assignment of Player 2
	elif nplayers == 2:
	    while len(player1positions) != 5: 
	        x = input('Player 1 enter the position for your ship '+num[num_id1]+': ')
	        while x not in validPositions or x in player1positions:
	            os.system('cls||clear')
	            print('\n' * 40) 
	            x = input('Invalid Position, or position already taken. Try again: ')
	        else:
	            player1positions.append(x)
	            num_id1 += 1
	            os.system('cls||clear')
	            print('\n' * 40)
	    while len(player2positions) != 5:
	        x = input('Player 2 enter the position for your ship '+num[num_id2]+': ')
	        while x not in validPositions or x in player2positions:
	            os.system('cls||clear')
	            print('\n' * 40)
	            x = input('Invalid Position, or position already taken. Try again: ')
	        else:
	            player2positions.append(x)
	            num_id2 += 1
	            os.system('cls||clear')
	            print('\n' * 40)
### Game starts
	player_id = int(random.randrange(2,4)) # Random start
	print('Player', player_id-1, 'starts first')
	posprinter('a1', ' ') # First board print
	while len(player1positions) != 0 and len(player2positions) != 0:
	    while player_id%2 == 0: # Player 1
	        if len(player1positions) == 0 or len(player2positions) == 0:
	            break
	        else:
	            position = input('Player 1 enter the position to throw your missile: ')
	            while position not in validPositions or position in thrownmissiles1:
	                position = input(('Invalid Position, or missile already thrown there. Try again: '))
	            else:
	                if position not in player2positions:
	                    thrownmissiles1.append(position)
	                    player_id += 1
	                    print('Missile thrown at', position,'\nTarget missed!')
	                    posprinter(position,'x')
	                elif position in player2positions:
	                    thrownmissiles1.append(position)
	                    player_id += 1
	                    player2positions.remove(position)
	                    print('Missile thrown at', position,'\nTarget hit!')
	                    posprinter(position,'o')
	    while player_id%2 == 1: # Player 2
	        if len(player1positions) == 0 or len(player2positions) == 0:
	            break
	        else:
	            if nplayers == 2:
	                position = input('Player 2 enter the position to throw your missile: ')
	                while position not in validPositions or position in thrownmissiles2:
	                    position = input(('Invalid Position, or missile already thrown there. Try again: '))
	                else:
	                    if position not in player1positions:
	                        thrownmissiles2.append(position)
	                        player_id += 1
	                        print('Missile thrown at', position,'\nTarget missed!')
	                        posprinter(position,'x')
	                    elif position in player1positions:
	                        thrownmissiles2.append(position)
	                        player_id += 1
	                        player1positions.remove(position)
	                        print('Missile thrown at', position,'\nTarget hit!')
	                        posprinter(position,'o')
	            if nplayers == 1:         
	                position = random.choice(validPositions)
	                if position in thrownmissiles2:
	                    continue
	                else:
	                    if position not in player1positions:
	                        thrownmissiles2.append(position)
	                        player_id += 1 
	                        print('Missile thrown at', position,'\nTarget missed!')
	                        posprinter(position,'x')
	                    elif position in player1positions:
	                        thrownmissiles2.append(position)
	                        player_id += 1
	                        player1positions.remove(position)
	                        print('Missile thrown at', position,'\nTarget hit!')
	                        posprinter(position,'o')
### Game finished, prints the winner
	if len(player2positions) == 0:
	    print('GAME OVER. Player 1 Wins')
	elif len(player1positions) == 0:
	    if nplayers == 2:
	        print('GAME OVER. Player 2 Wins')
	    else:
	        print('GAME OVER. CPU Wins')
except KeyboardInterrupt:
	print('\nProgram Forcibly Terminated')
except:
	print('\nSomething went wrong')