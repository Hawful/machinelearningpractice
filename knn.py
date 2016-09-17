from euclideanDistance import euclideanDistance 
from getAccuracy import getAccuracy 
from getNeighbors import getNeighbors 
from getResponse import getResponse 
from loadDataset import loadDataset 

def main():
	#prepdata
	trainingSet=[]
	testSet=[]
	split=0.67
	loadDataset('iris.data', split, trainingSet, testSet)
	print 'Train set: ' + repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))
	#predict
	predictions=[]
	k=3
	for x in range(len(testSet)):
		neighbors=getNeighbors(trainingSet, testSet[x], k)
		result=getResponse(neighbors)
		predictions.append(result)
		print('>predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	accuracy=getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')

main()
