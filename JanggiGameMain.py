from JanggiGameClass import JanggiGame

def main():
    """Main Game"""
    game = JanggiGame()
    # game.print_board()
    move_result = game.make_move('c1', 'e3') #should be False because it's not Red's turn
    print(move_result)
    move_result = game.make_move('a7', 'b7') #should return True
    print(move_result)
    state = game.get_game_state() #should return UNFINISHED
    print(state)
    game.make_move('b7','b6') #should return True
    print(state)
    game.make_move('b3','b6') #should return False because it's an invalid move
    game.make_move('a1','a4') #should return True
    game.make_move('c7','d7') #should return True
    # game.print_board()
    game.get_game_state()
    answer = game.make_move('a4','a4') #this will pass the Red's turn and return True
    print(answer)

if  __name__ == '__main__':
    main()
