class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0
        totalCost = target[0]
        for index in range(1, len(target)):
            num = target[index]
            prev = target[index - 1]
            diff = num - prev
            totalCost += max(diff, 0)
        return totalCost
        lst = []
        lst.append(target)
        prev_layer = target
        new_layer = []
        while len(prev_layer) > 1:
            counter = 0
            while counter < len(prev_layer):
                fi = prev_layer[counter]
                se = fi
                if counter + 1 < len(prev_layer):
                    se = prev_layer[counter + 1]
                new_layer.append(min(fi, se))
                counter += 2
            lst.append(new_layer)
            prev_layer = new_layer
            new_layer = []
        lst.append([0])
        cost = 0
        print(lst)
        for index in range(len(lst) - 2, -1, -1):
            l = lst[index]
            print(('l', l))
            for in_index in range(len(l)):
                val = l[in_index]
                parent_index = int(in_index / 2)
                cost += val - lst[index + 1][parent_index]
                print(('val', val))
                print(('parent_val', lst[index + 1][parent_index]))
                print(('cost', cost))
                print('--------')
        return cost
