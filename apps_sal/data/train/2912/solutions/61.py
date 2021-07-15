def find_multiples(integer, limit):
    ans = []
    count = integer
    while count <= limit:
        ans.append(count)
        count += integer
    return ans
