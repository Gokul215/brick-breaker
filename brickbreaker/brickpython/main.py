from Brickbreaker import Brickbreaker
brick=Brickbreaker(7,7)
brick.placeBricks(2,2,1)
brick.placeBricks(2,3,1)
brick.placeBricks(2,4,1)
brick.placeBricks(3,2,1)
brick.placeBricks(3,3,1)
brick.placeBricks(3,4,1)
while True:
    brick.printboard()
    direction =input("enter the move(l,r,s): ")
    match direction:
        case 'l':
            ballx=brick.ballpos[0]
            bally=brick.ballpos[1]
            brick.movedirection(ballx,bally,-1,-1)

        case 'r':
            ballx=brick.ballpos[0]
            bally=brick.ballpos[1]
            brick.movedirection(ballx,bally,-1,1)

        case 's':
            ballx=brick.ballpos[0]
            bally=brick.ballpos[1]
            brick.movedirection(ballx,bally,-1,0)
        case _:
            print("invalid direction")
            break