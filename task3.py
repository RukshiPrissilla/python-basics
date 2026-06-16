#task from chitty(task like using lsts and loops)
total=0
numbers=[3, 8 , 5, 12 , 7]

print("Numbers:")

for number in numbers:  #to get numers only from the list
    print(number,end=" ")
print()

print("Even Numbers:")

for number in numbers:
    if number % 2 == 0:
         print(number)

print("Odd Numbers:")

for number in numbers:
    if number % 2 != 0:
        print(number) 

for number in numbers:
    total+=number
print(f"sum={total}") 

Largest=numbers[0]
for number in numbers:
    if number > Largest:
       Largest=number
print(f"Largest={number}")

a=max(numbers)  #max min in whole list
print(f"largest in another way={a}")
