while int(input()) != 0:
 permutation = list(map(int,input().split()))
 inverse_permutation = [0 for i in range(len(permutation))]
 for index in range(len(permutation)):
  inverse_permutation[permutation[index]-1] = index+1
 print('ambiguous') if inverse_permutation == permutation else print('not         ambiguous')
 
