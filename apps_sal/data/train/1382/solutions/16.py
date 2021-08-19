n = int(input())
list_int = [int(i) for i in input().split()]
x = int(input())


def Negative(List):
    return [num for num in List if num < 0]


l = Negative(list_int)
l.sort()
list_sum = sum(l)

if(x == 0):
    print(0)
elif(x == 1):
    print(-l[0])
elif(x < len(l)):
    # cost=0
    #cost1 = -l[x]*x
    #cost2 = -(sum(l[:(x)])-l[x]*x)
    #cost  = cost1+cost2
    cost = -(sum(l[:(x)]))
    print(cost)
else:
    cost = -(list_sum)
    print(cost)
