class Solution:
    def countLargestGroup(self, n: int) -> int:
        l = [0]*40
        for i in range(1,n+1):
            s = str(i)
            sum = 0
            for j in range(len(s)):
                sum+=int(s[j])
            # print(sum)
            l[sum]+=1
        mm =  max(l)
        c = 0
        for i in range(len(l)):
            if(l[i]==mm):
                c+=1
        return c

