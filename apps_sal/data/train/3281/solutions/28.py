import datetime
def unlucky_days(n):

   t=0
   initial_date = datetime.date(n,1,1)
   for e in range(1,365):   # прибавлять по дню и счетчик если
      my_date = initial_date + datetime.timedelta(days=e)
      if my_date.isoweekday() == 5 and my_date.day == 13:
         t+=1
   return t
