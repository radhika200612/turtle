#import the turtle module
import turtle
import math
import random
import os

#Screen setup
wn = turtle.Screen()
wn.bgcolor("black")
#wn.bgpic("bg.gif") - to add background (gif) img
wn.tracer(3) #drops animation frames so that game works faster
 
#Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.color("white")
mypen.setposition(-100, -100)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
  mypen.forward(200)
  mypen.left(90)
mypen.hideturtle()

#Create turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()  #removes the trail
player.speed(0)  #no breaks while turning
player.setposition(0, 0)

#Create Score
score = 0

#Create enemy
maxGoals = 3
goal = []

for count in range(maxGoals):
  goal.append(turtle.Turtle())
  goal[count].color("red")
  goal[count].shape("circle")
  goal[count].penup()
  goal[count].speed(0)
  goal[count].setposition(random.randint(-90, 90), random.randint(-90, -90))

"""
#single enemy

goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-90, 90), random.randint(-90, -90))
"""

#Set speed variable
speed = 1


#Define the functions
def turnleft():
  player.left(45)


def turnright():
  player.right(45)


def increasespeed():
  global speed
  speed = speed + 1


def isCollision(t1, t2):
  d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.xcor(), 2))
  if d < 25:
    return True
  else:
    return False

#keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")

while True:
  player.forward(speed)

  #Boundary Check
  if player.xcor() > 100 or player.xcor() < -100:
    player.right(180)
    #os.system("afplay bounce.mp3&") - music
  if player.ycor() > 100 or player.ycor() < -100:
    player.right(180)
    #os.system("afplay bounce.mp3&") - music 

  #Move the goal
  for count in range(maxGoals):
    goal[count].forward(1)

    #Boundary Check for goal
    if goal[count].xcor() > 90 or goal[count].xcor() < -90:
      goal[count].right(180)
      #os.system("afplay bounce.mp3&") - music
    if goal[count].ycor() > 90 or goal[count].ycor() < -90:
      goal[count].right(180)
      #os.system("afplay bounce.mp3&") - music
        
    #Colision check
    if isCollision(player, goal[count]):
      goal[count].setposition(random.randint(-90, 90), random.randint(-90, -90))
      goal[count].right(random.randint(0, 360))
      #os.system("afplay bounce.mp3&") - music
      score = score + 1
      
      # print score on screen
      mypen.undo()
      mypen.penup()
      mypen.hideturtle()
      mypen.setposition(-100, 110)
      scorestring = "Score: %s" %score
      mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


  """
  #single enemy goal

  goal.forward(1)

    #Boundary Check for goal
    if goal.xcor() > 90 or goal.xcor() < -90:
      goal.right(180)
    if goal.ycor() > 90 or goal.ycor() < -90:
      goal.right(180)
        
    #Colision check
    if isCollision(player, goal):
      goal.setposition(random.randint(-90, 90), random.randint(-90, -90))
      goal.right(random.randint(0, 360))
  """
