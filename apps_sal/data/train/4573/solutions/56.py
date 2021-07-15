def over_the_road(address, n):
 numHouse = n*2
 if address%2 == 0:
  p = int(((numHouse-address)/2)+1)
  return (int((p*2)-1))

 else:
  p = (address+1)/2
  return (int(numHouse - 2*(p-1)))
