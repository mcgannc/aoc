import pandas as pd
import numpy as np

TARGET = 2020


def bruteForceSolution():
    inputList = pd.read_csv("input.txt").to_numpy()
    for i in range(0, inputList.size):
        for j in range(0, inputList.size):
            a = inputList[i][0]
            b = inputList[j][0]
            if a + b == TARGET:
                result = (a, b, a + b, a * b)
                print(result)
                return

    print("No joy")


def linearTimeSolution():
    """Ignores integers outside range of [1, TARGET] """

    inputList = pd.read_csv("input.txt").to_numpy()

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

    # Now process the candidateList, and check if the remainder was also recorded
    for candidate in candidateList:
        alternate = TARGET - candidate
        if numbersFound[alternate - 1] == 1:
            result = (candidate, alternate, candidate * alternate)
            print(result)
            return

    print("No joy")


if __name__ == "__main__":
    # execute only if run as a script
    #bruteForceSolution()
    linearTimeSolution()
