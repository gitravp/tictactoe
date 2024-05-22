#--------------------------------------------------variables--------------------------------------------------------------------------
p1="X"             #symbol of p1
p1_bg="red"        #color of p1
p2="O"             #symbol of p2
p2_bg="green"      #color of p2
default_bg="white" #default board background color
winner=None        #winner if any
turn=1             #global turn var decides if it is p1's turn(1) or p2's turn(-1)
mode="pvc"

p1arr=[]    #holds all moves of p1 in order
p2arr=[]    #holds all moves of p2 in order
available=[0,1,2,3,4,5,6,7,8]
wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]    #all win condition possibilities

from TICTACTOE_PYTHON_computer import next_move

#--------------------------------------------screen/label updating function-------------------------------------------------------------
def toggle_mode():
    global mode         #global mode variable to be toggled
    reset()             #first reset the board to start fresh in new mode
    if(mode=="pvc"):    #if mode was pvc,toggle to pvp, and vice versa. Also update the change on the screen
        mode="pvp"
        update_screen("MODE:PvP -Make a move")
    else:
        mode="pvc"
        update_screen("MODE:PvC -Make a move")

#--------------------------------------------screen/label updating function-------------------------------------------------------------
def update_screen(txt):
    screen.config(text=txt)  #change text of our label to the provided argument txt 

#-----------------------------------------------win condition checking function----------------------------------------------------------
def checkwin():
    global turn
    if(turn==1):          #check turn to see who's win to check for(w=potential winner)
        p=p1arr
        w="p1"
    else:
        p=p2arr
        w="p2"
    for i in wins:        #check if any of the win conditions are met
        if(i[0] in p and i[1] in p and i[2] in p):
            global winner
            winner=w
            button_state(winner)
            return(True)
    return(False)

#-------------------------------Button state control function---------------------------------------------------------------------------
#activate/deactivate buttons based on if someone won or not
def button_state(w):
    global mode
    match(mode):
        case("pvp"):
            if(w==None):
                for i in button_arr:
                    i.config(state="normal")
            else:
                for i in button_arr:
                    i.config(state="disabled")
        case("pvc"):
            if(w==None):
                for i in button_arr:
                    i.config(state="normal")
            else:
                for i in button_arr:
                    i.config(state="disabled")


    

#---------------------------------------------reset(empties out the board)---------------------------------------------------------------
def reset():
    global mode,p1arr,p2arr,available,turn,winner
    match(mode):
        case("pvp"):

            for i in button_arr:               #loop sets all buttons to blank
                i.config(text="",bg=default_bg)        
            p1arr.clear()                       #clears out the player moves from p1arr and p2arr
            p2arr.clear()
            available.clear()
            available.extend([0,1,2,3,4,5,6,7,8])
            turn=1                              #sets turn back to player1
            update_screen("player 1's turn")    #sets display back to p1's turn
            winner=None
            button_state(winner)
        case("pvc"):

            for i in button_arr:               #loop sets all buttons to blank
                i.config(text="",bg=default_bg)         
            p1arr.clear()                       #clears out the player moves from p1arr and p2arr
            p2arr.clear()
            available.clear()
            available.extend([0,1,2,3,4,5,6,7,8])
            turn=1                              #sets turn back to player1
            update_screen("player 1's turn")    #sets display back to p1's turn
            winner=None
            button_state(winner)

#----------------------------------------undo function(undo's the last move played) -----------------------------------------------------
def undo():
    global mode,turn,winner,p1arr,p2arr,available
    match(mode):
        case("pvp"):
            if(turn==1 and len(p2arr)>0):                  #if current turn is 1 or p1's =>last move was by p2(and make sure all plays havent been undone)
                b=p2arr.pop()                              #pop out last move of player2
                available.append(b)
                available.sort()
                button_arr[b].config(text="",bg=default_bg)#clear the button of that move
                turn*=-1                                   #set turn back to player2
                update_screen("player 2's turn")           #update screen to show that its p2's turn
            elif(turn==-1 and len(p1arr)>0):               #if current turn is -1 or p2's =>last move was by p1(and make sure all plays havent been undone)
                b=p1arr.pop()    
                available.append(b)                          #pop out last move of player1
                available.sort()
                button_arr[b].config(text="",bg=default_bg)#clear the button of that move
                turn*=-1                                   #set turn back to player1
                update_screen("player 1's turn")           #update screen to show that its p1's turn
            winner=None
            button_state(winner)
        case("pvc"):
            if(len(p1arr)==len(p2arr) and len(p1arr)>0):                  #if current turn is 1 or p1's =>last move was by p2(and make sure all plays havent been undone)
                b=p2arr.pop()                              #pop out last move of player2
                available.append(b)
                available.sort()
                button_arr[b].config(text="",bg=default_bg)#clear the button of that move                                  
                update_screen("player 2's turn")           #update screen to show that its p2's turn
            if(len(p1arr)>0):
                b=p1arr.pop()                              #pop out last move of player1
                available.append(b)
                available.sort()
                button_arr[b].config(text="",bg=default_bg)#clear the button of that move                                  
                update_screen("player 1's turn")           #update screen to show that its p1's turn
            turn=1
            winner=None
            button_state(winner)

#---------------------------------------------registering a players move after pressing a button----------------------------------------
def button_clicked(b):
    global mode,turn,p1arr,p2arr,available,winner
    match(mode):
        case("pvp"):
            if(b in p1arr):                                 #if a spot is already taken,prevent overwrite
                update_screen("space already taken by p1")
                return(1)
            elif(b in p2arr):
                update_screen("space already taken by p2")
                return(1)
            else:                                           #if it is a free spot, register the new play
                if(turn==1):                                #check turn to see if it is p1's or p2's play
                    button_arr[b].config(text=p1,bg=p1_bg)  #change button text to the player's symbol           
                    p1arr.append(b)                         #add the button number to the player's move list
                    available.remove(b)
                    available.sort()
                    if(checkwin()):                         #if the player has won,print the same
                        update_screen("player 1 wins!!")
                    else:                                   #if no win, display that it is the next player's turn
                        update_screen("player 2's turn")
                else:
                    button_arr[b].config(text=p2,bg=p2_bg)
                    p2arr.append(b)
                    available.remove(b)
                    available.sort()
                    if(checkwin()):
                        update_screen("player 2 wins!!")
                    else:
                        update_screen("player 1's turn")
                turn*=-1                                    #update the turn to the other player
        case("pvc"):
            if(b in p1arr):                                 #if a spot is already taken,prevent overwrite
                update_screen("space already taken by p1")
                return(1)
            elif(b in p2arr):
                update_screen("space already taken by Computer")
                return(1)
            else:                                           #if it is a free spot, register the new play
                if(turn==1):                                #check turn to see if it is p1's or p2's play
                    button_arr[b].config(text=p1,bg=p1_bg)  #change button text to the player's symbol           
                    p1arr.append(b)                         #add the button number to the player's move list
                    available.remove(b)
                    available.sort()
                    if(checkwin()):                         #if the player has won,print the same
                        update_screen("player 1 wins!!")
                    else:                                   #if no win, display that it is the next player's turn
                        update_screen("Computer's turn")
                    turn*=-1
                    if(winner==None):
                        b2=next_move(p2arr,p1arr,available)
                        if(b2!=None):
                            button_arr[b2].config(text=p2,bg=p2_bg)
                            p2arr.append(b2)
                            available.remove(b2)
                            available.sort()
                            if(checkwin()):
                                update_screen("Computer wins!!")
                            else:
                                update_screen("player 1's turn")
                            turn*=-1
                    #turn=1                                    #update the turn to the other player
                        else:
                            update_screen("Game Over- TIE")
                            turn*=-1



    
#--------------------------------------------------------GUI stuff----------------------------------------------------------------------
from tkinter import *
window=Tk()                 #create window
window.geometry("150x150")  #set window size
#window.title("TIC-TAC-TOE") #set window title, currently not visible due to small window size

#create board buttons and set their options
b0=Button(window,text="",width=4,height=2,command=lambda:button_clicked(0),bg=default_bg)  #row1
b0.grid(row=0,column=0,columnspan=1,rowspan=1)
b1=Button(window,text="",width=4,height=2,command=lambda:button_clicked(1),bg=default_bg)
b1.grid(row=0,column=1,columnspan=1,rowspan=1)
b2=Button(window,text="",width=4,height=2,command=lambda:button_clicked(2),bg=default_bg)
b2.grid(row=0,column=2,columnspan=1,rowspan=1)
b3=Button(window,text="",width=4,height=2,command=lambda:button_clicked(3),bg=default_bg)  #row2
b3.grid(row=1,column=0,columnspan=1,rowspan=1)
b4=Button(window,text="",width=4,height=2,command=lambda:button_clicked(4),bg=default_bg)
b4.grid(row=1,column=1,columnspan=1,rowspan=1)
b5=Button(window,text="",width=4,height=2,command=lambda:button_clicked(5),bg=default_bg)
b5.grid(row=1,column=2,columnspan=1,rowspan=1)
b6=Button(window,text="",width=4,height=2,command=lambda:button_clicked(6),bg=default_bg)  #row3
b6.grid(row=2,column=0,columnspan=1,rowspan=1)
b7=Button(window,text="",width=4,height=2,command=lambda:button_clicked(7),bg=default_bg)
b7.grid(row=2,column=1,columnspan=1,rowspan=1)
b8=Button(window,text="",width=4,height=2,command=lambda:button_clicked(8),bg=default_bg)
b8.grid(row=2,column=2,columnspan=1,rowspan=1)

#functional buttons
bundo=Button(window,text="UNDO",width=4,height=2,command=undo,bg=default_bg)
bundo.grid(row=0,column=3,columnspan=1,rowspan=1)
breset=Button(window,text="RSET",width=4,height=2,command=reset,bg=default_bg)
breset.grid(row=1,column=3,columnspan=1,rowspan=1)
bmode=Button(window,text="MODE",width=4,height=2,command=toggle_mode,bg=default_bg)
bmode.grid(row=2,column=3,columnspan=1,rowspan=1)
#display/screen
screen=Label(window,text="player 1's turn")
screen.grid(row=3,column=0,columnspan=4,rowspan=1,padx=0)
#list of the buttons to help with indexed operations
button_arr=[b0,b1,b2,b3,b4,b5,b6,b7,b8]
#mainloop of window

toggle_mode()

window.mainloop()

print(p1arr,p2arr,available)
