#QUIZ   if score is 0 want to do the quiz again
score=0

while score==0:

    answer=input("Stack works like?").lower().strip()
    valid_answers=["lifo","last in first out"]
    if answer in valid_answers:
        print("amazing")
        score+=1
    else:
        print("incorrect")

    print()
    
    answer=input("Queues works like?").lower().strip()
    valid_answers=["fifo","first in first out"]
    if answer in valid_answers:   
        print("wow!")
        score+=1
    else:
        print("incorrect")

    print()
    
    q3=input("Who is my favourite one?").lower().strip()
    if q3=="chatgpt":
        print("how do you know that?") 
        score+=1
    else:
        print("incorrect")

    print()
    
    print(f"Score={score}/3")

    if score==0:
        print("get out try again")
    print()

    continue

if score==1:
    print("u lost ur brain")

if score==2:
    print("just one")

else:
    print("gimme ur IG")
     






    


