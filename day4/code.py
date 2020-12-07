def loadData():
    f = open('input.txt', 'r')
    entries = []
    entry = {}
    for row in f.readlines():
        if len(row) < 3:
            entries.append(entry)
            entry = {}
        else:
            row = row.strip('\n')
            for field in row.split(" "):
                x, v = field.split(":")
                entry[x] = v
    return entries


if __name__ == "__main__":
    main()
