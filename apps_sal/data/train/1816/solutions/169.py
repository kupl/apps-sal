class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        arr=sorted(zip(keyName,keyTime))
        person=arr[0][0]
        queue=[]
        res=[]
        flag=False
        def diff(t1,t2):
            t1=int(t1[:2])*60+int(t1[3:])
            t2=int(t2[:2])*60+int(t2[3:])
            return t2-t1
            
        for i in range(len(arr)):
            if arr[i][0]!=person:
                person=arr[i][0]
                queue=[arr[i][1]]
                flag=False
            else:
                if flag==True:
                    continue
                queue.append(arr[i][1])
                while(diff(queue[0],arr[i][1])>60):
                    queue.pop(0)
                if len(queue)>=3:
                    res.append(person)
                    flag=True
        return res

