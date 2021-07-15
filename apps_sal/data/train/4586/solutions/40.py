import numpy

def tv_remote(word):
    initial = (0,0)
    current = ()
    final = ()
    total = 0
    count = 0
    screen = numpy.array([['a','b','c','d','e','1','2','3'],
                          ['f','g','h','i','j','4','5','6'],
                          ['k','l','m','n','o','7','8','9'],
                          ['p','q','r','s','t','.','@','0'],
                          ['u','v','w','x','y','z','_','/']])

    for i in word:
      current = numpy.argwhere(screen == word[count])
      final = abs(current - initial)
      total += final[0][0]+final[0][1]
      count += 1
      initial = current
      
    return total+len(word)
