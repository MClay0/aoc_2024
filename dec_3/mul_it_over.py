import re


def createLineArr(path):
    arr = []
    with open(path,"r") as f:
        for line in f:
            arr.append(line)
    return arr

def findMuls(lineArr):
    mulArr = []
    for line in lineArr:
        mulMatches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
        mulArr.append(mulMatches)
    return mulArr

def findLineDoToggleRange(line):
    doIndexes = [0]
    dontIndexes = []
    for i in range(len(line)):
        if line[i:i+4] == "do()":
            doIndexes.append(i)
        elif line[i:i+7] == "don't()":
            dontIndexes.append(i)
    rangePairs = [[0,dontIndexes[0]]]  
    maxStart = doIndexes.pop(0)
    maxStop = dontIndexes.pop(0)
    while len(dontIndexes) > 0 or len(doIndexes) > 0:
        if doIndexes[0] < maxStop:
            doIndexes.pop(0)
        else:
            maxStart = doIndexes.pop(0)
            while True:
                if dontIndexes[0] < maxStart:
                    dontIndexes.pop()
                else:
                    maxStop = dontIndexes.pop()
                    rangePairs.append([maxStart,maxStop])
                    break
            


def findMulsWithToggle(lineArr,doToggle):
    mulArr = []
    toggle = 1              #1 if do, 0 if don't
    for line in lineArr:
        
def createAndSumPairs(mulArr):
    sum = 0
    for line in mulArr:
        for entry in line:
            num1 = int(entry[4:entry.index(",")])
            num2 = int(entry[entry.index(",")+1:entry.index(")")])
            sum += num1 * num2
    return sum

def part1(path):
    lines = createLineArr(path)
    muls = findMuls(lines)
    sum = createAndSumPairs(muls)
    return sum

def part2(path):
    lines = createLineArr(path)
    muls = findMulsWithToggle(lines)
    toggleRange = findDoToggleRange(lines)
    sum = createAndSumPairs(muls,toggleRange)
    return sum
path = "/home/mason/Desktop/aoc_2024/dec_3/input.txt"
print(part1(path))
print(part2(path))

    
        