class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        mp = {}
        l = []
        for i, j in zip(keyName, keyTime):
            temp = j.split(\":\")
            if i not in mp:
                mp[i] = []
            mp[i] += [[float(temp[0]), float(temp[1])]]
        for key, value in mp.items():
            value.sort()
            if(len(value) < 3):
                continue
            for i in range(len(value)-2):
                if(value[i+2][0] - value[i][0] < 1.0):
                    l.append(key)
                    break
                elif(value[i+2][0] - value[i][0] == 1 and value[i+2][1] - value[i][1] <= 0):
                    l.append(key)
                    break
        l.sort()
        return l
