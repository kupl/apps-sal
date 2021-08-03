open_tweets = []
string = input()
a, b = string.split(" ")
n = int(a)
k = int(b)
counter = 0
for x in range(k):
    command = input()
    if command == "CLOSEALL":
        counter = 0
        open_tweets = []
        print(counter)
        continue
    click, tweetnum = command.split(" ")
    if tweetnum in open_tweets:
        open_tweets.remove(tweetnum)
        counter -= 1
        print(counter)
    else:
        open_tweets.append(tweetnum)
        counter += 1
        print(counter)
