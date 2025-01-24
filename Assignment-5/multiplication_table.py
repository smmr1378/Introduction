def multiplication_table(a, b):
    for i in range(1, a+1):
        for j in range(1, b+1):
            print(i*j, end=" ")
        print()

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

multiplication_table(num1, num2)