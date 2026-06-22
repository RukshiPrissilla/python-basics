#learn something new if i want high marks i want to create a list and then want to add them.
#want to update the code like when i type the name with num it want to show me error and the marks also
names=[]
scores=[]
for i in range (1,6):
    print(f"student {i}")
    name=str(input("name:"))
    score=float(input("score:"))
    names.append(name)
    scores.append(score)
print(f"highest score:{max(scores)}")

