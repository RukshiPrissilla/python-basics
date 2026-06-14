 #nested conditions
material="steel"
temp = 1600
if material == "steel":
    if temp > 1500:
        print ("steel melting")
    else:
        print("steel is still solid")

if material=="steel" and temp > 1500:
    print("steel is molten")

import math
force=float(input("enter the force"))
area=float(input("enter the area"))

stress=force/area
yield_strength=250_000_000

print(f"stress={stress:.2f}")

#if stress<yield_strength*0.5:
   # print("safe:")
#elif stress<yield_strength:
  #  print("warning")
#else:
   # "print("critical")

