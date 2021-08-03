def braces_status(s):
    order = ["X"]
    for i in s:
        if i in "({[":
            order.append(")}]"["({[".index(i)])
        elif i in ")}]":
            if order.pop() != i:
                return 0
    return len(order) == 1
