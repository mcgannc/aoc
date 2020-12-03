import pandas as pd
import numpy as np

TARGET = 2020
INPUT_FILE = "input.txt"


def prepareInput():
    inputList = pd.read_csv(INPUT_FILE).to_numpy()

    numbersFound = np.arange(TARGET)
    candidateList = []

    # Pre-process the input to get the candidate values and recall what has been seen
    for i in range(0, inputList.size):

        candidate = inputList[i][0]

        # Skip numbers that cannot be part of a solution
        if candidate < 1 or candidate >= TARGET:
            continue

        # Skip if seen already
        if numbersFound[candidate - 1] == 1:
            continue

        # Record the candidate
        candidateList.append(candidate)
        numbersFound[candidate - 1] = 1

    return candidateList, numbersFound


def factorPair(candidateList, numbersFound, target):
    # Now process the candidateList, and check if the remainder was also recorded
    for candidate in candidateList:
        remainder = target - candidate
        if remainder > 0 and numbersFound[remainder - 1] == 1:
            return (candidate, remainder)

    return None


def factorTriple(candidateList, numbersFound, target):
    # Now process the candidateList, and check if the remainder was also recorded
    for candidate in candidateList:
        remainder = target - candidate
        factoredPair = factorPair(candidateList, numbersFound, remainder)
        if factoredPair:
            return candidate, factoredPair[0], factoredPair[1]

    return None


def main():
    candidateList, numbersFound = prepareInput()

    a, b = factorPair(candidateList, numbersFound, TARGET)
    print((a, b, a + b, a * b))

    a, b, c = factorTriple(candidateList, numbersFound, TARGET)
    print((a, b, c, a + b + c, a * b * c))


if __name__ == "__main__":
    # execute only if run as a script
    main()
