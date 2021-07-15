def omit_hashtag(message, hashtag):
    index = message.find(hashtag)
    if index == -1:
        return message
    else:
        return message[:index] + message[index+len(hashtag):]
    


