def createMap(path):
    path = open(path, "r")
    mapArr = []
    for line in path:
        mapArr.append(list(line))
    return mapArr

def part1(path):
    mapArr = createMap(path)
    facing = "u"
    guard_x, guard_y = 93, 71
    max_x, max_y = len(mapArr)-1, len(mapArr[0])-1
    mapArr[guard_x][guard_y] = "x"
    while True:
        if facing == "u":
            if guard_y == 0:
                break
            elif mapArr[guard_y-1][guard_x] == "#":
                facing = "r"
            else:
                guard_y -= 1
                mapArr[guard_x][guard_y] = "x"
        elif facing == "r":    
            if guard_x == max_x:
                break
            elif mapArr[guard_y][guard_x+1] == "#":
                facing = "d"
            else:
                guard_x += 1
                mapArr[guard_x][guard_y] = "x"      
        elif facing == "d":
            if guard_y == max_y:
                break
            elif mapArr[guard_y+1][guard_x] == "#":
                facing = "l"
            else:
                guard_y += 1
                mapArr[guard_x][guard_y] = "x"
        elif facing == "l":
            if guard_x == 0:
                break
            elif mapArr[guard_y][guard_x-1] == "#":
                facing = "u"
            else:
                guard_x -= 1
                mapArr[guard_x][guard_y] = "x"
    count = 0
    for line in mapArr:
        for char in line:
            if char == "x":
                count += 1
    return count



print(part1("C:/Users/mason/Desktop/aoc_2024/dec_6/input.txt"))