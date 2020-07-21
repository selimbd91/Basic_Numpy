
import numpy as np
import cv2



class Naresh:

    def __init__(self)OP
        pass

    def matrix(self):

        self.m = int(input("Enter the row size:"))
        self.n = int(input("Enter the column size:"))

        self.mat = np.ndarray(shape= (self.m,self.n), dtype= int)

        print(f"The matrix have {self.m*self.n} elements with {self.m} x {self.n} matrix")

        for i in range(self.m):
            for j in range(self.n):
                self.mat[i][j] = int(input("Enter the value:"))


    def display(self):

        print("The matrix is ......")

        for i in range(self.m):
            for j in range(self.n):
                print(self.mat[i][j], end= "  ")
            print()

    def adsp(self):

        var = np.arange(16, dtype= np.int).reshape(4,4)
        print(var)
        print("\n")


        print(var.shape)

        var2 = np.transpose(var)
        print(var2)

        print("\n")
        print(var.itemsize)

        print("................")
        for i in np.nditer(var, order= "F"):
            print(i, end= "   ")
        print()

    def advance_numpy(self):

        ab = np.arange(25, dtype= np.int16).reshape(5,5)
        print(ab)
        print(np.shape(ab))
        row = ab.shape[0]
        col = ab.shape[1]
        print(f"The row size is:{row}")
        print(f"The Column size is:{col}")

        for i in range(row):
            for j in range(col):
                if i == j:
                    ab[i][j] = 1
                #else:
                    #ab[i][j] = 0

        print(ab)

def main():

    obj = Naresh()
    #obj.matrix()
    #obj.display()
    #obj.adsp()
    obj.advance_numpy()

if __name__ == "__main__":
    main()