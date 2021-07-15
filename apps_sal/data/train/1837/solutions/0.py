class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        answer = []
        
        if orders is None or len(orders) == 0 or len(orders[0]) == 0:
            return answer
        
        items = set()
        
        for order in orders:
            items.add(order[2])
            
        items = sorted(list(items))
        answer.append([\"Table\"])
        
        for item in items:
            answer[0].append(item)
            
        hashMap = collections.defaultdict(list)
        itemIndex = self.convertItemToIndex(answer[0])
        m = len(answer[0])
        
        for order in orders:
            hashMap[int(order[1])].append(order[2])
            
        hashMap = {key : hashMap[key] for key in sorted(hashMap.keys())}
        currentIndex = 1
        
        for key in hashMap.keys():
            answer.append([\"0\"] * m)
            answer[currentIndex][0] = str(key)
            countMap = defaultdict(lambda: 0)
            
            for currentItem in hashMap[key]:
                countMap[currentItem] += 1
            
            for currentItem in countMap.keys():
                answer[currentIndex][itemIndex[currentItem]] = str(countMap[currentItem])
            
            currentIndex += 1
            
        return answer
    
    def convertItemToIndex(self, tempAns):
        itemToIndex = {}
        
        for i, curr in enumerate(tempAns):
            itemToIndex[curr] = i
            
        return itemToIndex
            
                    
