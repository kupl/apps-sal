def array_madness(a,b):
    farr = 0
    sarr = 0
    for i in a : 
        n = i ** 2
        farr = farr + n
    for j in b :
        o = j ** 3
        sarr = sarr + o
    if farr > sarr :
        return True
    if sarr >= farr :
        return False

