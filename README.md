# tictactoe
A repository of the classic game of tic-tac-toe in multiple different languages

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1)  **TicTacToe written in RISCV**
- SETUP:
  + Open the ripes simulator and paste the code in the editor as an 'assembly' type input.
  + Go to the I/O section and create the following:
   1) A 3x3(height:3,width:3) LED Matrix 'LED Matrix 0' : FOR THE MAIN GAME BOARD
   2) A 5x8(height:5,width:8) LES Matrix 'LED Matrix 1' : FOR THE DASHBOARD TO DISPLAY PLAYER TURN AND WIN
   3) A 9 Switch array 'Switches 0' : FOR PLAYERS TO MAKE MOVES ON THE GAME BOARD. Make sure all switches start off before running code.
- PLAYING:
  + Click f8 to Exicute Simulator without updating UI for fast exicution (use the '>>' instead of the green '>' arrow)
  + The game will automatically start with player 1's turn, who is by default yellow. Once a switch is toggled,the correspoding led on the game board turns yellow and it becomes player 2's turn. turns alternate each time a player plays, and if someone wins, a 'W' is displayed on the dashboard(color matching the winning player) and the sequence blinks indicating the winner's 3 in a row set.
- CUSTOMISATION:
  + Player Colors - Colors of the players can be modified in the 'dashboard' function changing the backgroung and player colors of p1 and p2 by setting the 8 bit hexadecimal value to the desired color.Default colors:
    1) p1 background:0x00000000 (black)
    2) p1 color:0x00fff000 (yellow)
    3) p2 background:0x00ffffff (white)
    4) p2 color:0x00000fff (blue)(p2 color is set as inverse of p1's color to reduce variables, so p2 has to be modified with p1)
  + Player Pattern - Player pattern on dash board is set to 'P1' and 'P2' as a 5x8 pattern on the dashboard, this can be modified in the variables p1 and p2 in the .data section.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
