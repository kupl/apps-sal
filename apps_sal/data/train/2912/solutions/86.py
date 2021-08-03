def find_multiples(integer, limit):
    numList = []
    count = 1
    howMuch = int(limit / integer)
    for x in range(howMuch):
        numList.append(integer * count)
        count += 1
    return numList
