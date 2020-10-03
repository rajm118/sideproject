import turtle
import winsound

wn=turtle.Screen()
wn.title('ping pong by Raj')
wn.bgcolor('black')
wn.setup(width=800,height=600)
#it stops the screen from getting auto updated and it basically speeds up the game
wn.tracer(0)

#score variables
score_a=0
score_b=0

#paddle A
paddle_a=turtle.Turtle()
#here speed 0 is for animation by this we specify that the paddle should have max speed
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('cyan')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
#when we go to a location turtle draws a line to that pixel and to avoid that we use penup method
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
#here speed 0 is for animation by this we specify that the paddle should have max speed
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('cyan')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
#when we go to a location turtle draws a line to that pixel and to avoid that we use penup method
paddle_b.penup()
paddle_b.goto(350,0)

#ball in the centre
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('cyan')
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2


#score keeper
score=turtle.Turtle()
score.speed(0)
score.color('yellow')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write('Player A:{} Player B:{}'.format(score_a,score_b),align='center',font=('courier',24,'normal'))

#fucntion for paddle movement
def paddle_a_up():
    y=paddle_a.ycor()
    #kepping paddle from going out of screen
    if(y>250):
        y=y-20
    else:
        y+=20
        paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    #kepping paddle from going out of screen
    if(y<-250):
        y=y+20
    else:
        y-=20
        paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    #kepping paddle from going out of screen
    if(y>250):
        y=y-20
    else:
        y+=20
        paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    #kepping paddle from going out of screen
    if(y<-250):
        y=y+20
    else:
        y-=20
        paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')


#main game loop
while True:
    wn.update()

    #ball move
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        #when ball goes out of screen score gets incremented
        score_a+=1
        score._clear()
        score.write('Player A:{} Player B:{}'.format(score_a,score_b),align='center',font=('courier',24,'normal'))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        #when ball goes out of screen score gets incremented
        score_b+=1
        score._clear()
        score.write('Player A:{} Player B:{}'.format(score_a,score_b),align='center',font=('courier',24,'normal'))

    # paddle and ball collison
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50:
        ball.setx(340)
        ball.dx*=-1
        #winsound.PlaySound('mp3file')
    
    if ball.xcor() <-340 and ball.xcor() >- 350 and ball.ycor() < paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50:
        ball.setx(-340)
        ball.dx*=-1
        #winsound.PlaySound('mp3file')
