# making an empty chess board
grid = {x: (['.'] * 8)[:] for x in "abcdefgh"}
print(grid)


# notations
# K=king
# Q=Queen
# P=pawn
# Kn=Knight
# B=bishop
# R=rook
# WK=> white king BK=>black king and so for other pieces
# move (#start,#end) ex => (e4,e5)
def get_coin(x, y):
    '''uses zero based coordinates'''

    if x in "abcdefgh" and int(y) in range(8):
        return (grid[x][y])
    else:
        return False

def return_coords(start, end):
    """returns Zero-indexed coordinates"""

    return (start[0], int(start[1])-1, end[0], int(end[1])-1)

def check_for_check(ex,ey):
    pass

def check_valid_move(player, start, end):
    """Validates the move and returns the validity"""
    global grid
    try:
        print(player, start, end)
        sx, sy, ex, ey = return_coords(start, end)
        print(sx,sy)
        coin = get_coin(sx, sy)
        print(coin)
        grid[ex][ey] = coin
        grid[sx][sy] = '.'
        return(True)
    except Exception as e:
        print(e)
        return(False)

def make_move(player, move):
    '''Makes the move after validating ie updates the grid!'''
    global grid
    start, end = move.split(',')
    val = check_valid_move(player, start, end)
    if val is False:
        return ({'status': 'error'})
    else:
        return({'status':'success'})

grid['a'][0]="I am a king"
print(grid)
make_move('A',"a1,a2")
print(grid)
