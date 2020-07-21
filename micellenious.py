
def add(num1, num2):
    x = lambda a : num1 + num2 + a
    return x

someThingadd = add(2, 3)
print(someThingadd(5))

def quadratice(a, b, c):
    res = lambda x : a*x**2 + b*x + c
    return res

root = quadratice(2, 3, 4)
print(root(2))

def rangaboti():
    #my_list = [2, 3, 4, 5, 6, 7, 8]

    def check(lis):
        for i in lis:
            print(i)
            if i % 2 == 1:
                return i

    my_list = [[2, 6, 4]]

    check = list(filter(check, my_list))
    print(check)

rangaboti()

def fun2():

    def darling(val):
        return val*val

    nums = [2, 3, 4, 5]
    mapNums = list(map(darling, nums))
    print(mapNums)

fun2()


