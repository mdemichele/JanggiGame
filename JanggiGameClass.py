# Author: Matthew DeMichele
# Date: Last Updated 13 August 2021
# Description: This program contains the class definition for a game of Janggi. Program was built for Oregon State University CS 162 - Introduction to Computer Science II

class JanggiGame:
    """class defines the Janggi Board Game"""
    
    def __init__(self):
        """initializes class instances"""
        self._state = "UNFINISHED"
        self._board = [
                        [["a1","R","Chariot1"],["b1","R","Elephant1"],["c1","R","Horse1"],["d1","R","Guard1"],["e1",""],["f1","R","Guard2"],["g1","R","Elephant2"],["h1","R","Horse2"],["i1","R","Chariot2"]],
                        [["a2","",""],["b2","",""],["c2","",""],["d2","",""],["e2","R","General"],["f2","",""],["g2","",""],["h2","",""],["i2","",""]],
                        [["a3","",""],["b3","R","Cannon1"],["c3","",""],["d3","",""],["e3","",""],["f3","",""],["g3","",""],["h3","R","Cannon2"],["i3","",""]],
                        [["a4","R","Soldier1"],["b4","",""],["c4","R","Soldier2"],["d4","",""],["e4","R","Soldier3"],["f4","",""],["g4","R","Soldier4"],["h4","",""],["i4","R","Soldier5"]],
                        [["a5","",""],["b5","",""],["c5","",""],["d5","",""],["e5","",""],["f5","",""],["g5","",""],["h5","",""],["i5","",""]],
                        [["a6","",""],["b6","",""],["c6","",""],["d6","",""],["e6","",""],["f6","",""],["g6","",""],["h6","",""],["i6","",""]],
                        [["a7","B","Soldier1"],["b7","",""],["c7","B","Soldier2"],["d7","",""],["e7","B","Soldier3"],["f7","",""],["g7","B","Soldier4"],["h7","",""],["i7","B","Soldier5"]],
                        [["a8","",""],["b8","B","Cannon1"],["c8","",""],["d8","",""],["e8","",""],["f8","",""],["g8","",""],["h8","B","Cannon2"],["i8","",""]],
                        [["a9","",""],["b9","",""],["c9","",""],["d9","",""],["e9","B","General"],["f9","",""],["g9","",""],["h9","",""],["i9","",""]],
                        [["a10","B","Chariot1"],["b10","B","Elephant1"],["c10","B","Horse1"],["d10","B","Guard1"],["e10","", ""],["f10","B","Guard2"],["g10","B","Horse2"],["h10","B","Elephant2"],["i10","B","Chariot2"]]
                      ]
        self._turn = "B"
        self._move_translator = {'a1':[0,0],'b1':[0,1],'c1':[0,2],'d1':[0,3],'e1':[0,4],'f1':[0,5],'g1':[0,6],'h1':[0,7],'i1':[0,8],
                                 'a2':[1,0],'b2':[1,1],'c2':[1,2],'d2':[1,3],'e2':[1,4],'f2':[1,5],'g2':[1,6],'h2':[1,7],'i2':[1,8],
                                 'a3':[2,0],'b3':[2,1],'c3':[2,2],'d3':[2,3],'e3':[2,4],'f3':[2,5],'g3':[2,6],'h3':[2,7],'i3':[2,8],
                                 'a4':[3,0],'b4':[3,1],'c4':[3,2],'d4':[3,3],'e4':[3,4],'f4':[3,5],'g4':[3,6],'h4':[3,7],'i4':[3,8],
                                 'a5':[4,0],'b5':[4,1],'c5':[4,2],'d5':[4,3],'e5':[4,4],'f5':[4,5],'g5':[4,6],'h5':[4,7],'i5':[4,8],
                                 'a6':[5,0],'b6':[5,1],'c6':[5,2],'d6':[5,3],'e6':[5,4],'f6':[5,5],'g6':[5,6],'h6':[5,7],'i6':[5,8],
                                 'a7':[6,0],'b7':[6,1],'c7':[6,2],'d7':[6,3],'e7':[6,4],'f7':[6,5],'g7':[6,6],'h7':[6,7],'i7':[6,8],
                                 'a8':[7,0],'b8':[7,1],'c8':[7,2],'d8':[7,3],'e8':[7,4],'f8':[7,5],'g8':[7,6],'h8':[7,7],'i8':[7,8],
                                 'a9':[8,0],'b9':[8,1],'c9':[8,2],'d9':[8,3],'e9':[8,4],'f9':[8,5],'g9':[8,6],'h9':[8,7],'i9':[8,8],
                                 'a10':[9,0],'b10':[9,1],'c10':[9,2],'d10':[9,3],'e10':[9,4],'f10':[9,5],'g10':[9,6],'h10':[9,7],'i10':[9,8]
                                 }
        self._piece_tracker_red = [[1,4], [0,3], [0,5], [0,0], [0,8], [0,1], [0,6], [0,2], [0,7], [3,0], [3,2], [3,4], [3,6], [3,8]]
        self._piece_tracker_translator = {'General': 0, 'Guard1': 1, 'Guard2': 2, 'Chariot1': 3, 'Chariot2': 4, 'Elephant1': 5, 'Elephant2': 6, 'Horse1': 7, 'Horse2': 8, 'Soldier1': 9, 'Soldier2': 10, 'Soldier3': 11, 'Soldier4': 12, 'Soldier5': 13}
        self._piece_tracker_blue = [[8,4], [9,3], [9,5], [9,0], [9,8], [9,1], [9,6], [9,2], [9,7], [6,0], [6,2], [6,4], [6,6], [6,8]]
        self._piece_tracker_translator = {'General': 0, 'Guard1': 1, 'Guard2': 2, 'Chariot1': 3, 'Chariot2': 4, 'Elephant1': 5, 'Elephant2': 6, 'Horse1': 7, 'Horse2': 8, 'Soldier1': 9, 'Soldier2': 10, 'Soldier3': 11, 'Soldier4': 12, 'Soldier5': 13}

    def update_game_state(self):
        """Updates game state depending on current state of the board"""
        # Get current location of red general 
        rg = self._piece_tracker_red[0]
        
        # Get current location of blue general 
        bg = self._piece_tracker_blue[0]
       
        # Determine all legal moves for red general from a list of possible moves
        red_possible_moves = [
                                [rg[0], rg[1]], # current location
                                [rg[0] - 1, rg[1]], # up
                                [rg[0] + 1, rg[1]], # down
                                [rg[0], rg[1] + 1], # right
                                [rg[0], rg[1] - 1], # left
                                [rg[0] - 1, rg[1] + 1], # up + right
                                [rg[0] - 1, rg[1] - 1], # up + left
                                [rg[0] + 1, rg[1] + 1], # down + right
                                [rg[0] + 1, rg[1] - 1]  # down + left
                             ]

        # legal moves
        rg_legal_moves = []
        for move in red_possible_moves:
            # check if move is legal
            legal = self.is_legal(rg, move)
            if legal == True:
                rg_legal_moves.append(move)
        # print("Red General Legal Moves:")
        # print(rg_legal_moves)
        
        # Determine all legal moves for blue general from a list of possible moves
        blue_possible_moves = [
                                [bg[0], bg[1]], # current location
                                [bg[0] - 1, bg[1]], # up
                                [bg[0] + 1, bg[1]], # down
                                [bg[0], bg[1] + 1], # right
                                [bg[0], bg[1] - 1], # left
                                [bg[0] - 1, bg[1] + 1], # up + right
                                [bg[0] - 1, bg[1] - 1], # up + left
                                [bg[0] + 1, bg[1] + 1], # down + right
                                [bg[0] + 1, bg[1] - 1]  # down + left
                             ]
        
        # legal moves
        bg_legal_moves = []
        for move in blue_possible_moves:
            # check if move is legal
            legal = self.is_legal(bg, move)
            if (legal == True):
                bg_legal_moves.append(move)
        
        # print("Blue General Legal Moves")
        # print(bg_legal_moves)
        
        # Go through current location and through each legal move for red general and determine if all of those moves put the general in check. If every move puts general in check, set game state to "BLUE_WON"
        # To get if general is in check at any of the legal locations, iterate through each legal general move. For each legal general move, iterate through each opponent piece and see if the piece can legally capture the general.
        # If an opponent's piece can capture the general, then it is in check.
        # If not_check list is empty, then the general is in checkmate at the opposing player has won.
        # Update game's state to "BLUE_WON"
        not_check = []
        for move in rg_legal_moves:
            verdict = False 
            # Go through every piece on blue team 
            for piece in self._piece_tracker_blue:
                if self.is_legal(piece, move) == True:
                    verdict = True
                    
            if verdict == False:
                not_check.append(move)
                
        # print("Red General can move here: ")
        # print(not_check)
        if len(not_check) == 0:
            self._state = "BLUE_WON"
        
         # Go through current location and through each legal move for red general and determine if all of those moves put the general in check. If every move puts general in check, set game state to "BLUE_WON"
        # To get if general is in check at any of the legal locations, iterate through each legal general move. For each legal general move, iterate through each opponent piece and see if the piece can legally capture the general.
        # If an opponent's piece can capture the general, then it is in check.
        # If not_check list is empty, then the general is in checkmate at the opposing player has won.
        # update game's state to "RED_WON"
        not_check = []
        for move in bg_legal_moves:
            verdict = False 
            for piece in self._piece_tracker_red:
                if self.is_legal(piece, move) == True:
                    verdict = True
            
            if verdict == False:
                not_check.append(move)
                    
        # print("Blue General can move here:")
        # print(not_check)
        if len(not_check) == 0:
            self._state = "RED_WON"
        
        # If neither general is in check, set game state to "UNFINISHED"
        self._state = "UNFINISHED"
        
    def get_game_state(self):
        """returns a value depending on the game state"""
        return self._state
        
    def is_in_check(self, player):
        """Returns True if a player's general is in check, but False otherwise"""
        # First, determine the current position of the player's general 
        if player == 'red':
            red_general = self._piece_tracker_red[0]
            # Second, determine if any of opponent's pieces can legally take the general at its current position
            # for piece in opposing piece tracker, check if (move_from: piece current location) to (move_to: general current location) is legal
            # If so, then General is in check and the method returns True
            for piece in self._piece_tracker_blue:
                verdict = self.is_legal(piece, red_general)
                if verdict == True:
                    return True

        if player == 'blue':
            blue_general = self._piece_tracker_blue[0]
            
            # Second, determine if any of opponent's pieces can legally take the general at its current position
            # for piece in opposing piece tracker, check if (move_from: piece current location) to (move_to: general current location) is legal
            # If so, then General is in check and the method returns True
            for piece in self._piece_tracker_red:
                verdict = self.is_legal(piece, blue_general)
                if verdict == True:
                    return True 

        return False
             
    def make_move(self, move_from, move_to):
        """Allows player to make a move and updates game's state"""
        # PRELIMINARY CHECK: Check if the player is passing turn. Check if move_from equals move_to.
        # If so, simply switch turns. Return True
        if move_from[0] == move_to[0] and move_from[1] == move_to[1]:
            # Switch Turns
            if self._turn == "B":
                self._turn = "R"
            else:
                self._turn = "B"

            # End Turn 
            return True
        
        # First, translate move_from into usable reference
        # board format: board[i][j], i is the row, j is the column
        board_from = self._move_translator[move_from]
        board_to   = self._move_translator[move_to]

        
        # CHECK 1: Check if move_from space is empty, if so return False
        # self._board[board[0]][board[1]][1] references the color (i.e. 'R' or 'B')
        if self._board[board_from[0]][board_from[1]][1] == "":
            print("There's no piece there, dude!")
            return False
        
        # CHECK 2: Check if move_from piece belongs to player making the move, return False if not 
        # self._board[board[0]][board[1]][1] references the color (i.e. 'R' or 'B')
        if self._turn != self._board[board_from[0]][board_from[1]][1]:
            print("It's " + self._turn + " team's turn")
            return False
        
        # CHECK 3: check if move_to piece also belongs to player making the move, if so return False
        if self._turn == self._board[board_to[0]][board_to[1]][1]:
            print("Another one of your pieces is already there!")
            return False
            
        # CHECK 4: check if move is legal. If move is not legal, return False 
        legal_move = self.is_legal(board_from, board_to) 
        if legal_move == False: 
            return False
        
        # CHECK 5: check if the game has already been won 
        if self._state == "FINISHED":
            print("The game's already over, sorry!")
            return False
            
        # If everything checks out, make move, remove captured piece, update game state, update turn, return True
        # Make move and remove capture piece
        player = self._board[board_from[0]][board_from[1]][1]
        piece  = self._board[board_from[0]][board_from[1]][2]
        self._board[board_to[0]][board_to[1]][1] = player       # New Space: replace player 
        self._board[board_to[0]][board_to[1]][2] = piece        # New Space: replace piece
        
        self._board[board_from[0]][board_from[1]][1] = ""       # Old Space: replace player
        self._board[board_from[0]][board_from[1]][2] = ""       # Old Space: replace player
        
        # update game state: Check if opposing player's general is in checkmate. 
        self.update_game_state()
        
        # update turn
        if self._turn == "B":
            self._turn = "R"
        else:
            self._turn = "B" 
        
        # return True 
        return True
            
    def in_palace(self, location):
        """Checks if a piece is in a palace, either its own or opposing palace"""
        # Check if location matches a red_palace space. If match found, return True 
        red_palace = [[0,3], [0,4], [0,5], [1,3], [1,4], [1,5], [2,3], [2,4], [2,5]]
        for space in red_palace:
            if location[0] == space[0] and location[1] == space[1]:
                return True
        
        # Checks if location matches a blue_palace space. If match found, return False
        blue_palace = [[9,3], [9,4], [9,5], [8,3], [8,4], [8,5], [7,3], [7,4], [7,5]]
        for space in blue_palace:
            if location[0] == space[0] and location[1] == space[1]:
                return True
                
        # If no matches found, it's not in a palace, return false
        return False     
        
    def is_legal(self, move_from, move_to):
        """Returns True if a move is legal, False otherwise"""
        # First, determine the type of piece and the player 
        player = self._board[move_from[0]][move_from[1]][1]
        piece = self._board[move_from[0]][move_from[1]][2]
        
        if (piece == "Guard1") or (piece == "Guard2"): 
            answer = self.guard(move_from, move_to, player)
            return answer 
        
        if (piece == "Horse1") or (piece == "Horse2"):
            answer = self.horse(move_from, move_to, player)
            return answer 

        if (piece == "Elephant1") or (piece == "Elephant2"):
           answer = self.elephant(move_from, move_to, player)
           return answer 
            
        if (piece == "Chariot1") or (piece == "Chariot2"):
            answer = self.chariot(move_from, move_to, player)
            return answer 
            
        if (piece == "Cannon1") or (piece == "Cannon2"):
            answer = self.cannon(move_from, move_to, player)
            return answer 
            
        if (piece == "Soldier1") or (piece == "Soldier2") or (piece == "Soldier3") or (piece == "Soldier4"):
           answer = self.soldier(move_from, move_to, player)
           return answer 
            
        if (piece == "General"):
            answer = self.general(move_from, move_to, player)
            return answer
        
    # Guard Pieces: moves one step per turn along marked lines ONLY in the palace.
    def guard(self, move_from, move_to, player):
        """Returns True if guard move is legal, false otherwise"""
        # list of all possible moves based on piece type and board state 
        possible_moves = []
        
        # Add all possible moves into possible_moves list 
        if player == "R":
            # 01. move forward one step
            move_location = [move_from[0] + 1, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            # move forward one step: Check if move is in palace and a red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)
                
            # 02. move backwards one step
            move_location = [move_from[0] - 1, move_from[1]]
            # Catch list index out of range errors
            if move_location[0] > 0:
                move_value = self._board[move_location[0]][move_location[1]]
                # Move one step backwards if move is in palace and a red piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "R":
                    possible_moves.append(move_location)
                    
            # 03. move right one step
            move_location = [move_from[0], move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move one step right if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)
            
            # 04. move left one step
            move_location = [move_from[0], move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move left one step if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)
                
            # 05. move diagonally up-right
            move_location = [move_from[0] + 1, move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up-right if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value != "R":
                possible_moves.append(move_location)
                
            # 06. move diagonally up-left
            move_location = [move_from[0] + 1, move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up-left if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)

            # 07. move diagonally down-right
            move_location = [move_from[0] - 1, move_from[1] + 1]
            if move_location[0] > 0:
                move_value = self._board[move_location[0]][move_location[1]]
                # move up-left if move is in palace and red piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "R":
                    possible_moves.append(move_location)

            # 08. move diagonally down-left
            move_location = [move_from[0] - 1, move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up-left if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)
                            
        else:
            # 01. move forward one step
            move_location = [move_from[0] - 1, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            # move forward one step: Check if move is in palace and a blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)
                
            # 02. move backwards one step
            move_location = [move_from[0] + 1, move_from[1]]
            # Catch list index out of range errors
            if move_location[0] < 9:
                move_value = self._board[move_location[0]][move_location[1]]
                # Move one step backwards if move is in palace and blue piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "B":
                    possible_moves.append(move_location)
            
            # 03. move right one step
            move_location = [move_from[0], move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move one step right if move is in palace and blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)
                
            # 04. move left one step
            move_location = [move_from[0], move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move left one step if move is in palace and blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)
                
            # 05. move diagonally up-right
            move_location = [move_from[0] - 1, move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up right if move is in palace and blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)
                
            # 06. move diagonally up-left
            move_location = [move_from[0] - 1, move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up left if move is in palace and blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)
                    
            # 07. move diagonally down-right
            move_location = [move_from[0] + 1, move_from[1] + 1]
            # Check if move is within range
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                # move up left if move is in palace and blue piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "B":
                    possible_moves.append(move_location)
            
            # 08. move diagonally down-left
            move_location = [move_from[0] + 1, move_from[1] - 1]
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                # move up left if move is in palace and blue piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "B":
                    possible_moves.append(move_location)
        
        # compare move_to index to possible moves list. If there's a match, return True. 
        for move in possible_moves:
            if move_to == move:
                return True
        # If no match was found, move was not legal, return False
        return False  
    
    # Horse Piece: moves one step orthogonally then one step diagonally outward. No jumping, can be blocked.
    def horse(self, move_from, move_to, player):
        """Returns true if horse move is legal, false otherwise"""
        possible_moves = []
        
        # Add all possible moves into possible_moves list 
        if player == "R":
            # 01. STEP UP
            step_forward = []
            move_location = [move_from[0] + 1, move_from[1]]
            # Check for off the board moves
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_forward = move_location

            # Now move diagonally right-left from step_forward 
            # up-right
            move_location = [step_forward[0] + 1, step_forward[1] + 1]
            # Check if off board
            if move_location[1] < 9:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] != "R":
                    possible_moves.append(move_location)

            # up-left
            move_location = [step_forward[0] + 1, step_forward[1] - 1]
            # Check if off board
            if move_location[1] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] != "R":
                    possible_moves.append(move_location)

            # 02. STEP DOWN
            step_down = []
            move_location = [move_from[0] - 1, move_from[1]]
            # Check for off the board moves
            if move_location[0] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_down = move_location
            
            # Now move diagonally from step_down
            # down-right
            if step_down != []:
                move_location = [step_down[0] - 1, step_down[1] + 1]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # down-left
            if step_down != []:
                move_location = [step_down[0] - 1, step_down[1] - 1]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # 03. STEP LEFT
            step_left = []
            move_location = [move_from[0], move_from[1] - 1]
            # Check for off the board moves
            if move_location[0] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_left = move_location

            # Now move diagonally up-down from step_left
            # left-up
            if step_left != []:
                move_location = [step_left[0] + 1, step_left[1] - 1]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # left-down
            if step_left != []:
                move_location = [step_left[0] - 1, step_left[1] - 1]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # 04. STEP RIGHT
            step_right = []
            move_location = [move_from[0], move_from[1] + 1]
            # Check for off the board moves
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_right = move_location

            # Now move diagonally up-down from step_right
            # right-up
            if step_right != []:
                move_location = [step_right[0] + 1, step_right[1] + 1]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # right-down
            if step_right != []:
                move_location = [step_right[0] - 1, step_right[1] + 1]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)
                    
        else:
            # 01: STEP UP
            move_location = [move_from[0] - 1, move_from[1]]
            # Check for off the board moves
            if move_location[0] > 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_forward = move_location

            # Now move diagonally right-left from step_forward 
            # up-right
            move_location = [step_forward[0] - 1, step_forward[1] + 1]
            # Check if off board
            if move_location[1] < 9:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] != "B":
                    possible_moves.append(move_location)

            # up-left
            move_location = [step_forward[0] - 1, step_forward[1] - 1]
            # Check if off board
            if move_location[1] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] != "B":
                    possible_moves.append(move_location)

            # 02: STEP DOWN
            step_down = None
            move_location = [move_from[0] + 1, move_from[1]]
            # Check for off the board moves
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_down = move_location
            
            # Now move diagonally from step_down
            # down-right
            if step_down != None:
                move_location = [step_down[0] + 1, step_down[1] + 1]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # down-left
            if step_down != None:
                move_location = [step_down[0] + 1, step_down[1] - 1]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # STEP LEFT:
            step_left = []
            move_location = [move_from[0], move_from[1] - 1]
            # Check for off the board moves
            if move_location[0] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_left = move_location

            # Now move diagonally up-down from step_left
            # left-up
            if step_left != []:
                move_location = [step_left[0] - 1, step_left[1] - 1]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # left-down
            if step_left != []:
                move_location = [step_left[0] + 1, step_left[1] - 1]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # STEP RIGHT:
            step_right = []
            move_location = [move_from[0], move_from[1] + 1]
            # Check for off the board moves
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_right = move_location


            # Now move diagonally up-down from step_right
            # right-up
            if step_right != []:
                move_location = [step_right[0] - 1, step_right[1] + 1]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # right-down
            if step_right != []:
                move_location = [step_right[0] + 1, step_right[1] + 1]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)
         
        # If there's a possible move, return True. False otherwise 
        for move in possible_moves:
            if move_to == move:
                return True
        # If no match was found, move was not legal, return False
        return False  
    
    # Elephant Piece: moves one step orthogonally then two steps diagonally outward. No jumping, can be blocked.
    def elephant(self, move_from, move_to, player):
        """Returns true if elephant move is legal, false otherwise"""
        possible_moves = []
        
        if player == "R":
            # 01. STEP UP
            step_forward = []
            move_location = [move_from[0] + 1, move_from[1]]
            # Check for off the board moves
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_forward = move_location

            # Now move diagonally right-left from step_forward 
            # up-right
            move_location = [step_forward[0] + 2, step_forward[1] + 2]
            # Check if off board
            if move_location[1] < 9:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] != "R":
                    possible_moves.append(move_location)

            # up-left
            move_location = [step_forward[0] + 2, step_forward[1] - 2]
            # Check if off board
            if move_location[1] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] != "R":
                    possible_moves.append(move_location)

            # 02. STEP DOWN
            step_down = []
            move_location = [move_from[0] - 1, move_from[1]]
            # Check for off the board moves
            if move_location[0] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_down = move_location
            
            # Now move diagonally from step_down
            # down-right
            if step_down != []:
                move_location = [step_down[0] - 2, step_down[1] + 2]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # down-left
            if step_down != []:
                move_location = [step_down[0] - 2, step_down[1] - 2]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # 03. STEP LEFT
            step_left = []
            move_location = [move_from[0], move_from[1] - 1]
            # Check for off the board moves
            if move_location[0] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_left = move_location

            # Now move diagonally up-down from step_left
            # left-up
            if step_left != []:
                move_location = [step_left[0] + 2, step_left[1] - 2]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # left-down
            if step_left != []:
                move_location = [step_left[0] - 2, step_left[1] - 2]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # 04. STEP RIGHT
            step_right = []
            move_location = [move_from[0], move_from[1] + 1]
            # Check for off the board moves
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_right = move_location

            # Now move diagonally up-down from step_right
            # right-up
            if step_right != []:
                move_location = [step_right[0] + 2, step_right[1] + 2]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)

            # right-down
            if step_right != []:
                move_location = [step_right[0] - 2, step_right[1] + 2]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "R":
                        possible_moves.append(move_location)
                    
        else: 
            # 01: STEP UP
            move_location = [move_from[0] - 1, move_from[1]]
            # Check for off the board moves
            if move_location[0] > 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_forward = move_location

            # Now move diagonally right-left from step_forward 
            # up-right
            move_location = [step_forward[0] - 2, step_forward[1] + 2]
            # Check if off board
            if move_location[1] < 9:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] != "B":
                    possible_moves.append(move_location)

            # up-left
            move_location = [step_forward[0] - 2, step_forward[1] - 2]
            # Check if off board
            if move_location[1] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] != "B":
                    possible_moves.append(move_location)

            # 02: STEP DOWN
            step_down = None
            move_location = [move_from[0] + 1, move_from[1]]
            # Check for off the board moves
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_down = move_location
            
            # Now move diagonally from step_down
            # down-right
            if step_down != None:
                move_location = [step_down[0] + 2, step_down[1] + 2]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # down-left
            if step_down != None:
                move_location = [step_down[0] + 2, step_down[1] - 2]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # STEP LEFT:
            step_left = []
            move_location = [move_from[0], move_from[1] - 1]
            # Check for off the board moves
            if move_location[0] >= 0:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_left = move_location

            # Now move diagonally up-down from step_left
            # left-up
            if step_left != []:
                print(step_left)
                move_location = [step_left[0] - 2, step_left[1] - 2]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # left-down
            if step_left != []:
                move_location = [step_left[0] + 2, step_left[1] - 2]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # STEP RIGHT:
            step_right = []
            move_location = [move_from[0], move_from[1] + 1]
            # Check for off the board moves
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                if move_value[1] == "":
                    step_right = move_location


            # Now move diagonally up-down from step_right
            # right-up
            if step_right != []:
                move_location = [step_right[0] - 2, step_right[1] + 2]
                # Check if off board
                if move_location[1] < 9:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)

            # right-down
            if step_right != []:
                move_location = [step_right[0] + 2, step_right[1] + 2]
                # Check if off board
                if move_location[1] >= 0:
                    move_value = self._board[move_location[0]][move_location[1]]
                    if move_value[1] != "B":
                        possible_moves.append(move_location)
         
            
        # If there's a possible move, return True. False otherwise 
        for move in possible_moves:
            if move_to == move:
                return True
        # If no match was found, move was not legal, return False
        return False  
    
    # Chariot Piece: moves in a straight line either horizontally or vertically. May move along diagonal lines inside either palace. 
    def chariot(self, move_from, move_to, player):
        """Returns true if chariot move is legal, false otherwise"""
        possible_moves = []
        
        if player == "R":
            # 01. Move Up 
            steps = 1
            move_location = [move_from[0] + steps, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            while move_location[0] < 10 and move_value == "":
                possible_moves.append(move_location)
                steps += 1
                move_location = [move_from[0] + steps, move_from[1]]
                move_value = self._board[move_location[0]][move_location[1]]
            if move_location[0] < 10 and move_value == "B":
                possible_moves.append(move_location)
            
            # 02. Move Down 
            steps = 1
            move_location = [move_from[0] - steps, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            while move_location[0] >= 0 and move_value == "":
                possible_moves.append(move_location)
                steps += 1
                move_location = [move_from[0] - steps, move_from[1]]
                move_value = self._board[move_location[0]][move_location[1]]
            if move_location[0] >= 0 and move_value == "B":
                possible_moves.append(move_location)
                
            # 03. Move Left
            steps = 1
            move_location = [move_from[0], move_from[1] - steps]
            move_value = self._board[move_location[0]][move_location[1]]
            while move_location[1] >= 0 and move_value == "":
                possible_moves.append(move_location)
                steps += 1
                move_location = [move_from[0], move_from[1] - steps]
                move_value = self._board[move_location[0]][move_location[1]]
            if move_location[1] >= 0 and move_value == "B":
                possible_moves.append(move_location)
                
            # 04. Move Right 
            steps = 1
            if move_from[1] + steps < 9:
                move_location = [move_from[0], move_from[1] + steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while move_location[1] < 9 and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0], move_from[1] + steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if move_location[1] < 10 and move_value == "B":
                    possible_moves.append(move_location)
            
            if self.in_palace(move_from) == True:
                # 05. Move up-right 
                steps = 1
                move_location = [move_from[0] + steps, move_from[1] + steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while self.in_palace(move_location) == True and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] + steps, move_from[1] + steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if self.in_palace(move_location) == True and move_value == "B":
                    possible_moves.append(move_location)
                    
                # 06. Move up-left 
                steps = 1
                move_location = [move_from[0] + steps, move_from[1] - steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while self.in_palace(move_location) == True and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] + steps, move_from[1] - steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if self.in_palace(move_location) == True and move_value == "B":
                    possible_moves.append(move_location)
                    
                # 07. Move down-right 
                steps = 1
                move_location = [move_from[0] - steps, move_from[1] + steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while self.in_palace(move_location) == True and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] - steps, move_from[1] + steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if self.in_palace(move_location) == True and move_value == "B":
                    possible_moves.append(move_location)
                    
                # 08. Move down-left 
                steps = 1
                move_location = [move_from[0] - steps, move_from[1] - steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while self.in_palace(move_location) == True and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] - steps, move_from[1] - steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if self.in_palace(move_location) == True and move_value == "B":
                    possible_moves.append(move_location)
                
        else: 
            # 01. Move Up 
            steps = 1
            move_location = [move_from[0] - steps, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            while move_location[0] >= 0 and move_value == "":
                possible_moves.append(move_location)
                steps += 1
                move_location = [move_from[0] - steps, move_from[1]]
                move_value = self._board[move_location[0]][move_location[1]]
            if move_location[0] >= 0 and move_value == "R":
                possible_moves.append(move_location)
            
            # 02. Move Down 
            steps = 1
            if move_from[0] + steps < 10:
                move_location = [move_from[0] + steps, move_from[1]]
                move_value = self._board[move_location[0]][move_location[1]]
                while move_location[0] < 10 and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] + steps, move_from[1]]
                    move_value = self._board[move_location[0]][move_location[1]]
                if move_location[0] < 10 and move_value == "R":
                    possible_moves.append(move_location)
                
            # 03. Move Left
            if move_from[0] - steps >= 0:
                steps = 1
                move_location = [move_from[0], move_from[1] - steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while move_location[1] >= 0 and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0], move_from[1] - steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if move_location[1] >= 0 and move_value == "R":
                    possible_moves.append(move_location)
                
            # 04. Move Right 
            steps = 1
            if move_from[0] + steps < 10:
                move_location = [move_from[0], move_from[1] + steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while move_location[1] < 10 and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0], move_from[1] + steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if move_location[1] < 10 and move_value == "R":
                    possible_moves.append(move_location)
            
            if self.in_palace(move_from) == True:
                # 05. Move up-right 
                steps = 1
                move_location = [move_from[0] - steps, move_from[1] + steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while self.in_palace(move_location) == True and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] - steps, move_from[1] + steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if self.in_palace(move_location) == True and move_value == "R":
                    possible_moves.append(move_location)
                    
                # 06. Move up-left 
                steps = 1
                move_location = [move_from[0] - steps, move_from[1] - steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while self.in_palace(move_location) == True and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] - steps, move_from[1] - steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if self.in_palace(move_location) == True and move_value == "R":
                    possible_moves.append(move_location)
                    
                # 07. Move down-right 
                steps = 1
                move_location = [move_from[0] + steps, move_from[1] + steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while self.in_palace(move_location) == True and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] + steps, move_from[1] + steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if self.in_palace(move_location) == True and move_value == "R":
                    possible_moves.append(move_location)
                    
                # 08. Move down-left 
                steps = 1
                move_location = [move_from[0] + steps, move_from[1] - steps]
                move_value = self._board[move_location[0]][move_location[1]]
                while self.in_palace(move_location) == True and move_value == "":
                    possible_moves.append(move_location)
                    steps += 1
                    move_location = [move_from[0] + steps, move_from[1] - steps]
                    move_value = self._board[move_location[0]][move_location[1]]
                if self.in_palace(move_location) == True and move_value == "R":
                    possible_moves.append(move_location)
            
        # If there's a possible move, return True. False otherwise 
        for move in possible_moves:
            if move_to == move:
                return True
        # If no match was found, move was not legal, return False
        return False  
    
    # Cannon Piece: moves by jumping over exactly one piece. May move or capture diagonally along diagonal lines in either palace, provided there is an intervening piece in the center.
    def cannon(self, move_from, move_to, player):
        """Returns true if cannon move is legal, false otherwise"""
        possible_moves = []
        
        if player == "R":
            # 01. Move Up 
            steps = 1
            jump_piece = ""
            capture = ""
            move_location = [move_from[0] + steps, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            while move_location[0] < 9:
                
                # Check for valid moves (captures) 
                if jump_piece != "" and capture == "" and move_value[2] != "" and move_value[2] != "Cannon1" and move_value[2] != "Cannon2" and move_value[1] != "R":
                    capture = move_value[2]
                    possible_moves.append(move_location)
                    
                if jump_piece != "" and move_value[2] == "" and capture == "":
                    possible_moves.append(move_location)
                
                # Set Jump Piece 
                if move_value[2] != "" and move_value[2] != "Cannon1" and move_value[2] != "Cannon2" and jump_piece == "":
                    jump_piece = move_value[2]
                    
                # Iterate to next space 
                steps += 1
                move_location = [move_from[0] + steps, move_from[1]]
                move_value = self._board[move_location[0]][move_location[1]]
            
            # 02. Move Down 
            steps = 1
            jump_piece = ""
            capture = ""
            move_location = [move_from[0] - steps, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            while move_location[0] > 0:
                
                # Check for valid moves (captures) 
                if jump_piece != "" and capture == "" and move_value[2] != "" and move_value[2] != "Cannon1" and move_value[2] != "Cannon2" and move_value[1] != "R":
                    capture = move_value[2]
                    possible_moves.append(move_location)
                    
                # Check for valid moves (non-captures)
                if jump_piece != "" and move_value[2] == "" and capture == "":
                    possible_moves.append(move_location)
                
                # Set Jump Piece 
                if move_value[2] != "" and move_value[2] != "Cannon1" and move_value[2] != "Cannon2" and jump_piece == "":
                    jump_piece = move_value[2]
                    
                # Iterate to next space 
                steps += 1
                move_location = [move_from[0] - steps, move_from[1]]
                move_value = self._board[move_location[0]][move_location[1]]
            
            # 03. Move Left
            steps = 1
            jump_piece = ""
            capture = ""
            move_location = [move_from[0], move_from[1] - steps]
            move_value = self._board[move_location[0]][move_location[1]]
            while move_location[1] > 0:
                
                # Check for valid moves (captures) 
                if jump_piece != "" and capture == "" and move_value[2] != "" and move_value[2] != "Cannon1" and move_value[2] != "Cannon2" and move_value[1] != "R":
                    capture = move_value[2]
                    possible_moves.append(move_location)
                    
                # Check for valid moves (non-captures)
                if jump_piece != "" and move_value[2] == "" and capture == "":
                    possible_moves.append(move_location)
                
                # Set Jump Piece 
                if move_value[2] != "" and move_value[2] != "Cannon1" and move_value[2] != "Cannon2" and jump_piece == "":
                    jump_piece = move_value[2]
                    
                # Iterate to next space 
                steps += 1
                move_location = [move_from[0], move_from[1] - steps] 
                move_value = self._board[move_location[0]][move_location[1]]
            
            # 04. Move Right 
            steps = 1
            jump_piece = ""
            capture = ""
            move_location = [move_from[0], move_from[1] + steps]
            move_value = self._board[move_location[0]][move_location[1]]
            while move_from[1] + steps < 8:
                
                # Check for valid moves (captures) 
                if jump_piece != "" and capture == "" and move_value[2] != "" and move_value[2] != "Cannon1" and move_value[2] != "Cannon2" and move_lvalue[1] != "R":
                    capture = move_value[2]
                    possible_moves.append(move_location)
                    
                # Check for valid moves (non-captures)
                if jump_piece != "" and move_value[2] == "" and capture == "":
                    possible_moves.append(move_location)
                
                # Set Jump Piece 
                if move_value[2] != "" and move_value[2] != "Cannon1" and move_value[2] != "Cannon2" and jump_piece == "":
                    jump_piece = move_value[2]
                    
                # Iterate to next space 
                steps += 1
                move_location = [move_from[0], move_from[1] + steps]
                move_value = self._board[move_location[0]][move_location[1]]
            
            # IN PALACE 
            # 05. Move up-right 
            if self.in_palace(move_from) == True:
                if self.in_palace([move_from[0] + 2, move_from[1] + 2]) == True and self._board[1][4][2] != "":
                    possible_moves.append([move_from[0] + 2, move_from[1] + 2])
            
            # 06. Move up-left 
            if self.in_palace(move_from) == True:
                if self.in_palace([move_from[0] + 2, move_from[1] - 2]) == True and self._board[1][4][2] != "":
                    possible_moves.append([move_from[0] + 2, move_from[1] - 2])
            
            # 07. Down-right
            if self.in_palace(move_from) == True:
                if self.in_palace([move_from[0] - 2, move_from[1] + 2]) == True and self._board[1][4][2] != "":
                    possible_moves.append([move_from[0] - 2, move_from[1] + 2]) 
            
            # 08. Down-left 
            if self.in_palace(move_from) == True:
                if self.in_palace([move_from[0] - 2, move_from[1] - 2]) == True and self._board[1][4][2] != "":
                    possible_moves.append([move_from[0] - 2, move_from[1] - 2]) 
        else: 
            # 01. Move Up 
            steps = 1
            jump_piece = ""
            capture = ""
            move_location = self._board[move_from[0] - steps][move_from[1]]
            while move_from[0] - steps > 0:
                
                # Check for valid moves (captures) 
                if jump_piece != "" and capture == "" and move_location[2] != "" and move_location[2] != "Cannon1" and move_location[2] != "Cannon2" and move_location[1] != "R":
                    capture = move_location[2]
                    possible_moves.append(move_location)
                    
                if jump_piece != "" and move_loction[2] == "" and capture == "":
                    possible_moves.append(move_location)
                
                # Set Jump Piece 
                if move_location[2] != "" and move_location[2] != "Cannon1" and move_location[2] != "Cannon2" and jump_piece == "":
                    jump_piece = move_location[2]
                    
                # Iterate to next space 
                steps += 1
                move_location = self._board[move_from[0] - steps][move_from[1]]
            
            # 02. Move Down 
            steps = 1
            jump_piece = ""
            capture = ""
            move_location = self._board[move_from[0] + steps][move_from[1]]
            while move_from[0] + steps > 0:
                
                # Check for valid moves (captures) 
                if jump_piece != "" and capture == "" and move_location[2] != "" and move_location[2] != "Cannon1" and move_location[2] != "Cannon2" and move_location[1] != "R":
                    capture = move_location[2]
                    possible_moves.append(move_location)
                    
                # Check for valid moves (non-captures)
                if jump_piece != "" and move_loction[2] == "" and capture == "":
                    possible_moves.append(move_location)
                
                # Set Jump Piece 
                if move_location[2] != "" and move_location[2] != "Cannon1" and move_location[2] != "Cannon2" and jump_piece == "":
                    jump_piece = move_location[2]
                    
                # Iterate to next space 
                steps += 1
                move_location = self._board[move_from[0] + steps][move_from[1]]
            
            # 03. Move Left
            steps = 1
            jump_piece = ""
            capture = ""
            move_location = self._board[move_from[0]][move_from[1] - steps]
            while move_from[1] - steps > 0:
                
                # Check for valid moves (captures) 
                if jump_piece != "" and capture == "" and move_location[2] != "" and move_location[2] != "Cannon1" and move_location[2] != "Cannon2" and move_location[1] != "R":
                    capture = move_location[2]
                    possible_moves.append(move_location)
                    
                # Check for valid moves (non-captures)
                if jump_piece != "" and move_loction[2] == "" and capture == "":
                    possible_moves.append(move_location)
                
                # Set Jump Piece 
                if move_location[2] != "" and move_location[2] != "Cannon1" and move_location[2] != "Cannon2" and jump_piece == "":
                    jump_piece = move_location[2]
                    
                # Iterate to next space 
                steps += 1
                move_location = self._board[move_from[0]][move_from[1] - steps] 
            
            # 04. Move Right 
            steps = 1
            jump_piece = ""
            capture = ""
            move_location = self._board[move_from[0]][move_from[1] + steps]
            while move_from[1] + steps < 8:
                
                # Check for valid moves (captures) 
                if jump_piece != "" and capture == "" and move_location[2] != "" and move_location[2] != "Cannon1" and move_location[2] != "Cannon2" and move_location[1] != "R":
                    capture = move_location[2]
                    possible_moves.append(move_location)
                    
                # Check for valid moves (non-captures)
                if jump_piece != "" and move_loction[2] == "" and capture == "":
                    possible_moves.append(move_location)
                
                # Set Jump Piece 
                if move_location[2] != "" and move_location[2] != "Cannon1" and move_location[2] != "Cannon2" and jump_piece == "":
                    jump_piece = move_location[2]
                    
                # Iterate to next space 
                steps += 1
                move_location = self._board[move_from[0]][move_from[1] + steps]
            
            # IN PALACE 
            # 05. Move up-right 
            if self.in_palace(move_from) == True:
                if self.in_palace([move_from[0] - 2, move_from[1] + 2]) == True and self._board[8][4][2] != "":
                    possible_moves.append([move_from[0] + 2, move_from[1] + 2])
            
            # 06. Move up-left 
            if self.in_palace(move_from) == True:
                if self.in_palace([move_from[0] - 2, move_from[1] - 2]) == True and self._board[8][4][2] != "":
                    possible_moves.append([move_from[0] + 2, move_from[1] - 2])
            
            # 07. Down-right
            if self.in_palace(move_from) == True:
                if self.in_palace([move_from[0] + 2, move_from[1] + 2]) == True and self._board[8][4][2] != "":
                    possible_moves.append([move_from[0] - 2, move_from[1] + 2]) 
            
            # 08. Down-left 
            if self.in_palace(move_from) == True:
                if self.in_palace([move_from[0] + 2, move_from[1] - 2]) == True and self._board[8][4][2] != "":
                    possible_moves.append([move_from[0] - 2, move_from[1] - 2]) 
            
        # If there's a possible move, return True. False otherwise 
        for move in possible_moves:
            if move_to == move:
                return True
        # If no match was found, move was not legal, return False
        return False  
    
    # Soldier Piece: moves one step forward or sideways. Once they reach the end of the board they may only move sideways. May move one point diagonally when within enemy palace. 
    def soldier(self, move_from, move_to, player):
        """Returns true if soldier move is legal, false otherwise"""
        possible_moves = []
        
        if player == "R":
            # 01. MOVE FORWARD ONE STEP
            move_location = [move_from[0] + 1, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            # move forward one step: Check if red piece is not already there
            if move_value[1] != "R":
                possible_moves.append(move_location)
            
            # 02. MOVE RIGHT ONE STEP
            move_location = [move_from[0], move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move one step right if red piece is not already there
            if move_value[1] != "R":
                possible_moves.append(move_location)

            # 03. MOVE LEFT ONE STEP
            move_location = [move_from[0], move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move left one step if red piece is not already there
            if move_value[1] != "R":
                possible_moves.append(move_location)        
        else:
            # 01. MOVE FORWARD ONE STEP
            move_location = [move_from[0] - 1, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            # move forward one step: Check if blue piece is not already there
            if move_value[1] != "B":
                possible_moves.append(move_location)
                
            # 02. MOVE RIGHT ONE STEP
            move_location = [move_from[0], move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move one step right if  blue piece is not already there
            if move_value[1] != "B":
                possible_moves.append(move_location)

            # 03. MOVE LEFT ONE STEP
            move_location = [move_from[0], move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move left one step if blue piece is not already there
            if move_value[1] != "B":
                possible_moves.append(move_location)
                
        # If there's a possible move, return True. False otherwise 
        for move in possible_moves:
            if move_to == move:
                return True
        # If no match was found, move was not legal, return False
        return False  
    
    # General Piece 
    def general(self, move_from, move_to, player):
        """returns true if general move is legal, false otherwise"""
        possible_moves = []
        
        if player == "R":
            # 01. move forward one step
            move_location = [move_from[0] + 1, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            # move forward one step: Check if move is in palace and a red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)
            
            # 02. move backwards one step
            move_location = [move_from[0] - 1, move_from[1]]
            # Catch list index out of range errors
            if move_location[0] > 0:
                move_value = self._board[move_location[0]][move_location[1]]
                # Move one step backwards if move is in palace and a red piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "R":
                    possible_moves.append(move_location)

            # 03. move right one step
            move_location = [move_from[0], move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move one step right if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)

            # 04. move left one step
            move_location = [move_from[0], move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move left one step if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)

            # 05. move diagonally up-right
            move_location = [move_from[0] + 1, move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up-right if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value != "R":
                possible_moves.append(move_location)

            # 06. move diagonally up-left
            move_location = [move_from[0] + 1, move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up-left if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)

            # 07. move diagonally down-right
            move_location = [move_from[0] - 1, move_from[1] + 1]
            if move_location[0] > 0:
                move_value = self._board[move_location[0]][move_location[1]]
                # move up-left if move is in palace and red piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "R":
                    possible_moves.append(move_location)

            # 08. move diagonally down-left
            move_location = [move_from[0] - 1, move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up-left if move is in palace and red piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "R":
                possible_moves.append(move_location)

        else:
            # 01. move forward one step
            move_location = [move_from[0] - 1, move_from[1]]
            move_value = self._board[move_location[0]][move_location[1]]
            # move forward one step: Check if move is in palace and a blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)
            
            # 02. move backwards one step
            move_location = [move_from[0] + 1, move_from[1]]
            # Catch list index out of range errors
            if move_location[0] < 9:
                move_value = self._board[move_location[0]][move_location[1]]
                # Move one step backwards if move is in palace and blue piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "B":
                    possible_moves.append(move_location)

            # 03. move right one step
            move_location = [move_from[0], move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move one step right if move is in palace and blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)

            # 04. move left one step
            move_location = [move_from[0], move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # Move left one step if move is in palace and blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)

            # 05. move diagonally up-right
            move_location = [move_from[0] - 1, move_from[1] + 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up right if move is in palace and blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)

            # 06. move diagonally up-left
            move_location = [move_from[0] - 1, move_from[1] - 1]
            move_value = self._board[move_location[0]][move_location[1]]
            # move up left if move is in palace and blue piece is not already there
            if self.in_palace(move_location) == True and move_value[1] != "B":
                possible_moves.append(move_location)

            # 07. move diagonally down-right
            move_location = [move_from[0] + 1, move_from[1] + 1]
            # Check if move is within range
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                # move up left if move is in palace and blue piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "B":
                    possible_moves.append(move_location)

            # 08. move diagonally down-left
            move_location = [move_from[0] + 1, move_from[1] - 1]
            if move_location[0] < 10:
                move_value = self._board[move_location[0]][move_location[1]]
                # move up left if move is in palace and blue piece is not already there
                if self.in_palace(move_location) == True and move_value[1] != "B":
                    possible_moves.append(move_location)
        
        # If there's a possible move, return True. False otherwise 
        for move in possible_moves:
            if move_to == move:
                return True
        # If no match was found, move was not legal, return False
        return False  
        
    def print_board(self):
        """prints out the current state of the game board"""
        for space in range(0, len(self._board)):
            print(self._board[space])


