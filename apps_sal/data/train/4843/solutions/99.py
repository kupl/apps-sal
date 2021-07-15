from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((sum(i) for i in combinations(ls,k) if sum(i)<= t), default=None)
    
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     arr=[]
#     for index, num in enumerate(ls):
#         while index+k-1 <= len(ls)-1:
#             totalSum = 0
#             totalSum = sum(ls[index+1:index+k-1],num)
#             if totalSum < t:
#                 arr.append(totalSum)
#             index +=1
#             print(index,num,totalSum,)
    
#     arr.sort()
#     print(arr)
#     if arr !=[]:
#         return arr[-1]
            
            
            

