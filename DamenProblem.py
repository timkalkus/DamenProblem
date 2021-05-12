import itertools
import datetime

def isValidSolution(inputList):
	# inputList contains rows as list. Location of the queen is encoded in the bit location
	diag_0 = 0b0
	diag_1 = 0b0
	size = len(inputList)
	for i in range(size):
		diag_0 = diag_0 ^ (inputList[i] << i)
		diag_1 = (diag_1 << 1) ^ inputList[i]
	return bin(diag_0).count("1") == size and bin(diag_1).count("1") == size

def findSolution(size = 8):
	# test all plausible solutions with 1 queen in each row and column
	rows = [0b1 << i for i in range(size)]
	allPossibleSolutions = itertools.permutations(rows)
	validSolutions = []
	for possibleSolution in allPossibleSolutions:
		if isValidSolution(possibleSolution):
			validSolutions.append(possibleSolution)
	return validSolutions

def printChessBoard(inputList):
	for element in inputList:
		print(format(element, '#0' + str(len(inputList)+2) + 'b')[2:])



if __name__ == "__main__":
	for i in range(1,11):
		startTime = datetime.datetime.now()
		solutions = findSolution(i)
		executionTime = (datetime.datetime.now() - startTime).total_seconds() * 1000
		print('{0:} solution(s) on a {1:}x{1:} field. Found in {2:.2f}ms'.format(len(solutions),i,executionTime))
