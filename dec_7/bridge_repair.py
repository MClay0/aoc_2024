<<<<<<< HEAD
def part1(filepath):
    f = open(filepath,"r")
    calibrations = []
    for line in f:
        calibrations.append([int(line.split()[0].replace(":","")),int(line.split()[1]),int(line.split()[2])])

def generatePermutations(arr):
    
part1("C:/Users/mason/Desktop/aoc_2024/dec_7/input.txt")
=======

def createRepairDict(path):
    file = open(path,"r")
    repairDict = {}
    for line in file:
        target = int(line.split(":")[0])
        componentArr = []
        for num in line.split(":")[1].split():
            componentArr.append(int(num))
        repairDict[target] = componentArr
    return repairDict

def createPermutations(components: list):         
    permutations = []
    for num in components:
        newPermutations = []
        for permutation in permutations:
            newPermutations.append(permutation + num)
            newPermutations.append(permutation * num)
        permutations.append(num)
        permutations.extend(newPermutations)
    finalPermutations = pow(2,len(components))
    permutations = permutations[len(permutations)-finalPermutations:]
    return permutations

def isValidRepair(target, permutations):
    if target in permutations:
        return True
    return False

def checksum(repairDict):
    sum = 0
    for repair in repairDict:
        if isValidRepair(repair,createPermutations(repairDict[repair])):
            sum += repair
    return sum

def part1(path):
    repairs = createRepairDict(path)
    return checksum(repairs)

print(part1("./dec_7/input.txt"))   #Answer is between 1399219270675 and 1509440453766
>>>>>>> bea18fb (sync)
