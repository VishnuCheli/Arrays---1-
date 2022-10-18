
#Time Complexity:: O(n*m)-traversing all the elements in the 2D matrix twice
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        #the neighbours directions
        directions = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
        
        
        #first pass
        
        for i in range(n):
            for j in range(m):
                count=0
                for r,c in directions: #processing neighbours
                    nr = r+i
                    nc = c+j
                    
                    #boundary check to only check for neighbours that are present inside the board
                    if nr>=0 and nr<n and nc>=0 and nc<m:
                        if board[nr][nc] == -1 or board[nr][nc] == 1: 
                            count+=1 #counts the alive cells
            
                if board[i][j] == 1: #if current cell is alive then check for underpopulation
                    if count<2 or count>3: 
                        board[i][j] = -1
                        
                else: #if current cell is dead check if reproduction of cell is possible
                    if count==3:
                        board[i][j] = 2
                        
        #second pass-to finalize the changes with 1's and 0's as the full board has been checked
        for i in range(n):
            for j in range(m):
                if board[i][j]==-1: #change all the -1 to 0
                    board[i][j] = 0
                    
                elif board[i][j] == 2: #change all the 2 to 1
                    board[i][j] = 1