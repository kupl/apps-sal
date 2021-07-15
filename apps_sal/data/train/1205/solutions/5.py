# cook your dish here
# cook your dish here

def calc(array) :
 result = 0
 for i in range (1,len(array)):
  if array[i] == array[i-1]:
   result+=1
 return result
def answer(p,q):
 result = p*(p-1)+(p*(p-3)*q)//2
 return result
for test_case in range (int(input())):
 String = input()
 sequence = []
 for i in range (len(String)) :
  sequence.append(String[i])
 q = calc(sequence)
 print(answer(len(String),q))

