class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        #         n5 = 0
        #         n10 = 0
        #         while True:
        #             ind10 = bills.index(10) if 10 in bills else 10000
        #             ind20 = bills.index(20) if 20 in bills else 10000

        #             ind = min(ind10, ind20)
        #             if ind ==10000:
        #                 return True

        #             bill_type =bills[ind]
        #             n5 += bills[:ind].count(5)

        #             if bill_type==10:
        #                 if n5==0:
        #                     return False
        #                 n10+=1
        #                 n5 -=1
        #             elif bill_type ==20:
        #                 if n5<3 and n5>0 and n10>0:
        #                     n10 -= 1; n5 -=1
        #                 elif n5 >=3:
        #                     n5 -= 3
        #                 else:
        #                     return False

        #             bills = bills[ind+1:]
        #             # print(bills)

        #         else:
        #             return True

        n5 = 0
        n10 = 0
        for i in bills:
            if i == 5:
                n5 += 1
            elif i == 10:
                if n5 <= 0:
                    return False
                else:
                    n5 -= 1
                    n10 += 1
            else:
                if n10 > 0 and n5 > 0:
                    n10 -= 1
                    n5 -= 1
                elif n5 >= 3:
                    n5 -= 3
                else:
                    return False
        else:
            return True


#         def deter(part_bill):
#             n5 = part_bill.count(5)
#             n10 = part_bill.count(10)
#             n20 = part_bill.count(20)

#             if (n5 >= n10) and ( (15*n20 <= (5*(n5-n10) + 10*n10)) and (n5-n10)>=n20 ):
#                 result = True
#             else:
#                 result = False

#             rest5 = n5-n10
#             rest10 =

#             return result, n5-n10, n


#         for i in bills:

#             if i == 5:
#                 changes.append(5)

#             elif i == 10:
#                 if 5 in changes:
#                     changes.remove(5)
#                     changes.append(10)
#                 else:
#                     return False

#             else:
#                 if 5 in changes and 10 in changes:
#                     changes.remove(5)
#                     changes.remove(10)
#                 elif changes.count(5) >=3:
#                     changes.remove(5)
#                     changes.remove(5)
#                     changes.remove(5)
#                 else:
#                     return False

#         return True
