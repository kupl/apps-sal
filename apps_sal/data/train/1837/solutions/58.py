class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        display=[]
        tableList=set()
        foodList=set()
        
        for order in orders:
            foodList.add(order[2])
            tableList.add(int(order[1]))
            
        display.append([\"Table\"]+sorted(list(foodList)))
        tableList=sorted(list(tableList))
        for table in tableList:
            display.append([table]+[0]*len(foodList))
        tableToIndex={}
        for i in range(1,len(display)):
            tableToIndex[display[i][0]]=i
            
        foodToIndex={}
        for i in range(1,len(display[0])):
            foodToIndex[display[0][i]]=i
            
        for order in orders:
            display[tableToIndex[int(order[1])]][foodToIndex[order[2]]]=display[tableToIndex[int(order[1])]][foodToIndex[order[2]]]+1
            
        display=[[str(ele) for ele in table] for table in display]
                
        return display
        
            
        
