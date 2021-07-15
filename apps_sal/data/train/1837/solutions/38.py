class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = {}
        top_row = set()
        
        for order in orders:            
            _name, num, item = order
            top_row.add(item)
            if tables.get(num):
                tables[num].append(item)
            else: 
                tables[num] = [item]
                
        top_row = list(top_row)
        top_row.sort()
        top_row = [\"Table\", *top_row]
        all_items = [(top_row[idx], idx) for idx in range(len(top_row))]

        food_indexes = dict(all_items)
        
        output = []

        for table, orders in tables.items():
            row = [0 for i in range(1, len(top_row))]
            row = [table, *row]
            for food in tables[table]:
                row[food_indexes[food]] += 1;
            row = [str(num) for num in row]
            output.append(row)
        
        output.sort(key=lambda row: int(row[0]))
        output.insert(0, top_row)
        return output
        
        
        

# var displayTable = function(orders) {
#     let tables = {};
#     let allItems = new Set();
#     //get tables first, and an array of items. if table exists, push. if not, create then oush
#     for(let o of orders){
#         let [_name, num, item] = o;
#         tables[num]
#         ? tables[num].push(item)
#         : tables[num] = [item];
#         allItems.add(item);
#     }
#     let sortedItems = [\"Table\", ...[...allItems].sort()];
#     let foodIndexes = {};
#     for(let i = 1; i < sortedItems.length; i++){
#         let key = sortedItems[i];
#         foodIndexes[key] = i;
#     }

#     //then add orders to the table
#     let output = [sortedItems];
#     for(let t of Object.keys(tables)){
#         //an array from sortedItems.length, filled with zeroes
#         let row = new Array(sortedItems.length).fill(0);
#         row[0] = t;
#         // increment the food based on the index of foodIndexes
#         tables[t].forEach(f => {
#             let index = foodIndexes[f];
#             row[index] ++;
#         })
#         row = row.map(x => `${x}`);
#         output.push(row);
#     }
#     return output;
# };
