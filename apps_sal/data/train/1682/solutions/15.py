# cook your dish here
number = input()
number = list(number)
number = list(map(int,number))
d1={}
for i in range(len(number)-1):
    k = number[i]
    for j in range(i,len(number)-1):
        if number[j+1]>number[j]:
            k=k+number[j+1]
        else:
            d1[i] = k
            break            
d1[len(number)-1] = number[len(number)-1] 
# print(d1)
Keymax = max(d1, key=d1.get)
all_values = d1.values()
max_value = max(all_values)
sum1=number[i]
for i in range(Keymax,len(number)-1):
    if number[i+1]>number[i]:
        pass
    else:
        print(str(max_value)+":"+str(Keymax+1)+"-"+str(i+1))
        break
    
        
