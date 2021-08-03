class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points)<4:
            return
        minimum=float(\"inf\")
        length=defaultdict(list)
        for x,y in points:
            length[x].append(y)
         
        print(length)
        breadth={}
        
        for x in sorted(length):
            values=length[x]
            print(values)
            values.sort()
            if len(values)<2:
                continue
            for i in range(0,len(values)-1):
                for j in range(i+1,len(values)):
                    if (values[i],values[j]) in breadth:
                        minimum=min(minimum,(x-breadth[(values[i],values[j])])*(values[j]-values[i]))
                        
                    breadth[(values[i],values[j])]=x
        
        if minimum==float(\"inf\"):
            return 0
        else:
            return minimum
        
