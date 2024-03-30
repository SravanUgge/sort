def gen():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

values=gen()

for i in values:
    print(i)

