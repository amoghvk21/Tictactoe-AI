"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    l = []

    for row in board:
        for element in row:
            l.append(element)

    if (l == [EMPTY] * 9) or (l.count(X) <= l.count(O)):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    s = []

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                s.append((i, j))

    return s


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    copy = deepcopy(board)

    if player(copy) == X:
        copy[action[0]][action[1]] = X
    elif player(copy) == O:
        copy[action[0]][action[1]] = O
    else:
        raise Exception("Error in the result function, could not apply action to the state")

    return copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check for horizontal
    for row in board:
        if row == [X] * 3:
            return X
        elif row == [O] * 3:
            return O
    
    # Check for vertical
    for i in range(0, 3):
        if f"{board[0][i]}{board[1][i]}{board[2][i]}" == "XXX":
            return X
        elif f"{board[0][i]}{board[1][i]}{board[2][i]}" == "OOO":
            return O

    # Check for diagonal
    if f"{board[0][0]}{board[1][1]}{board[2][2]}" == "XXX":
        return X
    elif f"{board[0][0]}{board[1][1]}{board[2][2]}" == "OOO":
        return O
    elif f"{board[2][0]}{board[1][1]}{board[0][2]}" == "XXX":
        return X
    elif f"{board[2][0]}{board[1][1]}{board[0][2]}" == "OOO":
        return O
    
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    l = []

    for row in board:
        for element in row:
            l.append(element)

    if winner(board) != None:
        return True
    elif l.count(EMPTY) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def min_value(board):
        if terminal(board):
            return utility(board)
        else:
            current_value = 1000000000000000000000000000000
            for action in actions(board):
                x = result(board, action)
                temp = max_value(x)
                if temp < current_value:
                    current_value = deepcopy(temp)
            return current_value


    def max_value(board):
        if terminal(board):
            return utility(board)
        else:
            current_value = -1000000000000000000000000000000
            for action in actions(board):
                x = result(board, action)
                temp = min_value(x)
                if temp > current_value:
                    current_value = deepcopy(temp)
            return current_value


    if terminal(board):
        return None
    
    if player(board) == X:
        possible_actions = {}
        for action in actions(board):
            x = result(board, action)
            possible_actions[action] = min_value(x)
        
        for key in possible_actions.keys():
            if possible_actions[key] == 1:
                return key
        for key in possible_actions.keys():
            if possible_actions[key] == 0:
                return key
        for key in possible_actions.keys():
            if possible_actions[key] == -1:
                return key
    else:
        possible_actions = {}
        for action in actions(board):
            x = result(board, action)
            possible_actions[action] = max_value(x)

        for key in possible_actions.keys():
            if possible_actions[key] == -1:
                return key
        for key in possible_actions.keys():
            if possible_actions[key] == 0:
                return key
        for key in possible_actions.keys():
            if possible_actions[key] == 1:
                return key