class Solution:
    def longestAwesome(self, s: str) -> int:
        
        # See suggestion in solutions of using approach of leetcode 1371:
        # Find longest substring containing even number of vowels.
        # Which is also same approach as leetcode 1, two sum:
        # You record status at every index, and keep it in dictionary of
        # prior indices, so you can check for any elements in dictionary
        # that have status such that sequence between earlier index
        # and current value meets the needed requirement
        
        # Complicated thing here is to determine earlier \"status\" values
        # that mean that current index is appropriate
        
        maxV = 0
        
        c = [0 for i in range(10)]
        counts = []
        c[int(s[0])] += 1
        counts.append(c[:])
        for i in range(1, len(s)):
            c = counts[-1][:]
            c[int(s[i])] = (c[int(s[i])] + 1) % 2
            counts.append(c)
        counts = [[0,0,0,0,0,0,0,0,0,0]] + counts
        #print(counts)
              
        d = {tuple(counts[0]):0} # d has tuple of the 10 counts, mapping it to first index where those counts found in array counts
              
        # remember to use i+1 in finding values in counts, since we added
        # the extra value at position 0.
        for i in range(len(s)):
            current = counts[i+1][:]
              # j is the one digit that can have odd number of occurences
                # and remember to include possibility that all digits are even numbers!!!
            for j in range(10): # for each j, creating another newCurrent
                newCurrent = current[:]
                newCurrent[j] = (current[j]+1) % 2
                newCurrent = tuple(newCurrent)
                if newCurrent in d:
                    ind = d[newCurrent]
                    maxV = max(maxV, i+1 - ind)
            if tuple(current) in d:
                ind = d[tuple(current)]
                maxV = max(maxV, i+1 - ind)
            else:
                d[tuple(current)] = i+1
        
        return maxV        
                          
        # My prior proposed answer, maybe during contest?
        # That gave correct answer, but was TLE
        
        newS = \"\"
        d = {}
        
        def xor(l1,l2):
            res = []
            for i in range(10):
                res.append(l1[i] ^ l2[i])
            return res
        
        counts = [[0 for i in range(10)] for j in range(len(s)+1)]
        counts[1][int(s[0])] += 1 # added extra \"all zero counts at left end, to deal with index -1 later\"
        for i in range(1,len(s)):
            counts[i+1] = counts[i][:]
            counts[i+1][int(s[i])] = abs(counts[i+1][int(s[i])]-1)
        bestAns = 1
        for i in range(len(s)-1, -1, -1):
            if i < bestAns:
                break
            for j in range(0, i+1):
                if i - j < bestAns:
                    break
                ans = xor(counts[i+1], counts[j])
                oneCount = [1 for i in ans if i == 1]
                if sum(oneCount) <= 1:
                    bestAns = max(bestAns, i+1 - j)
        return bestAns
