def calcAngle(h,m):
   
  # validate the input
  if (h < 0 or m < 0 or h > 12 or m > 60):
   print('Wrong input')
   
  if (h == 12):
   h = 0
  if (m == 60):
   m = 0
   h += 1;
   if(h>12):
     h = h-12;
   
  # Calculate the angles moved by 
  # hour and minute hands with 
  # reference to 12:00
  hour_angle = 0.5 * (h * 60 + m)
  minute_angle = 6 * m
   
  # Find the difference between two angles
  angle = abs(hour_angle - minute_angle)
   
  # Return the smaller angle of two 
  # possible angles
  angle = min(360 - angle, angle)
   
  if angle.is_integer() : return int(angle)
  else: return angle
 
 
def __starting_point():
 T= int(input())
 for i in range(T):
  t = input()
  h = int(t.split(":")[0])%12
  m = int(t.split(":")[1])
  # print(h,m)
  print(calcAngle(h,m),"degree")
__starting_point()
