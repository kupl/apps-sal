def difference_of_squares(n):
    
# =============================================================================
#     This function returns the difference between the sum of the squares of the 
#     first n natural numbers (1 <= n <= 100) and the square of their sum.
#     
#     Example:
#         When n = 10:
#         The square of the sum of the numbers is:
#         (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)2 = 552 = 3025
#         The sum of the squares of the numbers is:
#         12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385
#         
#         The difference between square of the sum of the first ten natural numbers
#         and the sum of the squares of those numbes is: 3025 - 385 = 2640
# =============================================================================
    
    sum_1 = 0
    
    sum_2 = 0
    
    for num in range (1,(n+1)):
       sum_1 += num      
       sum_2 += num**2
       
    return ((sum_1**2) - sum_2)
