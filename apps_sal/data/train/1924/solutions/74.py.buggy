class Solution:
    def isinterval(self,a,b):
        if abs(int(a)-int(b))<=60:
            return True
        return False
    def issame(self,a,b):
        if a!=b:
            return True
        return False
    
    def issamename(self,a,b):
        if a==b:
            return True
        return False
    def invalidTransactions(self, A: List[str]) -> List[str]:
        arr=[]
        index=0
        n=len(A)
        while index<n:
            arr.append(list(A[index].split(',')))
            index+=1
        
        arr=sorted(arr,key=lambda x:int(x[1]))
        visited=[True for i in range(n)]
        result=[]
        for i in range(n):
            if int(arr[i][2])>1000:
                result.append(\",\".join(arr[i]))
                visited[i]=False
            for j in range(i+1,n):    
                if self.isinterval(arr[i][1],arr[j][1]) and arr[i][3]!=arr[j][3] and arr[i][0]==arr[j][0]:
                    if visited[i]:
                        visited[i]=False
                        result.append(\",\".join(arr[i]))                    
                    if visited[j]:
                        visited[j]=False
                        result.append(\",\".join(arr[j]))                    
                    
                
        result=list(set(result))                                                       
                
        return result
            
        
