def well(x):
    cnt=x.count('good')
    return "Fail!" if cnt==0 else "Publish!" if cnt < 3 else "I smell a series!"
