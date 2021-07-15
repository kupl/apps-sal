def decipher_message(message):
    from math import sqrt
    if len(message) == 0:
        return message
    else:
        lists, output = [],[] #empty lists for storing column values and output message
        x = int(sqrt(len(message))) #denotes the column/row length
        for i in range(0,len(message),x):
            lists.append(list(message[i:i+x])) #simulates the n x n grid 
        for i in range(len(lists)):
            for j in range(len(lists)): #iterates over each grid element
                output.append(lists[j][i]) #appends to output list
        return ''.join(output) #decoded message

