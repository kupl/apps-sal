class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        count02 = 0
        count03 = 0
        count05 = 0
        count09 = 0
        newstr = \"\"
        for i in range(4):
            if arr[i]<=2:
                count02 += 1
            if arr[i]<=3:
                count03 += 1 
            if arr[i]<=5:
                count05 += 1
        if count02 == 0 or (2 in arr and count03 == 1) or (2 in arr and count02 == 1 and count05 <= 2) or count05 <= 1 :
            return \"\"
        if 2 in arr and count05 > 2:
            newstr = newstr + str(2)
            arr.remove(2)
        elif count05 <=2 or 2 not in arr:
            if 1 in arr:
                newstr = newstr + str(1)
                arr.remove(1)
            elif 0 in arr:
                newstr = newstr + str(0)
                arr.remove(0)
            else:
                return \"\"
        if newstr[0] != \"2\":
            for i in range(9, -1, -1):
                if i in arr:
                    newstr = newstr+ str(i) + \":\"
                    arr.remove(i)
                    break
        else:
            for i in range(3, -1, -1):
                if i in arr:
                    newstr = newstr+ str(i) + \":\"
                    arr.remove(i)
                    break
    
        for i in range(5, -1, -1):
            if i in arr:
                newstr = newstr+ str(i)
                arr.remove(i)
                break
        if len(newstr) <= 3:
            return \"\"
        newstr = newstr + str(arr[0])
            
        return newstr
    
