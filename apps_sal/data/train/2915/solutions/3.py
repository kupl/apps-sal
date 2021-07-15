check_availability=lambda sh,ct:next((j for i,j in sh if ct>i and ct<j),1)
