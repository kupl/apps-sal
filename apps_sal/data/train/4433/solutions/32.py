def logical_calc(array, op):
    ans = array[0]
    for operator in array[1:]:

        if op == "AND":
            ans = ans and operator
        elif op == "OR":
            ans = ans or operator
        else:
            ans = ans ^ operator
    return ans

#     return #boolean
