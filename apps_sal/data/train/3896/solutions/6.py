def solution(number):
  return sum(i for i in range(number) if i%5==0 or i%3==0)
