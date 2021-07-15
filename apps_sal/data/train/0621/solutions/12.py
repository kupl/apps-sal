# STEM.py

def main():
 t = int(input())
 for _ in range(t):
  n = int(input())
  arr = input().split();      
  min_length = 30;
  index = -1;
  for i in range(n):
   x = arr[i];     
   # print x,len(x)    
   if len(x) < min_length:
    index = i;
    min_length = len(x);

  
  s = arr[index];
  # print s
  # max_len = len(s)+1;
  answers = []
  l = len(s);
  while l > 0:
   for i in range(len(s)):            
    if i+l > len(s):
     break;
    flag = True;
    sub = s[i:i+l];

    for j in arr:
     if j.find(sub) == -1:
      # print sub,j
      flag = False;
      break;
    if flag :
     # print 'Answer Found',sub
     answers.append(sub);
   l -=1;
   if len(answers) > 0 :
    break;

  
  answers.sort();     
  print((answers[0]));
main();

