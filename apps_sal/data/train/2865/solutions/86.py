def solution(string):
    pass
    negcount=-1
    solstring=""
    for i in range(len(string)):
        solstring+=string[negcount]
        negcount=negcount-1
    print(solstring)
    return(solstring)

