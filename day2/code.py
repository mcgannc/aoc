import pandas as pd


def checkPassword(entry, policy):
    counts, letter, password = entry
    a, b = [int(s) for s in counts.split("-")]
    return policy(a, b, letter[0], password), counts, letter, password


def policy1(minCount, maxCount, letter, password):
    count = password.count(letter)
    return count >= minCount and count <= maxCount


def policy2(pos1, pos2, letter, password):
    return len(password) >= pos2 and ((password[pos1 - 1] == letter) ^
                                      (password[pos2 - 1] == letter))


def main():
    inputList = pd.read_csv('input.txt', delim_whitespace=True,
                            header=None).to_numpy()
    results1 = [
        x for x in map(lambda entry: checkPassword(entry, policy1), inputList)
        if x[0] == True
    ]
    results2 = [
        x for x in map(lambda entry: checkPassword(entry, policy2), inputList)
        if x[0] == True
    ]

    print(len(results1), len(results2))


if __name__ == "__main__":
    main()
