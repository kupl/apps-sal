class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
      if n < 2:
        return []
      else:
        res = []
        dicts = {}
        grid = [1]*n
        grid[0] = 0
        for i in range(1, n):
          target = i + 1
          if grid[target-1] == 1:
            dicts[target] = {target:1}
            start = target*2
            while start <= n:
              grid[start-1] = 0
              dicts[target][start] = 1
              start += target
        for i in range(2, n+1):
          res.append('1/' + str(i))
          for j in range(2, i):
            found = True
            de = j
            candidates = []
            for key,value in list(dicts.items()):
              if de in value: candidates.append(key)
            for can in candidates:
              if i in dicts[can]: 
                found = False
                break
            if found: res.append(str(j) + '/' + str(i))
        return res
            
            
            
          

