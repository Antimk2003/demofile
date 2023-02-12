number = int(input("Enter a number : "))
x = 1
while x <= number :
    if x%10==0:
        print(x)
    else:
        print(x, end= " ")
    x = x+1 
