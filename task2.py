#task from chitty
# first task(this task is find even and odd then find the count of them between 1 & 10)
even_count=0  #learn someting they should created in start of the code
odd_count=0
for number in range(1,11):
    if number %2 == 0:
        print(f"{number}->Even")
        
    else:
        print(f"{number}->Odd")

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"\nEven_count={even_count}")
print(f"Odd_count={odd_count}")

print()

#second dask(this task is print the numbers and also print the sum of previous numbers)
total=0
for numbers in range(1,11):
    total += numbers
    print(f"{numbers}->{total}")


    
           