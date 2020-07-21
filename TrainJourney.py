
import pandas as pd
import numpy as np
import random

class JourneyByTrain:

    def __init__(self):
        pass

    def fun1(self):
        my_dic = {"Name" : ["selim", "roman", "somon", "karim", "rahim"],
                  "ID" : [123, 124, 125, 126, 127],
                  "University" : "university of Bremen",
                  "CGPA" : [4, 5, 6, 7, 6],
                  "Major" : ["cmm", "cit", "cit", "cmm", "english"]}

        df = pd.DataFrame(my_dic, index= ["A", "B", "C", "D", "E"])
        print(df)
        df.loc["B", "University"] = "university of Soudia"

        print("<<<<<<<<<<<>>>>>>>>>>>>>")
        print(df.loc[["A","C"], ["Name", "CGPA", "Major"]])
        print("<<<<<<<<<<<>>>>>>>>>>>>>")
        print(df)
        #df.to_csv("writeTocsb")
        print("<<<<<<<<<<<>>>>>>>>>>>>>")
        print(df.loc["B", : ])


    def matrixa(self):
        mat1 = np.array([[1, 2, 3],[4, 5, 6,],[7, 8, 9]])
        print(mat1[ [0,2], [0,2]])
        #mat2 = np.matrix(mat1)
        print("<<<<<<<<<<<>>>>>>>>>>>>>")
        print(mat1)

    def practice_csv(self):

        df_csv = pd.read_csv("practice.csv")
        print(df_csv.head())

    def myNumpy(self):

        row = int(input("please enter the row:"))
        col = int(input("please enter the column:"))
        sal = np.ndarray(shape= [row, col], dtype= "int16")
        for i in range(row):
            for j in range(col):

                sal[i][j] = random.randint(0, 10)
            #print()

        print(sal)
        ab = sal[0,[1,3,4]]
        bc = sal[1,[1, 2, 3]]
        cd = sal[2,[1,2, 4]]
        lo = np.vstack([ab, bc, cd])
        print(lo)
        for i in range(len(sal)):
            for j in range(len(sal[i])):
                if i == j:
                    print(sal[i][j], end="\t")
            print()

    def poja(self):
        """this doc for the poja apu"""
        lst = [["name",["selim", "rahim"]], ["age", [22, 23]]]
        print(lst)

        dic = dict(lst)
        print(dic.values())
def main():
    obj = JourneyByTrain()
    #obj.fun1()
    #obj.matrixa()
    #obj.practice_csv()
    #obj.myNumpy()
    print(obj.poja.__doc__)

if __name__ == "__main__":
    main()
