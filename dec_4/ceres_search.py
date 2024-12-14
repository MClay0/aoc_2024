def createCharArr(path):
    charArr = []
    with open(path) as f:
        for line in f:
            charArr.append(list(line.strip()))
    return charArr
    
def part1(filepath):
    charArr = createCharArr(filepath)
    count = 0
    for i in range(len(charArr)):
        for j in range(len(charArr[i])):
            if j < len(charArr[i]) - 3:
                if charArr[i][j] == 'X' and charArr[i][j+1] == 'M' and charArr[i][j+2] == 'A' and charArr[i][j+3] == 'S':   #Horizontal
                    count += 1
                if charArr[i][j] == 'S' and charArr[i][j+1] == 'A' and charArr[i][j+2] == 'M' and charArr[i][j+3] == 'X':
                    count += 1
            if i < len(charArr) - 3:
                if charArr[i][j] == 'X' and charArr[i+1][j] == 'M' and charArr[i+2][j] == 'A' and charArr[i+3][j] == 'S':   #Vertical
                    count += 1
                if charArr[i][j] == 'S' and charArr[i+1][j] == 'A' and charArr[i+2][j] == 'M' and charArr[i+3][j] == 'X':
                    count += 1
            if i < len(charArr) - 3 and j < len(charArr[i]) - 3:
                if charArr[i][j] == 'X' and charArr[i+1][j+1] == 'A' and charArr[i+2][j+2] == 'M' and charArr[i+3][j+3] == 'S': #Top Left to Bottom Right
                    count += 1
                if charArr[i][j] == 'S' and charArr[i+1][j+1] == 'M' and charArr[i+2][j+2] == 'A' and charArr[i+3][j+3] == 'X':
                    count += 1
            if i < len(charArr) - 3 and j > 2:
                if charArr[i][j] == 'X' and charArr[i+1][j-1] == 'M' and charArr[i+2][j-2] == 'A' and charArr[i+3][j-3] == 'S': #Top Right to Bottom Left
                    count += 1
                if charArr[i][j] == 'S' and charArr[i+1][j-1] == 'M' and charArr[i+2][j-2] == 'A' and charArr[i+3][j-3] == 'X':
                    count += 1
    return count

print(part1('C:/Users/mason/Desktop/aoc_2024/dec_4/input.txt'))