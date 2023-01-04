#Write a program to print all the even numbers up to n ( n is the input n=10)

"""num = 10
for i in range(num):
     if num%2 == 0:
        print(count)"""


"""def test(n):
    for i in range(n):
        if i%2 == 0:
            print(i)
def main():
    n= 10
    test(n)
main()"""

def test(n):
    for i in range(n):
        if i%2 != 0:
            print(i)

def main():
    n= 20
    test(n)
main()