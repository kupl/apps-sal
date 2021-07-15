import math
for _ in range(int(input())):
 a = list(map(int, input().split()))
 steps = a[0]
 stairs_speed = a[1]
 elevators_speed = a[2]
 stairs_distance = math.sqrt(2) * steps
 elevators_distance = steps + steps
 stairs_time = stairs_distance / stairs_speed
 elevators_time = elevators_distance / elevators_speed
 if stairs_time < elevators_time:
  print("Stairs")
 else:
  print("Elevator")
