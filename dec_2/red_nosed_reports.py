def ascOrDesc(nums):
    ascending = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
    descending = all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))
    return ascending or descending

def isGradual(nums):
    flag = True
    for i in range(len(nums)-1):
        difference = abs(nums[i+1] - nums[i])
        if difference < 1 or difference > 3:
            flag = False
    return flag

def isSafe(nums):
    return ascOrDesc(nums) and isGradual(nums)

def safeWhenRemoved(nums):
    for i in range(len(nums)):
        if isSafe(nums[:i] + nums[i+1:]):
            return True
    return False
def part1(filepath):
    safeCount = 0
    with open(filepath, "r") as f:
        for line in f:
            report = [int(x) for x in line.split()]
            if isSafe(report):
                safeCount += 1
    return safeCount 

def part2(filepath):
    safeCount = 0
    with open(filepath, "r") as f:
        for line in f:
            report = [int(x) for x in line.split()]
            if isSafe(report):
                safeCount += 1
            else:
                if safeWhenRemoved(report):
                    safeCount += 1
    return safeCount 
    
path = "C:/Users/mason/Desktop/aoc_2024/dec_2/input.txt" 
print(part1(path))
print(part2(path))

