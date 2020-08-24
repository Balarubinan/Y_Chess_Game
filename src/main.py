# grid=[(['.']*8)[:] for x in range(8)]
# # W-white player B-Black Player
#
# # K - King ,Q-Queen,H-Knight,B-Bishop,P-Pawn,R-Rook
#
# turn=1


def print_grid():
    global grid
    for x in grid:
        print(x)


def direction(x, y, ex, ey):
    val1, val2 = -1, -1
    if ex - x > 0:
        val1 = 1
    elif ex - x == 0:
        val1 = 0

    if ey - y > 0:
        val2 = 1
    elif ey - y == 0:
        val2 = 0

    return val1, val2


def obstusruted(x, y, ex, ey):
    global grid
    dirx, diry = direction(x, y, ex, ey)
    stx, sty = x + dirx, y + diry
    while (stx != ex or sty != ey):
        if grid[stx][sty] != '.':
            return False
        stx += dirx
        sty += diry
    return True


def get_last_coin(x, y, dx, dy):
    pass


def check(bx=-1,by=-1,wx=-1,wy=-1,mode='D'):
    global grid
    Wcheck, Bcheck = False, False
    # bx, by, wx, wy = 0, 0, 0, 0
    if (bx,by,wx,wy)==(-1,-1,-1,-1):
        for x in range(8):
            for y in range(8):
                if grid[x][y] == 'BK':
                    bx, by = x, y
                if grid[x][y] == 'WK':
                    wx, wy = x, y

    if wx>=0:
        for x in range(8):
            for y in range(8):
                if grid[x][y] != '.':
                    if movable(grid[x][y],x,y,bx,by) and grid[x][y][0]=='W':
                        Bcheck=True

    if bx>=0:
        for x in range(8):
            for y in range(8):
                if grid[x][y]!='.':
                    if movable(grid[x][y], x, y, wx, wy) and grid[x][y][0]=='B':
                        Wcheck = True
    print("Check Function Was Called!!")
    if mode=='D':
        return ((wx,wy),(bx,by),Wcheck,Bcheck)
    elif mode=='W':
        return Wcheck
    elif mode=='B':
        return Bcheck

def check_mate():
    global grid
    a=check()
    wx, wy = a[0]
    bx, by = a[1]
    Wc, Bc = a[2], a[3]
    if Wc:
        for x in [0,1,-1]:
            for y in [0,1,-1]:
                if wx + x in range(8) and wy + y in range(8) and grid[wx+x][wy+y]=='.':
                    a=check(wx+x,wy+y,-1,-1,mode='W')
                    if a==False:
                        return False,1
        print("CheckMate for White")
        return (True,'W')
    elif Bc:
        print("Boxes Checked:")
        for x in [0,1,-1]:
            for y in [0,1,-1]:
                if bx+x in range(8) and by+y in range(8) and grid[bx+x][by+y]=='.':
                    print(bx+x,by+y)
                    a=check(bx+x,by+y,-1,-1,mode='B')
                    if a==False:
                        return False,1
        print("CheckMate for Black")
        return (True,"B")
    else:
        return False,1

def straight(x, y, ex, ey):
    if (x == ex or y == ey) and obstusruted(x, y, ex, ey):
        return True
    return False


def diagnal(x, y, ex, ey):
    if abs(x - ex) == abs(y - ey) and obstusruted(x, y, ex, ey):
        return True
    return False


def lmove(x, y, ex, ey):
    if (abs(x - ex), abs(y - ey)) in [(2, 1), (1, 2)]:
        return True
    return False


def movable(coin, x, y, ex, ey):
    color = coin[0]
    coin = coin[1]
    if (coin == 'P'):
        if (straight(x, y, ex, ey) or diagnal(x, y, ex, ey)) and (abs(y - ey) <= 1 and abs(x - ex) == 1):
            print("Got here!", color)
            if color == 'B' and ex > x:
                return (True)
            elif color == 'W' and ex < x:
                return True
            else:
                return False
        else:
            return False

    elif coin == 'Q':
        if straight(x, y, ex, ey) or diagnal(x, y, ex, ey):
            return True
        return False

    elif coin == 'R':
        if straight(x, y, ex, ey):
            return True
        return False

    elif coin == 'B':
        if diagnal(x, y, ex, ey):
            return True
        else:
            return False

    elif coin == 'H':
        return lmove(x, y, ex, ey)

    elif coin == 'K':
        if (straight(x, y, ex, ey) or diagnal(x, y, ex, ey)) and (abs(x - ex) <= 1 and abs(y - ey) <= 1):
            return True
    else:
        return False


def validate_move(gr, t, x, y, ex, ey):
    global turn, grid
    turn = t
    grid = gr
    coin = grid[x][y]
    end_coin = grid[ex][ey]
    # 'WK'
    if coin == '.' or (turn == 0 and (coin[0] == 'B' or end_coin[0] == 'W')) or (
            turn == 1 and (coin[0] == 'W' or end_coin[0] == 'B')):
        return False
    else:
        res = movable(coin, x, y, ex, ey)
        if res is True:
            print("True part!")
            return True
        else:
            print("Invalid Move....Given end not reachable!!")
            return (False)


def move():
    turn = 0
    if (turn == 1):
        print("White's move:")
        x, y = map(int, input("Enter Start Point").split(' '))
        ex, ey = map(int, input("Enter end Point").split(' '))
        res = validate_move(x, y, ex, ey)
        turn = 0
    else:
        print("Black's move")
        x, y = map(int, input("Enter Start Point").split(' '))
        ex, ey = map(int, input("Enter end Point").split(' '))
        res = validate_move(x, y, ex, ey)
        turn = 1

def set_grid(gr):
    global grid
    grid=gr

# init_grid()
# while(True):
#     move()
#     print_grid()
