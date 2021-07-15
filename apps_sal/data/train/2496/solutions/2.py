from datetime import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        # index mapping: 0          1           2           3           4           5       6        
        weekday_name= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        
        # datetime is a class, whose constructor can output corresponding date-time object
        #
        # for example:
        # datetime(2020, 1, 15) = '2020-01-15 00:00:00'

        # And its strftime('%w') can convert a date-time object into a index string of weekday, start from Sunday as 0
        #
        # for example:
        # datetime(2020, 1, 15).strftime('%w') = '3'

        # Finally, use int( ... ) to carry out explicit type conversion fron str to integer as weekday index
        return weekday_name[ int( datetime(year, month, day).strftime('%w') ) ]
