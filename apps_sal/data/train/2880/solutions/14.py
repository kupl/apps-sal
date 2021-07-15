seven=lambda n,s=0:(n,s)if n<99else seven(n//10-2*(n%10),s+1)
