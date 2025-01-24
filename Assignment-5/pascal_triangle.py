def pascals_triangle(n):
    
    result = []
    
    for i in range(n):
        
        row = []
        
        for j in range(i + 1):
            
            row.append(combination(i, j))
        
        result.append(row)
    
    return result

def combination(n, r):
   
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

def factorial(n):
    
    f = 1
    for i in range(1, n + 1):
        f = f * i
   
    return f

n = int(input("Enter your number: "))
for row in pascals_triangle(5):
    print(row)