from visual import *

Rnum = 0
Lnum = 0

RightScore = text(pos=vector(4,6,0),text=str(Rnum), align='center', depth=0.1, color=color.green)
LeftScore = text(pos=vector(-4,6,0),text=str(Lnum), align='center', depth=0.1, color=color.green)

#ball
ball = sphere(pos=(-5,0,0),radius=0.5, color=color.cyan)

#box
RightWall = box(pos=(8,0,0), size=(0.2,12,12), color=color.green, opacity=0)
LeftWall = box(pos=(-8,0,0), size=(0.2,12,12), color=color.green, opacity=0)
TopWall = box(pos=(0,6,0), size=(12,0.2,12), color=color.yellow, opacity=0)
BottomWall = box(pos=(0,-6,0), size=(12,0.2,12), color=color.yellow, opacity=0)
wallBack = box(pos=(0,0,-6), size=(12,12,0.2), color=color.cyan, opacity=0)

RightPaddle = box(pos=(7,0,0), size=(1,4,0), color=color.blue)
LeftPaddle = box(pos=(-7,0,0), size=(1,4,0), color=color.blue)

ball.velocity=vector(25,35,0)

deltat=0.005
t=1

while 1 >0:
    rate(55)

    if ball.pos.x == RightPaddle.pos.x-1 and ball.pos.y <= RightPaddle.pos.y+2 and ball.pos.y >= RightPaddle.pos.y-2: 
        ball.velocity.x=-25

    if ball.pos.x == LeftPaddle.pos.x+1 and ball.pos.y <= LeftPaddle.pos.y+2 and ball.pos.y >= LeftPaddle.pos.y-2: 
        ball.velocity.x=25

    if ball.pos.x >= RightWall.pos.x:
        ball.velocity.x=-25
        
    elif ball.pos.x <= LeftWall.pos.x:
        ball.velocity.x=25
        
    elif ball.pos.y >= TopWall.pos.y:
        ball.velocity.y=-35
       
    elif ball.pos.y <= BottomWall.pos.y:
        ball.velocity.y=35

        
### SCOREBOARD ########################



    if ball.pos.x == LeftWall.pos.x:
        Rnum = Rnum + 1
        RightScore.text = str(Rnum)


        
    if ball.pos.x == RightWall.pos.x:
        Lnum = Lnum + 1
        LeftScore.text = str(Rnum)


       

######################################
# KEY PRESS EVENTS
    if scene.kb.keys: 
         key = scene.kb.getkey() 
         if key == "up":
            if LeftPaddle.pos.y <= 7:
                LeftPaddle.pos.y = LeftPaddle.pos.y + 2

         elif key == "down":
            if LeftPaddle.pos.y >= -7:
                LeftPaddle.pos.y = LeftPaddle.pos.y - 2 
         
         elif key == "w":
            if RightPaddle.pos.y <= 7:
                RightPaddle.pos.y = RightPaddle.pos.y + 2

         elif key == "s":
            if RightPaddle.pos.y >= -7:
                RightPaddle.pos.y = RightPaddle.pos.y - 2

    ball.pos = ball.pos + ball.velocity * deltat