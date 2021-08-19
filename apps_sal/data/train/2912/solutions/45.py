def find_multiples(integer, limit):
    # Your code here!
    list = []
    for i in range(limit):
        i = i + 1
        count = i * integer
        if(count <= limit):
            list.append(count)
    return list
