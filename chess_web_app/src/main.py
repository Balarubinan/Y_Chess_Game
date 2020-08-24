grid=[(['.']*8)[:] for x in range(8)]
# W-white player B-Black Player

# K - King ,Q-Queen,H-Knight,B-Bishop,P-Pawn,R-Rook

turn=1
WhiteCheck,BlackCheck=False,False

def init_grid():
    global grid
    arr = ['R', 'H', 'B', 'K', 'Q', 'B', 'H', 'R']
    for x in range(8):
        grid[0][x] = 'B' + arr[x]

    for x in range(8):
        grid[-1][x] = 'W' + arr[x]

    for x in range(8):
        grid[1][x] = 'BP'

    for x in range(8):
        grid[-2][x] = 'WP'


def print_grid():
    global grid
    for x in grid:
        print(x)

def direction(x,y,ex,ey):
    val1,val2=-1,-1
    if ex-x>0:
        val1=1
    elif ex-x==0:
        val1=0

    if ey-y>0:
        val2=1
    elif ey-y==0:
        val2=0

    return val1,val2

def obstusruted(x,y,ex,ey,mode="d"):
    global grid
    dirx,diry=direction(x,y,ex,ey)
    print(dirx,diry)
    stx,sty=x+dirx,y+diry
    lis=[]
    while(stx!=ex or sty!=ey):
        if grid[stx][sty]!='.':
            print("Obtruct returened false")
            if mode=="d":
                return False
            else:
                return lis
        else:
            lis.append((stx,sty))
        stx+=dirx
        sty+=diry
    if mode=='d':
        return True
    else:
        return lis

def check():
    global  WhiteCheck,BlackCheck,grid
    WhiteCheck,BlackCheck=False,False
    wx,wy,bx,by=0,0,0,0
    for x in range(8):
        for y in range(8):
            if grid[x][y]=='WK':
                wx,wy=x,y
            if grid[x][y]=='BK':
                bx,by=x,y

    for x in range(8):
        for y in range(8):
            # checking for Black King
            if movable('WR',bx,by,x,y) and (bx,by)!=(x,y) and (grid[x][y] in ('BR','BQ')):
                WhiteCheck = True
            elif movable('WB',bx,by,x,y) and  (bx,by)!=(x,y) and (grid[x][y]=='BB' or (grid[x][y]=='BP' and abs(x-y)==1)):
                WhiteCheck=True

    for x in range(8):
        for y in range(8):
            # checking for Black King
            if movable('BR', bx, by, x, y) and (bx, by) != (x, y) and (grid[x][y] in ('WR', 'WQ')):
                BlackCheck = True
            elif movable('BB', bx, by, x, y) and (bx, by) != (x, y) and (
                    grid[x][y] == 'BB' or (grid[x][y] == 'WP' and abs(x - y) == 1)):
                BlackCheck = True
    print("rpiscvsfv:",get_check_stat(),(bx,by),(wx,wy))
    return (get_check_stat(),(bx,by),(wx,wy))

def check_mate():
    pass

def straight(x,y,ex,ey):
    if (x==ex or y==ey) and obstusruted(x,y,ex,ey):
        return True
    print("Strainght False")
    return False

def diagnal(x,y,ex,ey):
    if abs(x-ex)==abs(y-ey) and obstusruted(x,y,ex,ey):
        return True
    print("Diagnol False")
    return False

def lmove(x,y,ex,ey):
    print(x,y,ex,ey)
    if (abs(x-ex),abs(y-ey)) in [(2,1),(1,2)]:
        return True
    print("L Move False")
    return False

def movable(coin,x,y,ex,ey):
    global grid
    color = coin[0]
    coin=coin[1]
    print(x,y,ex,ey)
    if(coin=='P'):
        if (straight(x,y,ex,ey) or diagnal(x,y,ex,ey)) and (abs(y-ey)<=1 and abs(x-ex)==1):
        # if ((straight(x, y, ex, ey) and grid[x][y] == '.' and abs(y-ey)==1) or (diagnal(x, y, ex, ey) and grid[x][y] != '.')) and abs(x-ex)==1:
                print("Got here!", color)
                if color=='B' and ex>x:
                    return(True)
                elif color=='W' and ex<x:
                    return True
                else:
                    print("PAwn logic False")
                    return False
        else:
            print("Pawn False")
            return False

    elif coin=='Q':
        if straight(x,y,ex,ey) or diagnal(x,y,ex,ey):
            return True
        print("Queen False")
        return False

    elif coin=='R':
        if straight(x,y,ex,ey):
            return True
        print("Rook False")
        return False

    elif coin=='B':
        if diagnal(x,y,ex,ey):
            return True
        else:
            print("Bishop false")
            return False

    elif coin=='H':
        print("got here")
        return lmove(x,y,ex,ey)

    elif coin=='K':
        if ( straight(x,y,ex,ey) or diagnal(x,y,ex,ey) ) and (abs(x-ex)<=1 and abs(y-ey)<=1):
            return True
        else:
            print("King move False!")
            return False
    else:
        print("Movable totaal false")
        return False

def validate_move(t,gr,x,y,ex,ey):
    global turn,grid
    turn,grid=t,gr
    coin=grid[x][y]
    end_coin=grid[ex][ey]
    # 'WK'
    print("Before Validate ",coin,turn,end_coin[0],)
    if coin=='.' or (turn==0 and (coin[0]=='B' or end_coin[0]=='W')) or (turn==1 and (coin[0]=='W' or end_coin[0]=='B')):
        print("Validate False Pre")
        return False
    else:
        res=movable(coin,x,y,ex,ey)
        if res is True:
            # print("True part!")
            # grid[ex][ey]=coin
            # grid[x][y]='.'
            print("Validate True")
            return(True)
        else:
            print("Validate False")
            return(False)

def move():
    global turn,grid
    if(turn==1):
        print("White's move:")
        x,y=map(int,input("Enter Start Point").split(' '))
        ex,ey=map(int,input("Enter end Point").split(' '))
        res=validate_move(x,y,ex,ey)
        turn=0
    else:
        print("Black's move")
        x,y=map(int,input("Enter Start Point").split(' '))
        ex,ey=map(int,input("Enter end Point").split(' '))
        res=validate_move(x,y,ex,ey)
        turn=1

def check_mate():
    pass

def get_check_stat():
    global WhiteCheck,BlackCheck
    return (WhiteCheck,BlackCheck)

def set_grid(gr):
    global grid
    grid=gr

# init_grid()
# while(True):
#     move()
#     print_grid()
