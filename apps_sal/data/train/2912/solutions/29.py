def find_multiples(integer, limit):
    list=[]
    for i in range(1, limit+1):
        if i * integer <= limit:
            list.append(i*integer)
    return list# Your code here!
