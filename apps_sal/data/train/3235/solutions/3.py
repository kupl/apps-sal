def decompose_single_strand(ar):
    i = []
    t= []
    th= []
    for x,y,z in zip(ar[0::3], ar[1::3], ar[2::3]):
      i.append(x+y+z)
    #print( "Frame 1: " +" ".join(i))
    for x,y,z in zip(ar[1::3], ar[2::3], ar[3::3]):
      t.append(x+y+z)
    #print( "Frame 2: " +" ".join(t))
    for x,y,z in zip(ar[2::3], ar[3::3], ar[4::3]):
      th.append(x+y+z)
    #print( "Frame 3: " +" ".join(th))
    if len(ar)==3:
      return  ("Frame 1: " +" ".join(i) + "\n" +  "Frame 2: " + str(ar[0])+" "+str(ar[-2:])+ "\nFrame 3: "+ str(ar[0:2]) + " " + str(ar[-1]))
    else:
      return ("Frame 1: " +" ".join(i) + "\n" +  "Frame 2: " + str(ar[0])+" "+" ".join(t)+" "+str(ar[-2:])+ "\nFrame 3: "+ str(ar[0:2]) +" " +" ".join(th)+ " " + str(ar[-1]))
    
      

