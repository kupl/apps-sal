class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        mp ={}
        res=[]
        
        for i,v in enumerate(keyName):
            if v in mp:
                mp[v].append(keyTime[i])
            else:
                mp[v]=[keyTime[i]]
        for l in mp:
            n=len(mp[l])
            if n<3:
                continue
            t = mp[l]
            t.sort()
            count =0
            for i in range(n):
                if i+2 <n:
                    dh = int(t[i+2].split(':')[0])-int(t[i].split(':')[0])
                    dm = int(t[i+2].split(':')[1])-int(t[i].split(':')[1])

                    if dh >= 2:
                        continue
                    elif dh == 1 and dm>0:
                        continue
                    else:
                        res.append(l)
                        break
        res.sort()
        return res
    
        def hour(hr):
            return int(hr.split(':')[0])
        def minuu(hr):
            return int(hr.split(':')[1])
        def checkTime(self,name)-> bool:
            n=len(mp[name])
            if n<3:
                return False
            t = mp[name]
            t = t.sort()
            count =0
            
            for i,v in enumerate(t):
                if i+2 <n:
                    dh = self.hour(t[i+2])-self.hour(v)
                    dm = self.minuu(t[i+2])-self.minuu(v)
                    if dh >= 2:
                        return False
                    elif dh == 1 and dm>0:
                        return False
                    else:
                        return True

