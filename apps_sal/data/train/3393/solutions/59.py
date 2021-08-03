def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        #         b = 0
        # 开根方次循环
        a = sum(let * let + (i / let) * (i / let) for let in range(1, int(i ** 0.5) + 1) if i % let == 0)

        # 如果本身能被开根方，则减去，因为循环求和时多算了一次
        if (i ** 0.5) % 1 == 0:
            a = a - (i ** 0.5) * (i ** 0.5)

        if (a ** 0.5) % 1 == 0:
            result.append([i, int(a)])
    return result
#     r=[]
#     for i in range(m,n+1):
#         for x in range(1,int(i**0.5)+1):
#             if i%x==0:
#                 a=sum([x*x+(i/x)*(i/x)])
#         if (i ** 0.5) % 1 == 0:
#             a = a - (i ** 0.5) * (i ** 0.5)

#         if (a ** 0.5) % 1 == 0:
#             r.append([i, int(a)])
#     return r
