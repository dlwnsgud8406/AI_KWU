import copy

def white_move_down(current_state, index): #백말이 아래로 움직일때
    i = index [0]
    j = index [1]
    state = copy.deepcopy(current_state)
    state[i][j] = '-'
    state[i+1][j] = 'w'
    return state

def white_move_leftdown(current_state, index): #백말이 대각왼쪽으로 움직일때(흑말을 잡아먹을때)
    i = index [0]
    j = index [1]
    state = copy.deepcopy(current_state)
    state[i][j] = '-'
    state[i+1][j-1] = 'w'
    return state

def white_move_rightdown(current_state, index): #백말이 대각오른쪽으로 움직일때(흑말을 잡아먹을때)
    i = index [0]
    j = index [1]
    state = copy.deepcopy(current_state)
    state[i][j] = '-'
    state[i+1][j+1] = 'w'
    return state

def black_moveup(current_state, index): # 흑말이 위로 움직일때
    i = index [0]
    j = index [1]
    state = copy.deepcopy(current_state)
    state[i][j] = '-'
    state[i-1][j] = 'b'
    return state

def black_move_leftup(current_state, index): #흑말이 왼쪽위로 움직일때(백말을 잡아먹을때)
    i = index [0]
    j = index [1]
    state = copy.deepcopy(current_state)
    state[i][j] = '-'
    state[i-1][j-1] = 'b'
    return state

def black_move_rightup(current_state, index): #흑말이 오른쪽위로 움직일때(백말을 잡아먹을때)
    i = index [0]
    j = index [1]
    state = copy.deepcopy(current_state)
    state[i][j] = '-'
    state[i-1][j+1] = 'b'
    return state