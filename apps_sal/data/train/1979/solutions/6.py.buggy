class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ll = []
        def printAllKLength(set, k):
            n = len(set) 
            printAllKLengthRec(set, \"\", n, k)
        def printAllKLengthRec(set, prefix, n, k): 
            if (k == 0): 
                st = True
                for i in prefix:
                    if prefix.count(i) != set.count(i):
                        st = False
                        break
                if st == True and prefix not in ll:
                    ll.append(prefix)
                return prefix
            for i in range(n): 
                newPrefix = prefix + set[i] 
                printAllKLengthRec(set, newPrefix, n, k - 1) 
        set2=[]
        for i in arr:
            set2.append(str(i))
        k = 4
        printAllKLength(set2,k)
        ll.sort(reverse=True)
        s = ''
        for i in ll:
            if int(i[0])<2 and int(i[1])<10 and int(i[2]) <6 :
                s = i[0]+i[1]+\":\"+i[2]+i[3]
                break
            if int(i[0]) == 2 and int(i[1])<4 and int(i[2])<6:
                s = i[0] + i[1]+\":\"+i[2]+i[3]
                break
            else:
                continue
        return(s)
        
    
\t

        
                
            
        

                
                
            
            
            
            
            
                
        
        
        
