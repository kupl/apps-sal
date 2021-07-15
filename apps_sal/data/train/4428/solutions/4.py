def sort_by_bit(a):
    for i in range(len(a)):
      for j in range(i+1, len(a)):
        if bin(a[i]).count('1') > bin(a[j]).count('1'):
          a[i], a[j] = a[j], a[i]
        elif bin(a[i]).count('1') == bin(a[j]).count('1'):
          if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
    return a
