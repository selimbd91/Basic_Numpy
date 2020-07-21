import numpy as np
import pandas as pd

class TensionLife:

    def __init__(self):
        pass

    def display(self):
        print("yes, it's work perfectly")

    def padna_work(self):

        dic = {"country" : ["bangladesh", "india", "srilanka", "pakistan", "afghanistan"],
               "capital" : ["dhaka", "delhi", "columbo", "islamabad", "kabul"],
               "population" : [10, 30, 5, 22, 15],
               "age" : [2, 3, 4, 5, 6]
               }
        for key, value in dic.items():
            print(key, value, sep="----->")

        df = pd.DataFrame(dic)
        print(df)

        df2 = df[df["age"] == df["age"].max()]
        #df3 = df2[["country", "age"]]

        #print(df2[["country", "age"]])
        print(".......")
        print(df2)

def main():
    obj = TensionLife()
    obj.display()
    obj.padna_work()

if __name__ == "__main__":
    main()