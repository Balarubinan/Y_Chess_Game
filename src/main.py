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

def obstusruted(x,y,ex,ey):
    global grid
    dirx,diry=direction(x,y,ex,ey)
    print(dirx,diry)
    stx,sty=x+dirx,y+diry
    while(stx!=ex or sty!=ey):
        if grid[stx][sty]!='.':
            return False
        # stx+=dirx
        # sty+=diry
    return True

def check():
    pass

def check_mate():
    pass

def straight(x,y,ex,ey):
    if (x==ex or y==ey) and obstusruted(x,y,ex,ey):
        return True
    return False

def diagnal(x,y,ex,ey):
    if x-ex==y-ey and obstusruted(x,y,ex,ey):
        return True
    return False

def lmove(x,y,ex,ey):
    if (abs(x-ex),abs(y-ey)) in [(3,1),(1,3)]:
        return True
    return False

def movable(coin,x,y,ex,ey):
    color = coin[0]
    coin=coin[1]
    if(coin=='P'):
        if straight(x,y,ex,ey) or diagnal(x,y,ex,ey) and abs(y-ey)==1 and abs(x-ex)<=1:
            print("Got here!", color)
            if color=='B' and ex>x:
                return(True)
            elif color=='W' and ex<x:
                return True
            else:
                return False
        else:
            return False

    elif coin=='Q':
        if straight(x,y,ex,ey) or diagnal(x,y,ex,ey):
            return True
        return False

    elif coin=='R':
        if straight(x,y,ex,ey):
            return True
        return False

    elif coin=='B':
        if diagnal(x,y,ex,ey):
            return True
        else:
            return False

    elif coin=='H':
        return lmove(x,y,ex,ey)

    elif coin=='K':
        if ( straight(x,y,ex,ey) or diagnal(x,y,ex,ey) ) and (abs(x-ex)<=1 and abs(y-ey)<=1):
            return True
    else:
        return False

def validate_move(gr,t,x,y,ex,ey):
    global turn,grid
    turn=t
    grid=gr
    coin=grid[x][y]
    end_coin=grid[ex][ey]
    # 'WK'
    if coin=='.' or (turn==1 and (coin[0]=='B' or end_coin[0]=='W')) or (turn==0 and (coin[0]=='W' or end_coin[0]=='B')):
        return False
    else:
        res=movable(coin,x,y,ex,ey)
        if res is True:
            print("True part!")
            return True
        else:
            print("Invalid Move....Given end not reachable!!")
            return(False)

def move():
    turn=0
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

# init_grid()
# while(True):
#     move()
#     print_grid()
