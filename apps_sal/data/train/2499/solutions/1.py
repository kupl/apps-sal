class Solution:
    def gcd(a,b):
      if(b%a==0):
          return a 
      else:  
        if(a%b==0):
            return b
        else:
          if b>a:
             return gcd(a,b-a)  
          else:
              return gcd(a-b,b)  
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if(len(deck)==0 or len(deck)==1):
            return False
        d=list(set(deck))
        if(len(d)==1 and len(deck)>=2):
            return True
        s=gcd(deck.count(d[0]),deck.count(d[1]))
        if(s<2):
            return False
        for i in range(2,len(d)):
            if(gcd(s,deck.count(d[i]))<2):
                return False
            s=gcd(s,deck.count(d[i]))
            
        return True    
