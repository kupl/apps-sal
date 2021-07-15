class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        n=label
        change=False
        stack=[]
        index=-1
        while(n>0):
            stack.append(n)
            n=int(n/2)
            index+=1
        check=False
        output=[]
        while(stack):
            p=stack.pop(0)
            if not check:
                output.append(p)
            else:
                start=pow(2,index)
                end=pow(2,index+1)-1
                while(start<=end):
                    if p==start:
                        output.append(end)
                        break
                    elif p==end:
                        output.append(start)
                        break
                    start+=1
                    end-=1
            check=not check
            index-=1
        return output[::-1]

