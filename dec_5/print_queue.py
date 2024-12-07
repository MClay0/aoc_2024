def createOrderingDict(orderingRules):
    tmpDict = {}
    for rule in orderingRules:
        if int(rule.split("|")[0]) in tmpDict:
            tmpDict[int(rule.split("|")[0])].append(int(rule.split("|")[1]))
        else:
            tmpDict[int(rule.split("|")[0])] = [int(rule.split("|")[1])]
    return tmpDict

def isValidUpdate(update,orderingRules):
    processed = []
    unprocessed = [int(x) for x in update]
    for i in range(len(update)):
        if unprocessed[i] in orderingRules:
            for value in orderingRules[unprocessed[i]]:
                if value in processed:
                    return False
                else:
                    processed.append(value)
    return True

def part1():
    path = "c:/Users/mason/Desktop/aoc_2024/dec_5/input.txt"
    
    orderingRules = []
    updates = []
    with open(path) as f:
        for line in f:
            if "|" in line:
                orderingRules.append(line.strip())
            else:
                updates.append(line.strip().split(","))
    rulesDict = createOrderingDict(orderingRules)
    
    validUpdates = []
    for update in updates:
        if isValidUpdate(update,rulesDict):
            validUpdates.append(update)
    
part1()

testRules = '4|2\n1|8\n9|3\n3|6\n6|5\n5|7\n7|1'
testUpdates = [[1,4,6,3,6,2,9,3,2],[2,1,4,5,7],[4,1,8,9,3,6,5,7,1]]
print(isValidUpdate(testUpdates[0],createOrderingDict(testRules.split("\n"))))
print(isValidUpdate(testUpdates[1],createOrderingDict(testRules.split("\n"))))
print(isValidUpdate(testUpdates[2],createOrderingDict(testRules.split("\n"))))