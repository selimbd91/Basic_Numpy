
def fun2():

    result = "Manchester United 1 Chelse 0, Tottenham Hotspur 3 Manchester United 1, Manchester United 2 Liverpool 4, Aston Villa 1 Manchester United 32, Manchester City 3 Manchester United 4, Swensea 2 Manchester United 5, Manchester United 2 West Ham 2"
    ab = result.split(",") # First i split this string to list with the help of comma separate.
    print(ab) #i just show how the result of list


    target1 = [] # i just made one empty list for future
    target2 = [] # i just made second empty list for future

    for i in ab:
        # i just run a for loop over the list
        i = i.strip(" ") # use strip function to remove the white space

        if i.startswith("Manchester United"): # i just checked is the team Manchester United is first or not

            for kk in i.split(" "):
                if kk.isnumeric(): # i just checked where is the numeric number
                    target1.append(int(kk)) # when i got numeric number i append on my target1 list


        elif not i.startswith("Manchester United"): # Similarly, i checked if Manchester United  is not in first then i did the same thing

            for p in i.split():
                if p.isnumeric(): # i checked the number
                    target2.append(int(p)) # put the number on target2 list
        else:
            print("i just follow about the question and i made in this way")


    target3 = list(reversed(target2)) # i reverse target2 because i like to keep the Manchester United score first
    target4 = target1 + target3 # i just concatenation and make one complete list target4




    #print(target1) # in this list Manchester United score and other team score
    #print(target2) # in this list other team score and Manchester United score
    #print(target3) # in this list Manchester United score and other team score
    #print("the final result is.....")
    #print(target4) # in this list Manchester United score and other team score

    count = 0
    los = 0
    draw = 0

    for i in range(0, len(target4), 2):
        # Now, i will check how many games Manchester United Win, Loss and draw
        if target4[i] > target4[i+1]:
            count += 1
        elif target4[i] < target4[i+1]:
            los += 1
        else:
            draw = draw + 1

    print(f"Manchester United Win-> {count} times")
    print(f"Manchester United Loss-> {los} times")
    print(f"Manchester United  Draw-> {draw} times")

fun2()