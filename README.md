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


2)  **TicTacToe written in Python**
- SETUP:
  + Packages required: tkinter(if not installed, pip install using "pip install tkinter")
  + Save both tictactoe_main and tictactoe_computer file in same directory and run the main file. Game widow will open.
   
- PLAYING:
  + Game is initially in PvP or Player vs Player mode. 2 players can alternatively click squares to play. Game also has a PvC or Player vs Computer mode where a player can play and the computer will play a move as player 2.
  + Undo- Cancels last played move in PvP mode, and cancels the last player move along with computer's counter move in PVC mode.
  + Reset- Empty's board to start fresh in whichever is the current mode
  + Mode- Toggles the current mode to other mode, while also emptying board to start game afresh in the new mode.
 
- CUSTOMISATION-BASIC:
  + Default board color - change using variable "default_bg" in main file.
  + Player colors and symbols - change using variables "p1"(player 1's symbol), "p1_bg"(player 1's color), "p2"(player 2's symbol) and "p2_bg"(player 2's color).
  + Displayed messages - Change the default messages supplied to "update_screen" function in the functions - "toggle_mode", "reset", "undo" and "button_clicked".
  + Window name,size,etc... can be adjusted using respective tkinter funtions.
 
- CUSTOMISATION-ADVANCED:
  + Changing Computer decision making algorithm - change the "next_move" function in the computer file. This function accepts 3 args, namely comp(a list of integers between 0-8 indicating the squares occupied by the player p1), comp(a list of integers between 0-8 indicating the squares occupied by the computer) and available(a list of integers between 0-8 not occupied by either the board or the computer). The function must return a single integer indicating the square to be played by the computer based on the current spots taken and available. The logic for this decision making is totally upto you.
  + Adding modes - New modes can be added using the following changes:
    1) Edit "toggle_mode" to include new mode
    2) Add new mode's case in functions "button_state", "reset", "undo" and "button_clicked"
    3) May also have to edit chckwin if needed

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
