import numpy as np

def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1  

min = 0
max = 0
output = 0
arraySize = input()
array = []
inputA = input()
inputA = inputA.split()
for i in range(len(inputA)): 
    array.append(int(inputA[i]))
array.sort()
queries = input()
for i in range(int(queries)):
    output = 0
    query = input()
    query = query.split()
    command = int(query[0])
    min = int(query[1])
    #print("command: ", command)
    #print("compare value: ", min)
    binaryReturn = binarySearch(array, 0, len(array)-1, max)
    if binaryReturn == -1: 
        if command == 0:
            output = 0
            for i in range(len(array)):
                #print("array: ", array[i], " - i:", i)
                if array[i] >= min: 
                    output = len(array) - i
                    break
        elif command == 1: 
            output = 0
            for i in range(len(array)):
                #print("array: ", array[i], " - i:", i)
                if array[i] > min: 
                    output = len(array) - i
                    break
    else: 
        if command == 0: 
            output = (len(array) - binaryReturn) 
        elif command == 1:
            output = (len(array) - (binaryReturn + 1)) 
    print(output)
    
