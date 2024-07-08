matrixSize = int(input("Number of persons?\n"))

givenInput = []
seenArray = []
suspectArray = []

ACCEPTED_CHARS = ["0","1","2"]
SUSPECT_THRESHOLD = 2

def initSeenList():
    for i in range(matrixSize):
        seenArray.append(0)

def initInputList():
    for i in range(matrixSize):
        givenInput.append(seenArray.copy())

def initInputLines():
    for i in range(matrixSize):
        line = input(f"give list for line{i}\n")

        num = len(line)
        index = 0
        for j in range(num):
            extractedChar = line[j]
            if(extractedChar in ACCEPTED_CHARS):
                extractedNum = int(line[j])
                givenInput[i][index] = extractedNum
                index += 1
        checkForObservers(i)

def analyzer(): 
    initSeenList()
    initInputList()

    initInputLines()

    for i in range(matrixSize):
        lineAnalyzer(i, matrixSize)
    
    suspectFinder()

    #print(seenArray)
    print(suspectArray)


def lineAnalyzer(line, size):
    for i in range (size):
        num = givenInput[line][i]
        if(num == 1):
            seenArray[i] += 1

def checkForObservers(line):
    num = 0
    for i in range(matrixSize):
        if(givenInput[line][i] == 2):
            num += 1
    if(num != 1):
        raise Exception("Observer Exception, observer number should be 1 per line")

def suspectFinder():
    for i in range(matrixSize):
        if(seenArray[i] < SUSPECT_THRESHOLD):
            suspectArray.append(i)

analyzer()