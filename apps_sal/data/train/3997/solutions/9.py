def solve(s,k):
    count = 0
    l = s.split()
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            count += int(int(l[i]+l[j])%k == 0) + int(int(l[j]+l[i])%k == 0)
    return count
