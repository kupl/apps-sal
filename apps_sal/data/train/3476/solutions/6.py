li = [i for i in range(0,1000000,13)if'4'not in str(i)and'7'not in str(i)]
unlucky_number=lambda n:next(len(li[:li.index(i)])+1for i in range(n,-1,-1)if'4'not in str(i)and'7'not in str(i)and not i%13)
