#Write a program to print all the even numbers up to n ( n is the input n=10)

num = 10
count = 0
for i in range(num):
     count+=1
     if count%2 == 0:
        print(count)


"""def test(n, count):
    for i in range(n):
        count+=1
    if count%2 == 0:
        print(count)
def main():
    n= 10
    count = 0
    test(n,count)
main()"""