#This response system allows neighbors to "vote" for their class attribute, and use the
# majority as a prediction.
#This function assumes that the class that is voted on is the last attribute of each
# queried neighbor.
#Still totally based off machinelearningmastery.com

import operator

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse = True)
	return sortedVotes[0][0]

neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = getResponse(neighbors)
print(response)
