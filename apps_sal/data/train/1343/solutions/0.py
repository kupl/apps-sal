# cook your dish here
def check_equal(a, b):
    index = 0
    for i in a:
        while index < len(b) and i != b[index]:
            index += 1
        if(index >= len(b)):
            return False
        index += 1
    return True


def Dob_String(n):
    size = len(n)
    midpoint = size // 2
    if(check_equal(n[0:midpoint], n[midpoint:size])):
        return("YES")
    elif(size % 2 != 0 and check_equal(n[midpoint + 1:size], n[0:midpoint + 1])):
        return("YES")
    else:
        return("NO")


T = int(input())
for _ in range(T):
    n = input()
    if(len(n) > 1):
        print(Dob_String(n))
    else:
        print("NO")
