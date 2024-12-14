def part1(filepath):
    f = open(filepath,"r")
    calibrations = []
    for line in f:
        calibrations.append([int(line.split()[0].replace(":","")),int(line.split()[1]),int(line.split()[2])])

def generatePermutations(arr):
    
part1("C:/Users/mason/Desktop/aoc_2024/dec_7/input.txt")