def solution(number):
  import itertools
  return sum(set(itertools.chain(range(0, number, 3), range(0, number, 5))))
