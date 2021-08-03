class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = []
        output = [[]]
        temp = []

        for i in range(len(orders)):
            if orders[i][1] not in table:
                table.append(orders[i][1])

        for j in range(len(table)):
            temp.append(int(table[j]))

        temp = sorted(temp)

        temp2 = []
        for k in range(len(table)):
            temp2.append(str(temp[k]))
            output.append(temp2)
            temp2 = []

        for l in range(len(orders)):
            if orders[l][2] not in output[0]:
                output[0].append(orders[l][2])

        temp2 = sorted(output[0])
        output[0] = [\"Table\"]+temp2

        for r in range(1,len(output)):
            for n in range(len(output[0])-1):
                output[r].append(\"0\")

        for m in range(len(orders)):
            tab = int(orders[m][1])
            idxt = temp.index(tab)+1
            meal = orders[m][2]
            idxm = output[0].index(meal)

            stack = int(output[idxt][idxm])
            stack += 1
            output[idxt][idxm] = str(stack)
            
        return output
