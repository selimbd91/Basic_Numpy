
class string_mama():

    def __init__(self):
        pass

    def fun1(self):

        str1 = "ami tomakei valobasi 100 bar noy anok bar mone koro 200 bar"
        print(str1)

        list1 = str1.split(" ",maxsplit= 2)
        print(list1)
        for i in list1:
            if i.isdigit():
                print(i)


        lis2 = []
        for i in "tomi amar":
            #if not i.isspace():
                lis2.append(i)

        print(lis2)

        newStr = "".join(lis2)
        newStr = newStr + " " + "valobasha"
        print(newStr)

        pam = "".join(["a","v"])
        print(pam)

    def fun2(self):

        string1 = [x for x in range(0, 11)]
        string2 = [i for i in "ABCDE"]
        print(string2)
        print(string1)

        print("....................................")
        tup = [(i,j) for i in string2 for j in string1]
        print(type(tup))


        for i, j in zip(string1, string2):
            print(i, j)

    #def fun3(self):

        
def main():
    obj = string_mama()
    #obj.fun1()
    obj.fun2()

if __name__ == "__main__":
    main()