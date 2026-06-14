
print(list(range(1,10)))
print(list(range(0,10,4)))

#to calculate the total value of even numbers between 1 and 100
total = 0
for i in range(0,101,2):
    total += i
print(total)

#while loop
number = 5
while(number != 0):
    print("Hello")
    number -= 1  #number=number-1

for counter in (1,2,3,4,5):
        print (counter)

n=10
while n>0:
     print(n)
     n-=1
     if n==5:
          break

n=10
while n>0:
     n-=1
     if n==5:
          continue 
     print(n)

#for loop
val=int(input("enter number:"))
for x in range(0,val):
     for y in range(0,val):
          print('*',end='')
     print('')
     
numbers=(3,2,6)
for number in numbers:
    print("looking at:",number)   
    if number == 9:
        print("found number")
        break
    else:print("number not found")
    print("end")


#while loop
count = 0
while count < 5:   #while True infinity loop
    print(count)
    count += 1   #ithu illadi 0 continuos aakum

#break and continue
for n in range(1,100):
    if n*n>50:
        print(f"{n} is the first number whose square exceeds 50")
        break
    
for n in range(1,11):
    if n%2==0:
      continue
    print(n)

while True:
    value=input("enter a positive number")
    number=float(value)
    if number>0:
        break
    print("not positive try again")
print(f"u enter the {number}")


