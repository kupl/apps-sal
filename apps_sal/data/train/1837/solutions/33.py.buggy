class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
      table_dicts = {}
      dicts = {}
      for order in orders:
        if (int)(order[1]) not in table_dicts: table_dicts[(int)(order[1])] = 1
        if order[2] not in dicts:
          dicts[order[2]] = {order[1]:1}
        else:
          if order[1] in dicts[order[2]]:
            dicts[order[2]][order[1]] += 1
          else:
            dicts[order[2]][order[1]] = 1
      tables = []
      for key,value in table_dicts.items(): tables.append(key)
      tables.sort()
      tables = [str(x) for x in tables]
      dishes = []
      for key,value in dicts.items(): dishes.append(key)
      dishes.sort()
      res = []
      res.append([\"Table\"] + dishes)
      for i in range(len(tables)):
        temp_res = [tables[i]]
        for dis in dishes:
          if tables[i] in dicts[dis]:
            temp_res.append((str)(dicts[dis][tables[i]]))
          else:
            temp_res.append('0')
        res.append(temp_res)
      return res
        
      
        
