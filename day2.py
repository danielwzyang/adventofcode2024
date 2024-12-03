def validRow(row, removed=False):
    increasing = row[1] - row[0] > 0
    for i in range(1, len(row)):
        diff = row[i] - row[i - 1]
        if ((diff > 0) ^ increasing) or abs(diff) < 1 or abs(diff) > 3:
            if not removed:
                for i in range(len(row)):
                    newRow = [x for j, x in enumerate(row) if i != j]
                    if validRow(newRow, True):
                        return True
            return False

    return True

with open("a.in") as f:
    count = 0
    for line in f:
        row = [int(x) for x in line.strip().split()]
        increasing = row[1] - row[0] > 0
        if validRow(row): count += 1
    
    print(count)
            

