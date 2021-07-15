def queue_time(customers, n):
    time = 0
    while len(customers[:])>0:
      time=time+1
      customers[:n]=[x-1 for x in customers[:n]]
      customers=[y for y in customers if y !=0]
    return time
