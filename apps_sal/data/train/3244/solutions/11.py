b = {40:3.85,20:1.93,5:0.49,1:0.1,10:0.97}
def cheapest_quote(n):
    a = [0.0]
    while n != 0:
        if n - 40 >= 0:
            n-= 40
            a.append(b[40])
            continue
        if n - 20 >= 0:
            n-= 20
            a.append(b[20])
            continue
        if n - 10 >= 0:
            n-= 10
            a.append(b[10])
            continue
        if n - 5 >= 0:
            n-= 5
            a.append(b[5])
            continue
        if n - 1 >= 0:
            n-= 1
            a.append(b[1])
            continue
        if n < 0:
            break
    return round(sum(a),2)
