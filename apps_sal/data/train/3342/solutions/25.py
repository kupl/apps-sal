# if n = 3
#output 1
#       22
#       33
# if element in n is greater tha 1 then
#we loop through n and add 1 to n
# return the result in a new line
def pattern(n):
    return '\n'.join(str(x)*x for x in range(1, n + 1))
