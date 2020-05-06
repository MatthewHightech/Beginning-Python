import numpy as np

def findSum(matrix): 
    sum = 0 
    for row in range(0, 10):
        for cell in range(0, 10):
            sum += int(matrix[row][cell])
    print(sum)

matrix = np.random.random ([10,10]) * 10
matrix.astype(int)

findSum(matrix)
        

