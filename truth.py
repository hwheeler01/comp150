print('A B C AB+BC')
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            print(A, B, C, int(A and B or B and C))
