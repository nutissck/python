N=int(input())
if N>=0 and N<=5:
    print("LOW")
elif N>=6 and N<=10:
    print("AVERAGE")
elif N>=11 and N<=50:
    print("HIGH")
elif N>50:
    print("DISASTER")
