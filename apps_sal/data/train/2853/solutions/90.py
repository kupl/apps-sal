def solve(arr):
    answer=[]
    while len(arr)>0:
        poppedElement= arr.pop()
        if poppedElement not in answer:
            answer.append(poppedElement) 
    answer.reverse()
    return answer
print((solve([3,4,4,3,6,3]))) 

