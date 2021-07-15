data=[]
for nextum in range(1, 12):
    data.append(int(input()))
 
data.reverse()
 
for x in data:
    res = x**3 * 5
    res += abs(x)**(0.5)
 
    if(res <= 400):
        print("f({0}) =".format(x), "{:.2f}".format(res))
    else:
        print("f({0}) = MAGNA NIMIS!".format(x))
