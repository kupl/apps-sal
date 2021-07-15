def find_missing_number(sequence):
    if len(sequence) == 0:
        return 0
    myNumbers = sequence.split(" ")
    try:
        myNumbers = list(map(int,myNumbers))
        myNumbers.sort()
    except:
        return 1
    for i in range(0,len(myNumbers)):
        if (myNumbers[i] != (i+1)):
            return i +1
    return 0
