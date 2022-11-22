userInput = int(input("Input an integer:\n"))
a = 1
while (True):
    b = a ** 2
    if (b > userInput):
        print("Integer square root is " + str(a-1))
        break
    else:
        a = a + 1
