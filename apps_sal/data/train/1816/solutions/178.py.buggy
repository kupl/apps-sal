class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def convertTime(time):
            time = time.split(\":\")
            return int(time[0]) * 60 + int(time[1])
        
        dict = {}
        for i in range(len(keyName)):
            dict[keyName[i]] = dict.get(keyName[i], []) + [keyTime[i]]
        
        output = []
        for k, v in sorted(dict.items()):
            v.sort()
            l = 0
            for r in range(len(v)):
                while convertTime(v[r]) - convertTime(v[l]) > 60:
                    l +=1
                if r - l + 1 == 3:
                    output.append(k)
                    break
        return output
                
                
            
                
