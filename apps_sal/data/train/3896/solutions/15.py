def solution(number):
  return sum(range(0, number, 3)) + sum(range(0, number, 5)) - sum(range(0, number, 15))
