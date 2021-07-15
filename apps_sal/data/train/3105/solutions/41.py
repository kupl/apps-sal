def count_sheep(n):
    i = 1
    ans = ""
    while i <=n:
        ans = ans + str(i)+ " " + "sheep..."
        i = i+1
    return ans

