def chessboard(a, b):
    for i in range(1, a+1):
        for j in range(1, b+1):
            
            if (i+j) % 2 == 0:
               
                print("#", end=" ")
            else:
               
                print("*", end=" ")
        print()


num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

chessboard(num1, num2)