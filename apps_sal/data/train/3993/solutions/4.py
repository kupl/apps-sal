def solve(a):
    lenList = len(a)

    evenEntries = [a[i]  for i in range(0, lenList, 1 )  if str(a[i]).isdigit() and  a[i]%2==0 ]
    oddEntries =  [a[i]  for i in range(0, lenList, 1 )  if str(a[i]).isdigit() and  a[i]%2==1 ]

    amtEvenEntries = len(evenEntries)
    amtOddEntries = len(oddEntries)

    return amtEvenEntries-amtOddEntries
#end function 

