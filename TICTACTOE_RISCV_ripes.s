.data
#arr:.word 0,16711680,0,0,0,65280,0,0,0
arr:.word 0,0,0,0,0,0,0,0,0
p1:.word 1,1,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1
p2:.word 1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1
wins:.word 0x00000124,0x00000092,0x00000049,0x000001c0,0x00000038,0x00000007,0x00000111,0x00000054        
w:.word 1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1

.text
beq x0,x0,exitfunc #dont exicute sub routine unless called

setledmatrix:
    li x14,9 #counter from 9 to 0
    add x15,x0,x7 #array pointer
    add x16,x0,x5 #led matrix pointer
    loop0:
        lw x17,0(x15) #load color to set from array matrix
        sw x17,0(x16) #store it into led matrix
        addi x15,x15,4 #incement array pointer to next element
        addi x16,x16,4 #increment led matrix pointer to next element
        addi x14,x14,-1 #dectrement counter
bne x14,x0,loop0 #loop 9 times,while counter>0
jalr x0,x1,0

checkplay: #x18 has new switch config,x9 active color,x10 color flip
la x15,arr #load arr color matrix
loop: #keep looping till exit
    andi x19,x18,1 #extract current swich pos 1 by 1
    lw x20,0(x15) #extract led color 1 by 1
    beq x19,x0,notswitched #if switch is off,no change
    bne x20,x0,notrightswitch #if switch is on,but color already set,no change
        sw x9,0(x15) #if color to be changed,load active color in current arr element
        xor x9,x9,x10 #change active color to other player   
        beq x0,x0,exitloop #branch to exit after changing color
    notswitched:
    notrightswitch:
    srli x18,x18,1 #shift to next switch
    addi x15,x15,4 #shift to next led in arr matrix
beq x0,x0,loop #inf loop till color to be changed found
exitloop: #exit after arr updated with player move          
jalr x0,x1,0 #branch back to main program    

dashboard:
    li x25,0x00000000 #background color for p1
    li x21,0x00fff000 #color of p1
    li x22,40 #counter to go through all 40 leds
    bne x9,x21,color2 #branch to pattern p2 if current color not that of p1
        la x23,p1 #if p1,load address of pttern p1
        loop2:
            lw x24,0(x23) #load on/off from p1 seq
            sw x25,0(x6) #store background color by default
            beq x24,x0,blank #if led off,branch to blank(so no color added to led)
            sw x9,0(x6) #else,if led on,store x9 color onto led
            blank:
        addi x22,x22,-1 #decrement counter 
        addi x23,x23,4 #increment sequence array
        addi x6,x6,4 #increment led matrix 1 pointer(the dashboard)   
        bne x22,x0,loop2 #loop till counter=0     
    beq x0,x0,exit2 #exit to end after exicuting pattern
    color2:
    li x25,0x00ffffff #background color for p2 
    la x23,p2 #load p2 sequence and then same as p1 above
        loop3:
            lw x24,0(x23)
            sw x25,0(x6)
            beq x24,x0,blank1 
            sw x9,0(x6)
            blank1:
        addi x22,x22,-1
        addi x23,x23,4
        addi x6,x6,4    
        bne x22,x0,loop3      
    beq x0,x0,exit2
    exit2: 
addi x6,x6,-160 #decrement led matrix 1 pointer back to first led 
jalr x0,x1,0

checkwin: 
    xor x26,x9,x10 #store previous player color
    la x27,arr #load arr adress
    li x28,9 #ctr
    li x29,0 #player moves word(stores 1 if player moved here and o if hasnt)
    li x30,1 #1 to shift through all 9 possible player moves so can be added wherever necessary
    loop4:
        lw x31,0(x27) #load words from arr
        bne x31,x26,notsamecolor #if equal to previousplayer color=>previous player move
        or x29,x29,x30 #add to player move word(or also adds it as 0or1 = 0+1 & 0or0 = 0+0)
        notsamecolor:
        slli x30,x30,1 #shift 1 to next position (to add if next position played by player)
        addi x27,x27,4 #increment arr pointer
        addi x28,x28,-1 #decrement counter
    bne x28,x0,loop4 #loop till counter =0 
    la x27,wins #load wins adress to x27
    li x26,8 #load counter=8,since 8 possible win cases
    loop5:
        lw x28,0(x27) #load win cases one by one
        and x30,x28,x29 #and win case with player move word,so we know if player has moved in all positions of that win case
        bne x30,x28,notwinseq #if player had moved in all positions of that win case,then upon anding,we will still have all 1s as 1 and all 0s as 0,ie the same as the win case
        add x11,x0,x28 #if won,store winning case in game loop control var x11
        beq x0,x0,exit3 #if won,exit checking win cases
        notwinseq: #if not yet won
        addi x26,x26,-1 #decrement counter
        addi x27,x27,4 #increment wins array pointer
    bne x26,x0,loop5 #loop till counter=0
    exit3:        
jalr x0,x1,0 #branch back to main program

exitfunc:

la x5,LED_MATRIX_0_BASE #3x3 tictactoe board
la x6,LED_MATRIX_1_BASE #5x8 dashboard 
la x7,arr #9 elements array storing player moves
la x8,SWITCHES_0_BASE #9 switches to play game

#sw x0,0(x8) #resetting switches didnt work,to be done manually

li x9,0x00fff000 #color 1
li x10,0xffffffff #color flipper

add x11,x0,x0 #if win,=!0,store winning sequence from wins
add x12,x0,x0 #whose turn, x0 if p1, 1 if p2

jal x1,dashboard

gameloop:
    lw x13,0(x8) #store previous switch config
    
    jal x1,setledmatrix

    waitforplayer: #waiting for a player to make a move
        la x18,SWITCHES_0_BASE
        lw x18,0(x18) #load new switch config
        beq x18,x13,notyetplayed #if config hasnt changed,recheck
        jal x1,checkplay #if config has changed,update move in arr
        beq x0,x0,played #after update,go out of wait loop
        notyetplayed: #keep waiting since player hasnt played yet
    beq x0,x0,waitforplayer #keep waiting till player has played
    played: #exit waiting loop after player played
    
    jal x1,dashboard #diplay next player on dashboard
    jal x1,checkwin #check if previous playe won
    
beq x11,x0,gameloop #inf game loop till someone wins

jal x1,setledmatrix #set latest led config

la x6,LED_MATRIX_1_BASE #5x8 dashboard 
la x7,arr #9 elements array storing player moves

xori x9,x9,0xffffffff #color of winning player
li x25,0x00000000 #background color for p1 ie yellow
li x31,0x0000ffff #color of p2,ie blue
bne x31,x9,bgwhite #if winning color not blue,dont change bg
li x25,0x00ffffff #if winning color blue,change background
bgwhite:
li x22,40 #counter to go through all 40 leds
la x23,w #load w pattern
        loop6:
            lw x24,0(x23) #load on/off from w seq
            sw x25,0(x6) #store background color by default
            beq x24,x0,blank2 #if led off,branch to blank(so no color added to led)
            sw x9,0(x6) #else,if led on,store x9 color onto led
            blank2:
        addi x22,x22,-1 #decrement counter 
        addi x23,x23,4 #increment sequence array
        addi x6,x6,4 #increment led matrix 1 pointer(the dashboard)   
        bne x22,x0,loop6 #loop till counter=0  
blink: #blink winning streak
    la x18,LED_MATRIX_0_BASE #3x3 tictactoe board
    li x19,9 #counter to check 9 spots in winnning streak x11 
    li x20,1 #shifting 1,to extract digit by digit of x11 streak
    
    offloop: #turning off leds of streak for blink
        and x21,x11,x20 #anding to extract digit by digit
        beq x21,x0,off #if 0,no need to blink
        sw x0,0(x18) #if 1,turn off to blink
        off:
        slli x20,x20,1 #shift to get next digit
        addi x18,x18,4 #increment led matrix pointer
        addi x19,x19,-1 #decrement counter
    bne x19,x0,offloop #loop till counter=0
    
    li x22,10000 #10000 counts delay loop
    delay:
    addi x22,x22,-1
    bne x22,x0,delay
    
    jal x1,setledmatrix #set back led matrix with all on as usual 
    
    li x22,10000 #again 10000 counts delay loop
    delay1:
    addi x22,x22,-1
    bne x22,x0,delay1
        
beq x0,x0,blink #infinite loop