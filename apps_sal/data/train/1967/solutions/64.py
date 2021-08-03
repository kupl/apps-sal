class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(len(S)):
            for j in range(len(S)):
                arr = []
                if(S[0:i + 1][0] == '0' and len(S[0:i + 1]) >= 2):
                    continue
                arr.append(int(S[0:i + 1]))
                if(S[i + 1:i + j + 1] != ''):
                    arr.append(int(S[i + 1:i + j + 1]))
                flag = 0
                k = i + j + 1
                while(k < len(S)):
                    if(len(arr) > 1):
                        val = arr[-1] + arr[-2]
                        if(k + len(str(val)) > len(S) or str(val) != S[k:k + len(str(val))]):
                            flag = 1
                            break
                        else:
                            k += len(str(val))
                            arr.append(val)
                    else:
                        flag = 1
                        break
                if(flag == 0):
                    if(len(arr) > 2):
                        for i in arr:
                            if(i < 0 or i > 2**31 - 1):
                                return []
                        return arr
        if(len(arr) <= 2):
            return []
        return arr
