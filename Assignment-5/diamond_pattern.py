def diamond(height):
  height = int(input("Enter your number: "))
  if height % 2 == 0:
    print("Height must be an odd number")
    return
  
  for x in range(height//2 + 1):
   
    spaces = height//2 - x
    
    stars = 2*x + 1
    
    print(" " * spaces + "*" * stars)
 
  for x in range(height//2 - 1, -1, -1):
    
    spaces = height//2 - x
    
    stars = 2*x + 1
    print(" " * spaces + "*" * stars)

diamond(5)