import tkinter as tk
import pygame
from pygame import mixer
#from tkinter import messagebox
from PIL import Image,ImageTk
import random
#import tkinter.messagebox

#Setting Audio
mixer.init()

snakehiss = mixer.Sound("snake.wav")
ladderclimb = mixer.Sound("ladder.wav")
# diceSound = mixer.Sound("dice.mp3")

mixer.music.load("music.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.0)


#storing dice images in Dice list
Dice = []
#storing cordinates of numbers of board 
Index = {}

#Initial position of players
position1 = None
position2 = None
position3 = None

#ladder from bottom to top
Ladder={2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}

#Snake from head to tail
Snake={16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}

#Setting Players and dice buttons
def startGame():
  global diceImg,button1,button2,button5
  #Player 1
  # button1 = tk.Button(root,text="Player-1",height=3,width=20,fg="white",bg="blue",font=('Cursive',14,'bold') ,activebackground="blue",command=rollDice)
  button1.place(x=1200,y=400)

  #Player 2
  # button2 = tk.Button(root,text="Player-2",height=3,width=20,fg="white",bg="green",font=('Cursive',14,'bold') ,activebackground="green",command=rollDice)
  button2.place(x=1200,y=600)

  button5.place(x=1200,y=800)

  #Dice
  diceImg = Image.open("images/dice.png")
  diceImg = diceImg.resize((65,65))
  diceImg = ImageTk.PhotoImage(diceImg)
  button3 = tk.Button(root,image=diceImg,width=80,height=80,bg="white")
  button3.place(x=1280,y=250)

  #Exit
  button4 = tk.Button(root,text="Exit Game",height=3,width=20,fg="white",bg="red",font=('Cursive',14,'bold') ,activebackground="red" , command=root.destroy)
  button4.place(x=1200,y=20)


def resetPiece():
  global player1,player2,player3,position1,position2,position3

  player1.place(x=0,y=950)
  player2.place(x=50,y=950)
  player3.place(x=100,y=950)

  position1 = 0
  position2 = 0
  position3 = 0


def getDiceImages():
  global Dice
  dices = ["dice1.jpg","dice2.jpg","dice3.jpg","dice4.jpg","dice5.jpg","dice6.jpg"]
  for i in dices:
    diceImg = Image.open("images/"+i)
    diceImg = diceImg.resize((65,65))
    diceImg = ImageTk.PhotoImage(diceImg)
    Dice.append(diceImg)

def checkLadder(Turn):
  global position1,position2,position3,Ladder

  temp = 0 #No ladder
  if Turn==1:
    if position1 in Ladder:
      position1 = Ladder[position1]
      pygame.mixer.Sound.play(ladderclimb)
      temp=1
  elif Turn==2:
    if position2 in Ladder:
      position2 = Ladder[position2]
      pygame.mixer.Sound.play(ladderclimb)
      temp=1
  else:
    if position3 in Ladder:
      position3 = Ladder[position3]
      pygame.mixer.Sound.play(ladderclimb)
      temp=1
  return temp

def checkSnake(Turn):
  global position1,position2,position3,Snake

  if Turn==1:
    if position1 in Snake:
      position1 = Snake[position1]
      pygame.mixer.Sound.play(snakehiss)
  elif Turn==2:
    if position2 in Snake:
      position2 = Snake[position2]
      pygame.mixer.Sound.play(snakehiss)
  else:
    if position3 in Snake:
      position3 = Snake[position3]
      pygame.mixer.Sound.play(snakehiss)

      


def rollDice():
  global Dice,turn,position1,position2,position3
  global button1,button2
  
  r = random.randint(1,6)
  button3 = tk.Button(root,image=Dice[r-1],width=80,height=80,bg="white")
  button3.place(x=1280,y=250)

  lad=0 #no ladder
  #pygame.mixer.Sound.play(diceSound)
  if turn==1:
    if(position1+r)<=100:
      position1 = position1 + r
    lad=checkLadder(turn)
    checkSnake(turn)
    movePiece(turn,position1)
    if r!=6 and lad!=1:
      turn=2
      button1.configure(state="disabled")
      button5.configure(state="disabled")
      button2.configure(state="normal")
  elif turn==2:
    if(position2+r)<=100:
      position2 = position2 + r
    lad=checkLadder(turn)
    checkSnake(turn)
    movePiece(turn,position2)
    if r!=6 and lad!=1:
      turn=3
      button2.configure(state="disabled")
      button1.configure(state="disabled")
      button5.configure(state="normal")
  else:
    if(position3+r)<=100:
      position3 = position3 + r
    lad=checkLadder(turn)
    checkSnake(turn)
    movePiece(turn,position3)
    if r!=6 and lad!=1:
      turn=1
      button2.configure(state="disabled")
      button1.configure(state="normal")
      button5.configure(state="disabled")

  isWinner()

def isWinner():
  global position1,position2,position3

  if position1==100:
    lab = tk.Label(root,text="Player 1 is the WINNER",height=2,width=20,bg='blue',font=('Cursive',30,'bold'))
    lab.place(x=300,y=300)
    resetPiece()
  elif position2==100:
    lab = tk.Label(root,text="Player 2 is the WINNER",height=2,width=20,bg='green',font=('Cursive',30,'bold'))
    lab.place(x=300,y=300)
    resetPiece()
  elif position3==100:
    lab = tk.Label(root,text="Player 3 is the WINNER",height=2,width=20,bg='red',font=('Cursive',30,'bold'))
    lab.place(x=300,y=300)
    resetPiece()



def movePiece(Turn,r):
  global player1,player2,player3
  global Index

  if Turn==1:
    player1.place(x=Index[r][0],y=Index[r][1])
  elif Turn==2:
    player2.place(x=Index[r][0],y=Index[r][1])
  else:
    player3.place(x=Index[r][0],y=Index[r][1])


def getIndex():
  global player1,player2,player3

  Num = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 61, 62, 63 , 64, 65, 66, 67, 68, 69, 70, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  row = 30
  i=0
  for x in range(1,11):
    column = 30
    for y in range(1,11):
      Index[Num[i]] = (column,row)
      column = column + 95
      i = i+1
    row = row +95
  print(Index)

root = tk.Tk()
root.geometry("1200x1000")
root.title("Snakes and Ladders")

F1 = tk.Frame(root,width=1200,height=1000,relief='raise')
F1.place(x=0,y=0)

#Setting Board
image1 = ImageTk.PhotoImage(Image.open("images/snakesandladderboard.jpg"))
lable = tk.Label(F1,image=image1)
lable.place(x=0,y=0)

#Player1 pice
player1 = tk.Canvas(root,width=40,height=40)
player1.create_oval(10,10,40,40,fill='blue')

# player1 = ImageTk.PhotoImage(Image.open("images/player1.png"))
# l1 = tk.Label(F1,image=player1)
# l1.resize((65,65))
# l1.place(x=0,y=100)

#Player2 piece
player2 = tk.Canvas(root,width=40,height=40)
player2.create_oval(10,10,40,40,fill='green')

#player3 piece
player3 = tk.Canvas(root,width=40,height=40)
player3.create_oval(10,10,40,40,fill='red')

#Player 1 button
button1 = tk.Button(root,text="Player-1",height=3,width=20,fg="white",bg="blue",font=('Cursive',14,'bold') ,activebackground="blue",command=rollDice)

#Player 2 button
button2 = tk.Button(root,text="Player-2",height=3,width=20,fg="white",bg="green",font=('Cursive',14,'bold') ,activebackground="green",command=rollDice)

#Player 3 button
button5 = tk.Button(root,text="Player-3",height=3,width=20,fg="white",bg="red",font=('Cursive',14,'bold') ,activebackground="red",command=rollDice)


#By default player 1 turn=1st
turn = 1

#keeping players at starting point
resetPiece()

#get index of each number on the board
getIndex()

#Get dice images
getDiceImages()
#tkinter.messagebox.showinfo(title=None, message="WELCOME SNAKES AND LADDER \n click OK to start")
startGame()
root.mainloop()