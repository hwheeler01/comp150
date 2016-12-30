print("A B C A'B+(A+C)")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            print(A, B, C, int(not A and B or (A or C))==int(A or B or C))

print("A B C A+B+C")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            print(A, B, C, int((1 or C) and (A or B or C)))
