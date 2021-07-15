def increment_string(string):
    numbers=''
    others=''
    if string == '':
        return '1'        
    for i in range(len(string)-1,-1,-1):     #separates the numbers and the others
        if '0' <= string[i] <= '9':
            numbers = string[i] + numbers
        if string[i] < '0' or string[i] > '9':
            others = string[:i+1]
            break
    if numbers == '':           #the string doesnt contain numbers (in the end)
        return others + '1'
    i=0
    while numbers[i] == '0' and i < len(numbers)-1:        #to separate 0's from numbers
        i=i+1
    zeros = ''
    if i != 0:                                              #separates 0's from numbers
        zeros = numbers[:i]
        numbers = numbers[i:]
    if len(numbers) != len(str(int(numbers)+1)) and zeros != '':       # ex: if 099 goes to 100 and not 0100     removes one 0 if needed
        zeros = zeros[:-1]
    numbers = str(int(numbers)+1)         #increment
    return others + zeros + numbers
