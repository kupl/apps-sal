'''
\"aabcaca\"
 0123456
  x
 
devide conquer
先找到第一个stamp把string分成左右两部分（必须要）（On
然后从长到短用stamp的头match左边的部分，直到match到最头 如果不能到最头则退出
从长到短用stamp的尾巴match右边，直到match到尾巴，如果不能match到最尾巴 则 继续找下一个stamp
能把他分成左右
这时的左边有个offset了，比如****b** offset是3，只要stamp的长度不超过头且能match上，就可以

这个解法可以有nwin*M^2 其中m平方是在用stamp去match的时候最坏能从stamp最长match到1
可以给出最短match路径


'''
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ans = []
        offset = 0
        while target!='':
            x = target.find(stamp)
            if x==-1:
                return []
            ans.append(x+offset)
            
            can_stamp,indices = self.moveLeft(stamp,target[:x],offset)
            if not can_stamp:
                return []
            ans.extend(indices)
            
            offset,target,indices = self.moveRight(stamp,target[x+len(stamp):],
                                                offset+x+len(stamp))
            ans.extend(indices)
            
        return ans[::-1]
        
        
    
    def moveLeft(self,stamp,s,offset):
        ans = []
        while s:
            for ind in range(1,len(stamp)):
                additional = 0
                if ind>len(s):
                    if offset == 0:
                        continue
                        
                    additional = ind - len(s)
                    
                if stamp[additional:ind]==s[-ind:]:
                    ans.append(offset+len(s)-ind)
                    s=s[:-ind]
                    break
            else:
                return False,[]
        return True,ans
        
    
    def moveRight(self,stamp,s,offset):
        ans = []
        while s:
            for ind in range(1,len(stamp)):
                if stamp[-ind:]==s[:ind]:
                    ans.append(offset+ind-len(stamp))
                    offset+=ind
                    s=s[ind:]
                    break
            else:
                return offset,s,ans
        return offset,s,ans

