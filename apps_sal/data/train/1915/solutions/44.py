def getstamps(s):
    stamps = []
    for i in range(0, len(s)):
        for j in range(len(s), -1, -1):
            if i + len(s)-j <len(s):
                stamp = '*'*i+s[i:j]+'*'*(len(s)-j)
                stamps.append(stamp)
    return stamps

def stampseq(s, t):
    stamps = getstamps(s)
    print(stamps)
    flag = True
    result = []
    while flag:
        flag = False
        for stamp in stamps:
            pos = t.find(stamp)
            while(pos != -1):
                result.append(pos)
                t = t[:pos] + '*'*len(s) + t[pos+len(s):]
                flag = True
                pos = t.find(stamp)
            if t == '*'*len(t):
                return reversed(result)
    return []
        
        
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        return stampseq(stamp, target)
