def fun(numbers):
    # numbers.sort(reverse=True)
    le = len(numbers)
    stack =[]
    ans=0
    i=1
    for i in numbers:
        while stack:
            ans  = max(ans,stack[-1]^i)
            if stack[-1] > i:
                break
            else:
                stack.pop()
        stack.append(i)
    
    return ans


# var1, var2,var3 = [int(x) for x in input().split()]
n = input()
user_input = input().split(' ')
numbers = [int(x.strip()) for x in user_input] 
# st = input()
# print(fun(st))

print(fun(numbers))





# # st = input()
# var1, var2 = [int(x) for x in input().split()]

# # # fun(st,var1,var2)

# # # var2 = input()
# print(fun(var1,var2))

# ############################################################3###############################

# # user_input = input().split(' ')
# # numbers = [int(x.strip()) for x in user_input] 
# # print(fun(numbers))
# ######################################################################################

