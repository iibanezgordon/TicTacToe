# -*- coding: utf-8 -*-
"""
Initial Version of a Tic Tac Toe Game
By Iker Ibanez
Started 05/05/2017
"""

import tictactoefunctions
from IPython.display import clear_output


repeat = False 
Victory = False
replay = True
while replay :
    Board, Players, player, status = tictactoefunctions.inicio()
    while not Victory :
        if tictactoefunctions.gamefinish(Board):
            break
        else:
            selection = raw_input(' Please, player {}, introduce your field selection    '.format(Players[player])).upper()
            Board, repeat = tictactoefunctions.turno(Board,selection,Players,player,repeat)
            if repeat:
                while repeat:
                    selection = raw_input(' Please, player {}, introduce your field selection    '.format(Players[player])).upper()
                    Board, repeat = tictactoefunctions.turno(Board,selection,Players,player,repeat)
            Victory = tictactoefunctions.Victory_check(Board,player)
            tictactoefunctions.print_board(Board)
            if Victory :
                print ' Player {} Wins! congratulations '.format(Players[player])
                print ' Execute the script again for another Game '
                
            else:
                player =int(1 - player) ## If player is 0, players changes to 1, if is 1, to 0
                clear_output()
    replay = False 
    replay = raw_input(' Do you want to play the game again? Y/N    ').upper().startswith('Y')
    

    


    



