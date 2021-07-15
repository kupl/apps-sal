from math import ceil;numberOfSteps=lambda s,m:next((i for i in range(ceil(s/2),s+1)if not i%m),-1)
