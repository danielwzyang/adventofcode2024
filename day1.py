with open("a.in") as f:
    left = []
    right = []
    counts = {}
    for line in f:
        ints = [int(x) for x in line.strip().split()]
        left.append(ints[0])
        right.append(ints[1])
        counts[ints[1]] = counts.get(ints[1], 0) + 1
    
    left.sort()
    right.sort()
    
    sum = 0
    for i in range(len(left)):
        sum += left[i] * counts.get(left[i], 0)
    
    print(sum)