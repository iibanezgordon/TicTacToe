# -*- coding: utf-8 -*-
"""
Initial Version of a Tic Tac Toe Game Functions
By Iker Ibanez
Started 05/05/2017
"""
def inicio():
    '''
    Function that initializes the game. 
    The empty Board dictionary is created. and printed.
    The names of the players are asked and stored in the list Players.
    '''
    import random
    status =['-','X','0']
    Players=[]
    Board = {'A1':status[0], 'A2' :status[0], 'A3': status[0], 'B1':status[0],
             'B2': status[0], 'B3': status[0], 'C1': status[0], 'C2': status[0],
             'C3': status[0]}
    print_board(Board)
    print ' Starting the Game!'
    playerA = raw_input('Please, Introduce the name of the First player  ').upper()
    playerB = raw_input('Please, Introduce the name of the Second player  ').upper()
    Players =[playerA,playerB]
    player = random.randint(0,1)
    print ' {} starts first!'.format(Players[player])
    
    return Board, Players, player, status


def gamefinish(Board):
    '''
    Function that performs a check to see if the Board is full without having a
    winner. Which ends the game in a TIE
    '''
    finito =0
    for key in Board:
        if Board[key] != '-':
            finito += 1 
    if finito >= 9:
        print ' The game has finished in a TIE, do you want to try again?'
        return True
    else:
        return False




def turno(Board,selection,Players,player,repeat):
    '''
    Function that conducts one turn of the game.
    There are two initial checks to see:
        -If the Board is full and the game is finished in a TIE
        -If the selection from the current player is not correct
    Then the Board Dictionary is updated with the move. and the current player
    is changed.
    '''
    if gamefinish(Board):
        repeat = False
    elif selection not in Board.keys() or Board[selection] != '-' :
        print ' Incorrect field selection\n'
        print ' Please, Select one valid field '
        print ' The available fields are the following:\n'
        for key in Board:
            if Board[key] == '-':
                print 'Field available --> {}'.format(key)
                repeat = True
    elif player == 0:
        Board[selection] = 'X'
        repeat = False
    elif player == 1:
        Board[selection] = '0'
        repeat = False
    else:
        print ' ERROR, PLAYER NAME CORRUPTED START THE GAME AGAIN'
    return Board, repeat
            
def Victory_check(Board,player):
    '''
    Function that checks the current Board with a Victory matrix to see if
    the current player has won.
    '''
    Victory = 0
    if player == 0:
        status_check = 'X'
    else:
        status_check = '0'
    Victory_matrix =[{'A1':status_check, 'A2':status_check, 'A3':status_check},
                     {'B1':status_check, 'B2':status_check, 'B3':status_check},
                     {'C1':status_check, 'C2':status_check, 'C3':status_check},
                     {'A1':status_check, 'B1':status_check, 'C1':status_check},
                     {'A2':status_check, 'B2':status_check, 'C2':status_check},
                     {'A3':status_check, 'B3':status_check, 'C3':status_check},
                     {'B2':status_check, 'A1':status_check, 'C3':status_check},
                     {'B2':status_check, 'A3':status_check, 'C1':status_check}]
            
    for item in Victory_matrix:
        iter_keys = item.keys()
        Victory = False
        if item[iter_keys[0]] == Board[iter_keys[0]] and item[iter_keys[1]] == Board[iter_keys[1]] and item[iter_keys[2]] == Board[iter_keys[2]]:
            Victory = True
    return Victory
        
def print_board(Board):
    '''
    Function that simply Prints a version of the Board,with the values of the
    Board Dictionary
    '''
    
    print '            A             B               C           '
    print '    ---------------|---------------|---------------   '
    print '  1            {}   |      {}       |      {}         1'.format(Board['A1'],Board['B1'],Board['C1'])
    print '    ---------------|---------------|---------------   '
    print '  2            {}   |      {}       |      {}         2'.format(Board['A2'],Board['B2'],Board['C2'])
    print '    ---------------|---------------|---------------   '
    print '  3            {}   |      {}       |      {}         3'.format(Board['A3'],Board['B3'],Board['C3'])
    print '    ---------------|---------------|---------------   ' 
    print '           A              B               C           '
        
    
            
    
    
    