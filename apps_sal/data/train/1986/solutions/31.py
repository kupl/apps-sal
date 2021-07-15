class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        answer = [start]
        visited = set(answer)
        
        next = start
        while (next != None): 
            previous = next
            next = None
            for i in range(n):
                newNum = previous ^ (1 << i)
                # print(i, newNum, previous)
                if newNum not in visited:
                    visited.add(newNum)
                    answer.append(newNum)
                    next = newNum
                    break
            
        return answer
