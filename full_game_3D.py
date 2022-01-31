#Computer ttt
import multiplayer_3D as ttt
import check_win_3D as win
import bot_strategies_and_code_3D as bot
import matplotlib.pyplot as plt

def graph_bot_data(data):
    win_tie = ['Bot 1 Wins','Bot 2 wins','Tied']

    plt.bar(win_tie, data)
    plt.title('Game result')
    plt.xlabel('Game result ')
    plt.ylabel('Number of games')
    plt.show()

def single_player_play_game():
    grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
    print("Welcome to single player 3D tic tac toe against bot")
    print("Please chose symbol first")
    player_symbol = ttt.getSymbol()
    print("Chose symbol for bot ")
    while True: #loop in case same symbol
        bot_symbol = ttt.getSymbol()
        if player_symbol==bot_symbol:
            print("Bot symbol cannot be the same as yours")
        else:
            break
    print("")
    print("""Instructions
Moves are determined by coordinates in the form 'x,y,z' 
The first cooridinate is the plane from top to bottom
The second coordinate is the row from top to bottom
The third coordinate is the column from left to right
I.e 1,1,1 would be the left uppermost move""")


    ttt.printGrid(grid) #initial board
    allplayer1moves = [] #for memory
    allplayer2moves= [] #for memory 
    while True:

        print("Player:")
        player1move=ttt.getCoordinates(grid) #get coordinates
        allplayer1moves.append(player1move) #store move in list
        grid = ttt.mark(grid,player_symbol,player1move) #implement the move
        #ttt.printGrid(grid) #show grid 

        if win.check_all_wins(grid,player_symbol):
            ttt.printGrid(grid)
            print("Player wins! ")
            #print(grid)
            break
        
        bot_move = bot.bot_decide_move(grid,bot_symbol,player_symbol)
    
        allplayer2moves.append(bot_move)
        grid =ttt.mark(grid,bot_symbol,bot_move)
        ttt.printGrid(grid) #show grid


        print("Bot moved: " + str(bot_move))

        if win.check_all_wins(grid,bot_symbol): #bot win?
            #ttt.printGrid(grid)
            print("Bot wins! ")
            break

        if ttt.check_tied_game(grid):
            print("Game tied! ")
            break

        choice = input("Press 'q' to quit or 'b' to undo ") #choice to end or undo
        if  choice == 'q': #end game
            print("Game ended")
            print(grid)
            break

        if choice == 'b': #go back
            goBack = int(input("Enter number of times to go back "))
            if goBack>len(allplayer2moves): #cant go back that many moves
                print('Invalid choice, keep playing')
            else: 
                for x in range(goBack): #make the last move empty
                    grid = ttt.mark(grid,'',allplayer1moves[-1]) 
                    grid = ttt.mark(grid,'',allplayer2moves[-1])
                    allplayer1moves.pop() #then delete the move from the memory 
                    allplayer2moves.pop()
            #print(allplayer1moves)
            #print(allplayer2moves)
                ttt.printGrid(grid) #show new grid after going back moves

def single_player_bot_move_first_play_game2():
    grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
    print("Welcome to single player 3D tic tac toe against bot")
    print("Please chose symbol first")
    player_symbol = ttt.getSymbol()
    print("Chose symbol for bot ")
    while True: #loop in case same symbol
        bot_symbol = ttt.getSymbol()
        if player_symbol==bot_symbol:
            print("Bot symbol cannot be the same as yours")
        else:
            break
    print("")
    print("""Instructions
Moves are determined by coordinates in the form 'x,y,z' 
The first cooridinate is the plane from top to bottom
The second coordinate is the row from top to bottom
The third coordinate is the column from left to right
I.e 1,1,1 would be the left uppermost move""")


    #ttt.printGrid(grid) #initial board
    allplayer1moves = [] #for memory
    allplayer2moves= [] #for memory 
    while True:
        bot_move = bot.bot_decide_move(grid,bot_symbol,player_symbol)
          
        allplayer2moves.append(bot_move)
        grid =ttt.mark(grid,bot_symbol,bot_move)
        ttt.printGrid(grid) #show grid
        print("Bot moved: " + str(bot_move))

        if win.check_all_wins(grid,bot_symbol): #bot win?
            #ttt.printGrid(grid)
            print("Bot wins! ")
            break

        print("Player:")
        player1move=ttt.getCoordinates(grid) #get coordinates
        allplayer1moves.append(player1move) #store move in list
        grid = ttt.mark(grid,player_symbol,player1move) #implement the move
        #ttt.printGrid(grid) #show grid 

        if win.check_all_wins(grid,player_symbol):
            ttt.printGrid(grid)
            print("Player wins! ")
            #print(grid)
            break

        if ttt.check_tied_game(grid):
            print("Game tied! ")
            break
        
        choice = input("Press 'q' to quit or 'b' to undo ") #choice to end or undo
        if  choice == 'q': #end game
            print("Game ended")
            #print(grid)
            break

        if choice == 'b': #go back
            goBack = int(input("Enter number of times to go back "))
            if goBack>len(allplayer2moves): #cant go back that many moves
                print('Invalid choice, keep playing')
            else: 
                for x in range(goBack): #make the last move empty
                    grid = ttt.mark(grid,'',allplayer1moves[-1]) 
                    grid = ttt.mark(grid,'',allplayer2moves[-1])
                    allplayer1moves.pop() #then delete the move from the memory 
                    allplayer2moves.pop()
            #print(allplayer1moves)
            #print(allplayer2moves)
                ttt.printGrid(grid) #show new grid after going back moves
    
def spectate_bots():
    grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
    #ttt.printGrid(grid) #initial board
    all_bot_1_moves = [] #for memory
    all_bot_2_moves= [] #for memory


    print("Welcome to 3D tic tac toe: Spectating bots")
    print("Please chose symbol for bot 1")
    bot_1_symbol = ttt.getSymbol()
    print("Chose symbol for bot 2")
    while True: #loop in case same symbol
        bot_2_symbol = ttt.getSymbol()
        if bot_1_symbol==bot_2_symbol:
            print("Bot 1 symbol cannot be the same as bot 2")
        else:
            break
    
    while True: #game
        
        bot_move = bot.bot_decide_move(grid,bot_1_symbol,bot_2_symbol)

        all_bot_1_moves.append(bot_move)
        grid =ttt.mark(grid,bot_1_symbol,bot_move)

        if win.check_all_wins(grid,bot_1_symbol): #bot 1 win?
            ttt.printGrid(grid)
            print("Bot 1 moved: " + str(bot_move))
            print("Bot 1 wins! ")
            break

#REPEAT BUT FOR BOT 2 _______________________________________________________________
        
        bot_2_move = bot.bot_decide_move(grid,bot_2_symbol,bot_1_symbol)

        all_bot_2_moves.append(bot_2_move)
        grid =ttt.mark(grid,bot_2_symbol,bot_2_move)
        ttt.printGrid(grid) #show grid

        if win.check_all_wins(grid,bot_2_symbol): #bot 2 win?
            #ttt.printGrid(grid)
            print("Bot 2 wins! ")
            break
#___________________________________________________________________________________
        
        print("Bot 1 moved: " + str(bot_move))
        print("Bot 2 moved: " + str(bot_2_move))


        if ttt.check_tied_game(grid):
            print("Game tied! ")
            break

        choice = input("Press 'q' to quit or 'b' to undo ") #choice to end or undo
        if  choice == 'q': #end game
            print("Game ended")
            #print(grid)
            break

        if choice == 'b': #go back
            goBack = int(input("Enter number of times to go back "))
            if goBack>len(all_bot_2_moves): #cant go back that many moves
                print('Invalid choice, keep playing')
            else: 
                for x in range(goBack): #make the last move empty
                    grid = ttt.mark(grid,'',all_bot_1_moves[-1]) 
                    grid = ttt.mark(grid,'',all_bot_2_moves[-1])
                    all_bot_1_moves.pop() #then delete the move from the memory 
                    all_bot_2_moves.pop()
                ttt.printGrid(grid) #show new grid after going back moves

def spectate_one_bot(): #used for debugging/analysis
    #technically single player but be able to skip moves 
    #purpose is to analyze bot's moves without always having to play
    grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
    #ttt.printGrid(grid) #initial board
    all_bot_1_moves = [] #for memory
    all_player_moves= [] #for memory


    print("Welcome to 3D tic tac toe: Spectating one bot")
    print("Please chose symbol for bot")
    bot_1_symbol = ttt.getSymbol()
    print("Chose symbol for player")
    while True: #loop in case same symbol
        player_symbol = ttt.getSymbol()
        if bot_1_symbol==player_symbol:
            print("Bot symbol cannot be the same as player")
        else:
            break
    
    while True: #game
        
        bot_move = bot.bot_decide_move(grid,bot_1_symbol,player_symbol)

        all_bot_1_moves.append(bot_move)
        grid =ttt.mark(grid,bot_1_symbol,bot_move)
        ttt.printGrid(grid) #show grid 


        if win.check_all_wins(grid,bot_1_symbol): #bot 1 win?
            #ttt.printGrid(grid)
            print("Bot 1 wins! ")
            break
        
#__________________________________________________________________________________

        print("bot moved " , bot_move)

        if input("Press 'p' to play ") =='p':
            player1move=ttt.getCoordinates(grid) #get coordinates
            all_player_moves.append(player1move) #store move in list
            grid = ttt.mark(grid,player_symbol,player1move) #implement the move
            ttt.printGrid(grid) #show grid 

            if win.check_all_wins(grid,player_symbol):
                ttt.printGrid(grid)
                print("Player wins! ")
                #print(grid)
                break
        
#___________________________________________________________________________________

        if ttt.check_tied_game(grid):
            print("Game tied! ")
            break

def collect_data(number_of_games):
    bot_1_wins = 0
    bot_2_wins = 0
    tied_games = 0

    for x in range(number_of_games):
        grid  = [[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']],[['','','',''],['','','',''],['','','',''],['','','','']]]
        #ttt.printGrid(grid) #initial board
        all_bot_1_moves = [] #for memory
        all_bot_2_moves= [] #for memory

        bot_1_symbol = 'x'
        bot_2_symbol = 'o'
        
        while True: #game
            
            bot_move = bot.bot_decide_move(grid,bot_1_symbol,bot_2_symbol)

            all_bot_1_moves.append(bot_move)
            grid =ttt.mark(grid,bot_1_symbol,bot_move)

            if win.check_all_wins(grid,bot_1_symbol): #bot 1 win?
                #ttt.printGrid(grid)
                #print("Bot 1 moved: " + str(bot_move))
                print("Bot 1 wins! ")
                bot_1_wins +=1
                break

    #REPEAT BUT FOR BOT 2 _______________________________________________________________
            
            bot_2_move = bot.bot_decide_move(grid,bot_2_symbol,bot_1_symbol)

            all_bot_2_moves.append(bot_2_move)
            grid =ttt.mark(grid,bot_2_symbol,bot_2_move)
            #ttt.printGrid(grid) #show grid

            if win.check_all_wins(grid,bot_2_symbol): #bot 2 win?
                #ttt.printGrid(grid)
                print("Bot 2 wins! ")
                bot_2_wins +=1
                break
    #___________________________________________________________________________________
            
            #print("Bot 1 moved: " + str(bot_move))
            #print("Bot 2 moved: " + str(bot_2_move))


            if ttt.check_tied_game(grid):
                print("Game tied! ")
                tied_games+=1
                break
    
    return [bot_1_wins,bot_2_wins,tied_games]


def play_again():
    while True:
        skip = False
        choice= input("Press 'a' for multiplayer player, 'b' for single player, and 'c' for spectating bots: ")
        if choice == 'a':
            ttt.play_multiplayer_game()
        elif choice == 'b':
            choice2 = input("Press 'a' to move first or 'b' to move second (default you move first): ")
            if choice2 =='b': 
                single_player_bot_move_first_play_game2()
            elif choice2 == 's': #analysis
                spectate_one_bot()
            elif choice2 == 'd': #collect data
                games_data = collect_data(int(input("Enter number of games: ")))
                graph_bot_data(games_data)
            else:
                single_player_play_game()
        elif choice == 'c':
            spectate_bots()
        else:
            print("Please enter a choice")
            skip = True
        if not skip and input("Would you like to play again? (y/n) ")=='n':
            break


play_again()
input("Press enter to end")