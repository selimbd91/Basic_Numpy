
import pandas as pd
import numpy as np

class train_ami:

    def __init__(self):
        pass

    def function1(self):

        my_dict = {"A": [1, 2, 3, 4], "B": [5, 6, 7, 8],
                   "C": [8, 9, 5, 6], "D": [2, 5, 6, 8]}
        df = pd.DataFrame(my_dict)
        print(df)
        print("<<<<<<<<>>>>>>>>")

        print(df.sort_index(axis=1, ascending=False))
        print("--------")
        print(df.sort_index(axis=0, ascending=False))

        #print(df)
        #print("...........")
        #num = df.to_numpy()
        #print(num)
        df2 = pd.DataFrame(np.random.randint(1, 21, [5,4]))
        print(df2)
        #df2.columns = ["selim", "Roman", "karim", "rahim"]e        print(df2)


def main():

    obj = train_ami()
    obj.function1()

if __name__ == "__main__":
    main()