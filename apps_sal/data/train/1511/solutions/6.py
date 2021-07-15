t=int(input()) #TESTCASES

for y in range(t):
 inptstr=input().split()

 n=int(inptstr[0]) #N TOTAL ELEMENTS

 K=int(inptstr[1]) #K CONSTaNT IN Pij

 s=input() #STRING SEQUENCE OF CELLS ELEMENTS

 
 noblock=s.split('X')
 cnt=[]
 cntiron=0
 for ele in noblock: #PARSING ELEMENTS WITHOUT BLOCK
  d={}
  d1={}
  iron=[]
  magnet=[]
  for x in range(len(ele)):#TRACKING LOCATION OF ELEMENTS IN NOBLOCK
   if ele[x]=='I':
    iron.append(x)
   elif ele[x]=='M':
    magnet.append(x)
  #print('part',ele)
  for i in iron:

   #print('IRON - ',i)
   for j in magnet:
    #print('MAGNET - ',j)
    
    if i in d or j in d1:
     continue
    if i<j:
     Sij=(ele[i:j]).count(':')

    if j<i:
     Sij=(ele[j:i]).count(':')
    Pij=(K+1)-(abs(j-i))-Sij
    if Pij > 0:
     cntiron=cntiron+1
     #print('CONNECTION DONE')
     d[i]=j
     d1[j]=i
     break
 
 print(cntiron)

    
    
    
  
  




 
 


