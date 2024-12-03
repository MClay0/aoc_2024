    
def part1(filepath):
    f = open(filepath,"r")
    lines = []
    for line in f:
        lines.append(line)
    l1 = []
    l2 = []
    total = 0
    for i in range(len(lines)):
        l1.append(lines[i].split(",")[0])
        l2.append(lines[i].split(",")[1])
    l1 = sorted(l1)
    l2 = sorted(l2)
    
    for i in range(len(l1)):
        total += abs(int(l1[i])-int(l2[i]))
    return total
    
def part2(filepath):
    f = open(filepath,"r")
    lines = []
    for line in f:
        lines.append(line)
    l1 = []
    l2 = []
    simScore = 0
    for i in range(len(lines)):
        l1.append(int(lines[i].split(",")[0]))
        l2.append(int(lines[i].split(",")[1]))
    l1 = sorted(l1)
    l2 = sorted(l2)
    
    freq = {}
    for num in l2:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in l1:
        if num in freq:
            simScore += num * freq[num]
    return simScore
path = "C:/Users/mason/Desktop/aoc_2024/dec_1/input.txt"
print(part1(path))
print(part2(path))
