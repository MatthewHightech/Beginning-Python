samples = input()

for i in range(int(samples)):
    error = 0 
    bases = input()
    string = input()
    newString = "" 
    for j in range(len(string)):
        if string[j] == 'T':
            newString += 'A'
        elif string[j] == 'A':
            newString += 'T'
        elif string[j] == 'C':
            newString += 'G'
        elif string[j] == 'G':
            newString += 'C'
        else:
            print ("Error RNA nucleobases found!")
            error = 1
            break
    if error == 0: 
        print(newString)
    elif error == 1:
        continue