readings=[23,56,78,12,34,90]
total=0
for r in readings:
    total += r
average=total / len(readings)
print(f"average reading: {average:.2f}")

print(readings[0])