from re import findall

def solution(tiles):
  
  res = ''
  
  for tile in range(1, 10):
      hand = ''.join(sorted(tiles + str(tile)))
      if any(hand.count(c) > 4 for c in set(hand)): continue
      
      for pair in findall(r'((\d)\2)', hand):
          
          rest = hand.replace(pair[0], '', 1)
          
          while rest: 
              char = rest[0]
              triplet = char * 3
              if triplet in rest: 
                  rest = rest.replace(triplet, '')
              else:
                  i = int(char)
                  second, third = str(i + 1), str(i + 2)
              
                  if char in rest and second in rest and third in rest:
                      rest = rest.replace(char, '', 1).replace(second, '', 1).replace(third, '', 1)
                  else: 
                      break
          
          if not rest: 
              res += str(tile)
              break
  
  return res
