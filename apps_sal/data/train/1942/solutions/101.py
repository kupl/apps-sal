class Solution:
    def peopleIndexes(self,favoriteCompanies):
        responses = dict()
        ret = []
        for i in range(len(favoriteCompanies)):
            responses[i] = set(favoriteCompanies[i])
        
        for i, resp in list(responses.items()):
          not_sub = True
          for v in list(responses.values()):
            if resp == v:
              continue
            if resp - v == set():
              not_sub = False
          if not_sub:
            ret.append(i)
        
        return list(sorted(ret))
            
                    

