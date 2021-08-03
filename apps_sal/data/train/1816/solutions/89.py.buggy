from collections import defaultdict
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        self.unique = set()
        self.d = defaultdict(list)
        for i in range(len(keyName)):
            if keyName[i] not in self.unique:
                r = list(keyTime[i].split(\":\"))
                self.d[keyName[i]].append(r)
                if len(self.d[keyName[i]])>=3:
                    self.d[keyName[i]].sort()
                    # print(self.d[keyName[i]])
                    for j in range(len(self.d[keyName[i]])-2):
                        hr1,mn1 = self.d[keyName[i]][j]
                        # print(\"1\",hr1,mn1)
                        hr2,mn2 = self.d[keyName[i]][j+2]
                        # print(\"2\",hr2,mn2)
                        if int(hr1) == int(hr2):
                            self.unique.add(keyName[i])
                            break
                        elif int(hr2)-int(hr1)==1:
                            if int(mn1)-int(mn2)>=0:
                                self.unique.add(keyName[i])
                                break
        
        return sorted(list(self.unique))
