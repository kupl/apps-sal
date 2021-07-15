#Lists
tempRecipeLossList = []
answerList = []
priceList = []
quantityList = []
discountList = []
total_lossList = []

#Functions
def split_loss_calculator(userInput):
 (price, quantity, discount) = list(map(int, userInput.split()))
 loss = price - (price * ((100+discount)/100) * ((100-discount)/100))
 tempRecipeLossList.append(loss * quantity)
 

#Program
test_cases = int(input())
for i in range(test_cases):
 numRecipeTypes = int(input())
 for j in range(numRecipeTypes):
  split_loss_calculator(input())
 answerList.append(sum(tempRecipeLossList))
 tempRecipeLossList.clear()
 
for item in range(len(answerList)):
 print("{}".format(answerList[item]))

