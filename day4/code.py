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


REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def isValid(passport):
    for field in REQUIRED_FIELDS:
        if field not in passport:
            return False
    return True


def main():
    passports = loadData()
    validPassports = [passport for passport in passports if isValid(passport)]
    return validPassports


if __name__ == "__main__":
    main()
