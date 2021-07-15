cards = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']

def royal_flush(arr):
 nonlocal ans, confirm
 rf_set = 'TJQKA'
 rf = 1
 for char in arr:
  if char[0] not in rf_set:
   rf = 0
   break
 if rf :
  if len(set(suit)) == 1:
   ans = 'royal flush'
   confirm = 1
def straight_flush(arr):  # and 'straight'
 nonlocal ans,confirm
 sf = 1
 for i in range(1,5):
  if arr[i] - arr[i-1] != 1:
   sf = 0
   break
 if sf:
  if len(set(suit)) == 1 :
   ans = 'straight flush'
   confirm = 1
  else:
   ans = 'straight'
   confirm = 1
def four(arr):
 nonlocal ans, confirm
 f = 0
 for char in arr:
  if arr.count(char) == 4:
   f = 1
   break
 if f:
  confirm = 1
  ans = 'four of a kind'
def full_house(arr): # and three
 nonlocal ans, confirm
 fh = 0
 three = 0
 two = 0
 for char in arr:
  if arr.count(char) == 3:
   three = 1
  elif arr.count(char) == 2:
   two = 1
 if three and two:
  confirm = 1
  ans = 'full house'
 elif three:
  confirm = 1
  ans = 'three of a kind'
def two_pairs(arr):
 nonlocal ans, confirm
 temp = []
 for char in arr:
  if arr.count(char) == 2:
   if char not in temp:
    temp.append(char)
 if len(temp) == 2:
  confirm = 1
  ans = 'two pairs'
 elif len(temp) == 1:
  confirm = 1
  ans = 'pair'

def idex(char_x):
 return cards.index(char_x)
for _ in range(int(input())):
 onhand = list(input().split())
 cards_set = [[],[]]
 suit = []
 confirm = 0
 ans = ''
 for c in onhand:
  num = idex(c[0])
  cards_set[0].append(num)
  if num == 0:
   cards_set[1].append(13)
  else:
   cards_set[1].append(num)
  suit.append(c[1])
 royal_flush(onhand)
 if not confirm:
  cards_set[0] = sorted(cards_set[0])
  cards_set[1] = sorted(cards_set[1])
  straight_flush(cards_set[0])
  straight_flush(cards_set[1])
 if not confirm:
  four(cards_set[0])
  four(cards_set[1])
 if not confirm:
  full_house(cards_set[0])
  full_house(cards_set[1])
 if not confirm:
  if len(set(suit)) == 1:
   confirm = 1
   ans = 'flush'
 if not confirm:
  two_pairs(cards_set[0])
  two_pairs(cards_set[1])
 print(ans if confirm else 'high card')
