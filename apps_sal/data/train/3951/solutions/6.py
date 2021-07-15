def duplicate_count(text):
    text = text.lower()
    duplicates = []
    for i in text:
        if text.count(i) > 1 and i not in duplicates:
            duplicates.append(i)    
    return len(duplicates)
