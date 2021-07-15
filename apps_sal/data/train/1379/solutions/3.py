import sys
def main():
 s = sys.stdin.readline
 string = s().strip()
 save = {}
 for i in string:
  if i in save:
   save[i]+=1
  else:
   save[i]=1
 output = ''
 x = set()
 for i in string:
  if i not in x:
   output += i
   output += str(save[i])
   x.add(i)
 print(output)

def __starting_point():
 main()

__starting_point()
