#task from chitty
# first task
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

#second dask
total=0
for numbers in range(1,11):
    total += numbers
    print(f"{numbers}->{total}")


    
           