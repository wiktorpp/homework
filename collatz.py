def collatz(n):
    if n==1:
        raise ValueError
    if n%2 == 0:
        return int(n/2)
    else:
        return (3*n) + 1

n=int(input(">"))
i=1
while True:
    try:
        n = collatz(n)
    except ValueError:
        print("End")
        exit()
    print(f"{i} -> {n}")
    i+=1
