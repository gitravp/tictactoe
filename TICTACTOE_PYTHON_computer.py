#0 1 2
#3 4 5
#6 7 8
#return number to play next, if none available return -1,if already won,return first available
comp1=[]
player1=[]
available1=[0,1,2,3,4,5,6,7,8]
wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]    #all win condition possibilities

#create list of our possiblel wins
#wins_left=[]
#for i in wins:
#    if(i[0] not in player and i[1] not in player and i[2] not in player):
#        wins_left.append(i)

        

def next_move(comp,player,available):
    #if no available moves return none
    if(len(available)==0):
        #print("case1")
        return(None)
    

    #1: Check if already won
    for i in wins:
        if(i[0] in comp and i[1] in comp and i[2] in comp):
            #print("case2")
            return("9")
    #check if we can win in one move and return the missing number
    for i in wins:
        for j in i:
            temp=[i for i in comp]
            temp.append(j)
            if(i[0] in temp and i[1] in temp and i[2] in temp and j in available):
                #print("case3",j)
                return(j)
    #check if opponent about to win and return spot to prevent it
    for i in wins:
        for j in i:
            temp=[i for i in player]
            temp.append(j)
            if(i[0] in temp and i[1] in temp and i[2] in temp and j in available):
                #print("case4")
                return(j)
    #else return first available spot
    #print("case5")
    return(available[0])
'''
while(available1!=[]):
    print("b4 player:",available1)
    a=int(input("player move"))
    player1.append(a)
    available1.remove(a)
    print("after player:",available1)
    b=next_move(comp1,player1,available1)
    available1.remove(b)
    print("computer move:",b)
    print("after comp:",available1)
    comp1.append(b)
    '''