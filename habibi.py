
import numpy as np

class Vacation:

    def __init__(self):
        pass

    def fun1(self):
        """"Habibi ki nain and nikle hai farabi
        and its f string practice and so be careful"""
        name = "selim Hossain"
        profession = "student"

        string = f"hello {name.capitalize()} "
        print(f"What is your profession and how is your day now?")
        str3 = f"my profession is {profession.capitalize()} "
        print(string, str3)

    def mutableNiaKaj(self):

        lst = [[1, 3], [5, 6]]
        print(type(lst))
        print(lst)
        print(np.size(lst))
        print(np.ndim(lst))
        lst = ["selim", "hossain", "is", "my", "name"]
        name = "selim hossain is my name "
        lst1 = name.split()
        print(lst1)
        name1 = " ".join(lst)
        print(name1)

    def pattern(self):

        row = int(input("Please enter the row Number:"))

        for i in range(row):
            for j in range(row-i,0,-1):
                print(" ", end= "")
            for k in range(i+1):
                print("*", end="")
            print()
def main():
    obj = Vacation()
    #obj.fun1()
    #obj.mutableNiaKaj()
    obj.pattern()

if __name__ == "__main__":
    main()