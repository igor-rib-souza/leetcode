class Solution:
    def spiralOrder(self, matrix: List[List[int]],resultAux=None) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        if (resultAux):
            result = resultAux
            result.extend(matrix[0][::])
        else:    
            result = matrix[0][::]
        
        if (m == 1 or n == 1):
            for i in range(1,m):    
                result.append(matrix[i][n-1])
            return result
        
        for i in range(1,m):    
            result.append(matrix[i][n-1])
            
        for j in range(n-2,-1,-1):
            result.append(matrix[m-1][j])
            
        for k in range(m-2,0,-1):
            result.append(matrix[k][0])
        

        if (m ==2 or n == 2):
            return result
        else:
            return self.spiralOrder([row[1:-1] for row in matrix[1:m-1]],result)
