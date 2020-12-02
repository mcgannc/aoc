import pandas as pd

def main():
    df = pd.read_csv("input.txt").to_numpy()
    results = []
    for i in range(0, df.size):
        for j in range(0, df.size):
            a = df[i][0]
            b = df[j][0]
            if a+b == 2020:
                result = (a, b, a+b, a*b)
                results.append(result)
    
    print(results)
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
