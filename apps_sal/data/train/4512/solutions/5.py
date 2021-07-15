def find_num(n):
    found, lastComplete, lastFound = {0}, 0, 0
    while len(found) <= n:
        lastDigits = set(str(lastFound))
        curr = lastComplete+1
        while curr in found or set(str(curr)) & lastDigits:
            curr += 1
        lastFound = curr
        found.add(lastFound)
        lastComplete += lastFound == lastComplete+1
    return lastFound
