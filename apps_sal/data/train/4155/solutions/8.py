dictio = {"0":"0","1":"1","6":"9","9":"6","8":"8"}
def solve(a, b):
    return sum(1 for i in range(a,b) if transf(i))

def transf(n):
    n = str(n)
    for i,j in enumerate(n):
        if j not in dictio:
            return False
        elif dictio[j] != n[-i-1]:
            return False
    return True
