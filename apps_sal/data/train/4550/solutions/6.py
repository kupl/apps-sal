import datetime,re
seconds_ago = lambda Q,S : str(datetime.datetime(*map(int,re.split('[- :]',Q))) - datetime.timedelta(0,S))

import datetime as dt
