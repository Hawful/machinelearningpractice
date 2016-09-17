#Now we are focusing on accuracy since we know the correct answer for every iris in our dataset.
# This function will determin classification accuracy, the ratio of total correct predictions
# out of predictions made.
# All based off of the knn python tutorial on machinelearningmastery.com

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] is predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'a']]
predictions = ['a','a','a']
accuracy = getAccuracy(testSet, predictions)
print accuracy
