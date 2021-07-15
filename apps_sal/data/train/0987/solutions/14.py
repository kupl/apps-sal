for _ in range(int(input())):
 finsh,distancetoBolt,tigerAccelaration,boltSpeed =list(map(int,input().split()))
 #s=(a*t*t)*1/2
 t1=(((distancetoBolt+finsh)*2)/(tigerAccelaration))**(1/2)
 t2=finsh/boltSpeed
 if(t1>t2):
  print('Bolt')
 if(t2>t1):
  print('Tiger')
 if(t1==t2):
  print('Tiger')


