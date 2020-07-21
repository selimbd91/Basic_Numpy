
def fibo():

    a, b = 0, 1

    while True:
        #yield a
        print(a)
        a, b = b, a+b

        if a >= 50:
            break

print(type(fibo()))
#for i in fibo():
   # if i >= 50:
     #   break
   # print(i)

