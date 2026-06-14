
#multiplication table format
y=2
for x in range(0,11):
    answer=x*y
    print(f"{x} * {y} ={answer}")

#fun designs
for x in range(1,5):
               for y in range(1,x+1):
                       print(y,end=" ")
               print()

for i in range(4,0,-1):
        for j in range(4,i-1,-1):
                print(j, end=" ")
        print()

for x in range(1,6):
        for y in range(x):
                print("*",end=" ")
        print()

for i in range(5,0,-1):
        for j in range(i):
                print("*",end=" ")# if ""no space here no space between stars
        print()