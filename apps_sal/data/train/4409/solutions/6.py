def noonerize(n):
    try:
        return abs(int(str(n[1])[0]+ str(n[0])[1:]) - int(str(n[0])[0]+ str(n[1])[1:])) if n[0] != n[1] else 0
    except:
        return "invalid array"
