T = int(input('Enter an no.='))
for i in range(T):
    n = input("Enter an value")

    while True:
        n = str(int(n)+1)
        # there is no repition in set
        sn = set(n)
        if (len(n) == len(sn)):
            break
    print(n)
