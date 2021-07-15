try:
    from collections import Counter
    from sys import stdin, stdout
    def get_ints(): return map(int, stdin.readline().strip().split())
    def get_list(): return list(map(int, stdin.readline().strip().split()))
    def get_string(): return stdin.readline().strip()
    def get_singleInt(): return int(stdin.readline())
    def main():
        testCases=get_singleInt()
        a=reqNumbers()
        for i in range(testCases):
            limit=get_singleInt()
            for i in range(limit):
                print(a[i],end=" ")
            print()
            print(sum(a[:limit]))

    def reqNumbers():
        reqList = [1, 2, 4, 8, 13, 21, 31, 45, 66, 81, 97, 123, 148, 182, 204, 252, 290, 361, 401, 475, 565, 593, 662, 775, 822, 916, 970, 1016, 1159, 1312, 1395, 1523, 1572, 1821, 1896, 2029, 2254, 2379, 2510, 2780, 2925, 3155, 3354, 3591, 3797, 3998,
                   4297, 4433, 4779, 4851, 5123, 5243, 5298, 5751, 5998, 6374, 6801, 6925, 7460, 7547, 7789, 8220, 8503, 8730, 8942, 9882, 10200, 10587, 10898, 11289, 11614, 11876, 12034, 12931, 13394, 14047, 14534, 14901, 15166, 15688, 15972, 16619, 17355]
        return reqList
        """uniqueList=[]#for storing all such values
        lis1=[]#for storing all the sum values and double of those values
        uniqueList.append(1)
        uniqueList.append(2)
        uniqueList.append(4)
        lis1.append(2)
        lis1.append(4)
        lis1.append(8)
        lis1.append(3)
        lis1.append(5)
        lis1.append(6)
        for number in range(5,100000):
            lis2 = []  # for storing the sums obtained by summing with current denomination 
            x=number
            for i in range(len(uniqueList)):
                lis2.append(x+uniqueList[i])
            lis2.append(x+x)
            count=0
            for j in range(len(lis2)):
                f=lis2[j]
                if f in lis1:
                    pass
                else:
                    count=count+1
            if count==len(lis2):               
                uniqueList.append(x)
                lis1.append(x+x)
                for k in range(len(uniqueList)-1):
                    lis1.append(x+uniqueList[k])
                print(x)
        print(len(uniqueList))
        return uniqueList"""

    def __starting_point():
        main()
except Exception:
    pass



__starting_point()
