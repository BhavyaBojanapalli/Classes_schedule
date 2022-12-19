#Write a program to print numbers in reverse order i.e n=5 output is (4,3,2,1,0)

def test(n):
    while(n>0):
        n=n-1
        print(n)

def main():
    test(5)
main()

""""
def test(i,n):
    while(i>=n):
        print((i))
        i-=1
def main():
    test(0,5)
main()"""