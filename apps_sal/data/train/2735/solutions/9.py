def jumping_number(number):
  j = lambda n: n<10 or abs(n%10-(n//10)%10)==1 and j(n//10)
  return 'Jumping!!' if j(number) else 'Not!!'
