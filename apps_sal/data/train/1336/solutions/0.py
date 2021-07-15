line = input()
test = 0

while line != "0":
    test += 1
    d = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    a = list(map(int,line.split()))
    for i in range(min(a),max(a)+1):
        for c in str(i):
            d[c] += 1
    pairs = list(d.items())
    pairs.sort()        
    print("Case %s: %s" % (test, " ".join(["%s:%s" % (k,v) for k,v in pairs])))
    line = input()
