def parseLine(line):
    enabled = findEnabled(line)
    cur = 0

    matcher = "mul("
    sum = 0
    n = len(line)
    l = 0
    r = 0
    while r < n:
        if r - l == 4:
            l = r

            # search for first int
            while line[r].isdigit():
                r += 1
            if l == r or line[r] != ",":
                l = r
                continue

            a = int(line[l:r])

            r += 1
            l = r

            # search for second int
            while line[r].isdigit():
                r += 1
            if l == r or line[r] != ")":
                l = r
                continue

            b = int(line[l:r])

            if shouldAdd(r, enabled):
                sum += a * b

            r += 1
            l = r
            
            continue
        
        if line[r] != matcher[r - l]:
            l = r
            if line[r] != "m":
                r += 1
            continue
            
        r += 1

    return sum

def shouldAdd(pos, enabled):
    cur = len(enabled) - 1
    while enabled[cur][0] > pos:
        cur -= 1
    return enabled[cur][1]

def findEnabled(line):
    res = [(0, True)]
    n = len(line)
    last = 0
    while last < n:
        do = line.find("do()", last)
        if do == -1:
            break
        res.append((do, True))
        last = do + 4
    last = 0
    while last < n:
        dont = line.find("don't()", last)
        if dont == -1:
            break
        res.append((dont, False))
        last = dont + 7
    
    res.sort()
    return res

        

with open("a.in") as f:
    sum = 0
    for line in f:
        sum += parseLine(line)
    print(sum)

    