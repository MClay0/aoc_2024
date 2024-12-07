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
            try:
                if charArr[i][j] == 'X' and charArr[i][j+1] == 'M' and charArr[i][j+2] == 'A' and charArr[i][j+3] == 'S':
                    count += 1
                if charArr[i][j] == 'S' and charArr[i][j+1] == 'A' and charArr[i][j+2] == 'M' and charArr[i][j+3] == 'X':
                    count += 1
                    
                if charArr[i][j] == 'X' and charArr[i+1][j] == 'M' and charArr[i+2][j] == 'A' and charArr[i+3][j] == 'S':
                    count += 1
                if charArr[i][j] == 'S' and charArr[i+1][j] == 'A' and charArr[i+2][j] == 'M' and charArr[i+3][j] == 'X':
                    count += 1
                
                if charArr[i][j] == 'X' and charArr[i+1][j+1] == 'A' and charArr[i+2][j+2] == 'M' and charArr[i+3][j+3] == 'S':
                    count += 1
                if charArr[i][j] == 'S' and charArr[i+1][j+1] == 'M' and charArr[i+2][j+2] == 'A' and charArr[i+3][j+3] == 'X':
                    count += 1
            except IndexError:
                pass
    return count

print(part1('C:/Users/mason/Desktop/aoc_2024/dec_4/input.txt'))