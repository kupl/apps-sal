from collections import defaultdict as ddict
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        wordmap = ddict(int)
        arr = [\"\"]*len(names)
        
        for ind, word in enumerate(names):
            if word not in wordmap:
                arr[ind] = word
                wordmap[word]+=1
            else:
                cnt = wordmap[word]
                while word+\"({0})\".format(cnt) in wordmap:
                    cnt+=1
                arr[ind] = word+\"({0})\".format(cnt)
                wordmap[word]=cnt+1
                wordmap[word+\"({0})\".format(cnt)]+=1
        return arr
