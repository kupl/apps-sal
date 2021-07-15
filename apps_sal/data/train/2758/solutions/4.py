def decode(s):
    arr = str(s).strip('98').split('98')
    return ', '.join(sum([[''.join([chr(96+int(arr[i][k:k+3])-100) for k in range(0,len(arr[i]),3)]),str(int(arr[i+1],2))] for i in range(0,len(arr),2)],[]))
