import random
class TicTacToe:
    mark1='X'
    mark2='O'
    turn_count=0
    board = [
        [' ','|',' ','|',' '],
        ['-','+','-','+','-'],
        [' ','|',' ','|',' '],
        ['-','+','-','+','-'],
        [' ','|',' ','|',' '],
        ]
    filled = [False for i in range(9)]
    
    
    def printBoard(self):
        for i in self.board:
            for j in i:
                print(j,end='')
            print()
    
    def H_turn(self):
        inp=int(input("H-Turn input\n"))
        if(inp>9 or inp<1):
            print("Incorrect Input")
            self.H_turn()
        if(self.filled[inp-1]!=True):
            if(inp==1):
                self.board[0][0]=self.mark1
                self.filled[0]=True
            elif(inp==2):
                self.board[0][2]=self.mark1
                self.filled[1]=True
            elif(inp==3):
                self.board[0][4]=self.mark1
                self.filled[2]=True
            elif(inp==4):
                self.board[2][0]=self.mark1
                self.filled[3]=True
            elif(inp==5):
                self.board[2][2]=self.mark1
                self.filled[4]=True
            elif(inp==6):   
                self.board[2][4]=self.mark1
                self.filled[5]=True
            elif(inp==7):
                self.board[4][0]=self.mark1
                self.filled[6]=True
            elif(inp==8):
                self.board[4][2]=self.mark1
                self.filled[7]=True
            elif(inp==9):
                self.board[4][4]=self.mark1
                self.filled[8]=True
        
        else:
            self.H_turn()
    
    def C_Turn(self):
        print('C-Turn')
        inp=int(random.randint(1, 9))
        print(inp)
        if(self.filled[inp-1]!=True):
            if(inp==1):
                self.board[0][0]=self.mark2
                self.filled[0]=True
            elif(inp==2):
                self.board[0][2]=self.mark2
                self.filled[1]=True
            elif(inp==3):
                self.board[0][4]=self.mark2
                self.filled[2]=True
            elif(inp==4):
                self.board[2][0]=self.mark2
                self.filled[3]=True
            elif(inp==5):
                self.board[2][2]=self.mark2
                self.filled[4]=True
            elif(inp==6):   
                self.board[2][4]=self.mark2
                self.filled[5]=True
            elif(inp==7):
                self.board[4][0]=self.mark2
                self.filled[6]=True
            elif(inp==8):
                self.board[4][2]=self.mark2
                self.filled[7]=True
            elif(inp==9):
                self.board[4][4]=self.mark2
                self.filled[8]=True
            else:
                print('Incorrect Input')
        else:
            self.C_Turn()
        
    def Start_Game(self):
        turn = random.randint(1, 2)
        if(turn==1):
            for i in range(5):
                self.H_turn()
                self.turn_count+=1
                self.printBoard()
                if(self.Check_Winner()==True or self.turn_count==9):
                    print('Winner Found!')
                    break
                self.C_Turn()
                self.turn_count+=1
                self.printBoard()
                
        else:
            for i in range(5):
                self.C_Turn()
                self.turn_count+=1
                self.printBoard()
                if( self.Check_Winner()==True or self.turn_count==9):
                    print('Winner Found!')
                    break
                self.H_turn()
                self.turn_count+=1
                self.printBoard()
                
    def Check_Winner(self):
        # 1st Row
        if((self.board[0][0]=='X' and self.board[0][2]=='X' and self.board[0][4]=='X')):
            print('H is Winner')
            return True
        
        elif(self.board[0][0]=='O' and self.board[0][2]=='O' and self.board[0][4]=='O'):
            print('C is Winner')
            return True
        
        # 2nd Row
        elif((self.board[2][0]=='X' and self.board[2][2]=='X' and self.board[2][4]=='X')):
            print('H is Winner')
            return True
        
        elif(self.board[2][0]=='O' and self.board[2][2]=='O' and self.board[2][4]=='O'):
            print('C is Winner')
            return True
        
        # 3rd Row
        elif((self.board[4][0]=='X' and self.board[4][2]=='X' and self.board[4][4]=='X')):
            print('H is Winner')
            return True
        
        elif(self.board[4][0]=='O' and self.board[4][2]=='O' and self.board[4][4]=='O'):
            print('C is Winner')
            return True
        
        # 1st Column
        elif((self.board[0][0]=='X' and self.board[2][0]=='X' and self.board[4][0]=='X')):
            print('H is Winner')
            return True
        
        elif(self.board[0][0]=='O' and self.board[2][0]=='O' and self.board[4][0]=='O'):
            print('C is Winner')
            return True
        
        # 2nd column
        elif((self.board[0][2]=='X' and self.board[2][2]=='X' and self.board[4][2]=='X')):
            print('H is Winner')
            return True
        
        elif(self.board[0][2]=='O' and self.board[2][2]=='O' and self.board[4][2]=='O'):
            print('C is Winner')
            return True
        
        # 3rd Column
        elif((self.board[0][4]=='X' and self.board[2][4]=='X' and self.board[4][4]=='X')):
            print('H is Winner')
            return True
        elif(self.board[0][4]=='O' and self.board[2][4]=='O' and self.board[4][4]=='O'):
            print('C is Winner')
            return True
        
        # 1st Diagonal
        elif((self.board[0][0]=='X' and self.board[2][2]=='X' and self.board[4][4]=='X')):
            print('H is Winner')
            return True
        elif(self.board[0][0]=='O' and self.board[2][2]=='O' and self.board[4][4]=='O'):
            print('C is Winner')
            return True
        
        # 2nd Diagonal
        elif((self.board[0][4]=='X' and self.board[2][2]=='X' and self.board[4][0]=='X')):
            print('H is Winner')
            return True
        elif(self.board[0][4]=='O' and self.board[2][2]=='O' and self.board[4][0]=='O'):
            print('C is Winner')
            return True
        
        else:
            return False
        
        
            
game = TicTacToe()    

game.printBoard()
game.Start_Game()
