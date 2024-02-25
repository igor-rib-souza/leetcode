class Solution:
    def spiralOrder(self, matrix: List[List[int]],resultAux=None) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        if (resultAux):
            resultAux.extend(matrix[0][::])
        else:    
            resultAux = matrix[0][::]
        
        if (m == 1 or n == 1):
            for i in range(1,m):    
                resultAux.append(matrix[i][n-1])
            return resultAux
        
        for i in range(1,m):    
            resultAux.append(matrix[i][n-1])
            
        for j in range(n-2,-1,-1):
            resultAux.append(matrix[m-1][j])
            
        for k in range(m-2,0,-1):
            resultAux.append(matrix[k][0])
        

        if (m ==2 or n == 2):
            return resultAux
        else:
            return self.spiralOrder([row[1:-1] for row in matrix[1:m-1]],resultAux)
