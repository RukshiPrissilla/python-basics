#task like ask for num if that num plus it gives the square if tht num minus it skips tht num if it 0 the program should be stoped

def Square(a):
    return a**2

while True: #infinite loop
    a=int(input("Enter a number(0 to stop):"))
    if a==0:
        print("Program ended")
        break #stops here 
        
    if a<0:
        print("Negative numbers are skipped")
        
    if a>0:
        print(f"Square={Square(a)}")


        
    