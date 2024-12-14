def generateMemory(memKey):             #12345  [0,".",".",1,1,1,".",".",".",".",2,2,2,2,2]
    memoryBlock = []
    if len(memKey) % 2 == 0:
        memKey = memKey[0:-1]
    id = 0
    for i in range(len(memKey)):
        if i % 2 == 0:
            for j in range(int(memKey[i])):
                memoryBlock.append(int(id))
            id += 1
        else:
            for j in range(int(memKey[i])):
                memoryBlock.append(".")
    return memoryBlock
                
def compress(memoryBlock):
    left = memoryBlock.index(".")
    right = -1
    for i in range(len(memoryBlock)):
        if memoryBlock[-1*(i+1)] != ".":
            right = len(memoryBlock) - i - 1 
            break
    while left < right:
        if memoryBlock[left] == "." and memoryBlock[right] != ".":
            temp = memoryBlock[right]
            memoryBlock[right] = "."
            memoryBlock[left] = temp
            left += 1
            right -= 1
        if memoryBlock[left] != ".":
            left += 1
        if memoryBlock[right] == ".":
            right -= 1
    return memoryBlock

def createGapDict(memoryBlock):
    gaps = {}
    i = 0
    while i < len(memoryBlock):
        if memoryBlock[i] == ".":
            j = i
            while memoryBlock[j] == ".":
                j+=1
                if j >= len(memoryBlock):
                    break
            if j-i in gaps:
                gaps[j-i].append(i)
            else:
                gaps[j-i] = [i]
            i = j
        else:
            i+=1
    return gaps

def compressFiles(memoryBlock):
    left = memoryBlock.index(".")
    right = -1
    gaps = createGapDict(memoryBlock)  # gaps[gap_length] = [start_index1, start_index2, ...]
    maxGap = max(gaps.keys())  
    for i in range(len(memoryBlock)):
        if memoryBlock[-1*(i+1)] != ".":
            right = len(memoryBlock) - i - 1 
            break
        
    while left < right:
        if memoryBlock[left] == "." and memoryBlock[right] != ".":
            j = right
            fileSize = -1
            fileId = memoryBlock[right]
            while memoryBlock[j] == memoryBlock[right]:
                j -= 1
            fileSize = right - j
            if fileSize <= maxGap:
                for key in gaps.keys():
                    if fileSize <= key and right > gaps[key][0]:
                        for i in range(fileSize):
                            memoryBlock[gaps[key][0] + i] = fileId
                            memoryBlock[right-i] = "."
                right = j
                gaps = createGapDict(memoryBlock)
            else:
                right = j
        if memoryBlock[left] != ".":
            left += 1
        if memoryBlock[right] == ".":
            right -= 1
    return memoryBlock

def checksum(compressed):
    sum = 0
    for i in range(len(compressed)):
        if compressed[i] != ".":
            sum += int(compressed[i])*i
    return sum

def part1(path):
    f = open(path,"r")
    line = f.readline()
    memoryBlock = generateMemory(line)
    compressed = compress(memoryBlock)
    total = checksum(compressed)
    return total

def part2(path):
    f = open(path,"r")
    line = f.readline()
    memoryBlock = generateMemory(line)
    compressed = compressFiles(memoryBlock)
    total = checksum(compressed)
    return total

#print(part1("C:/Users/mason/Desktop/aoc_2024/dec_10/input.txt"))
#print(generateMemory("12345"))
#print(compressFiles(generateMemory("12345"),"12345"))
#print(checksum(compressFiles(generateMemory("23331331214141314024"))))
print(part2("C:/Users/mason/Desktop/aoc_2024/dec_10/input.txt"))
#print(compressFiles(generateMemory("23331331214141314024")))