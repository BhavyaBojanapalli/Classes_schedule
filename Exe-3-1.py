# Write a program to count number of 'a' characters in the string 'aishwarya' with while and if loop.

def test(i, n):
    count = 0
    while(i < len(n)):
        if(n[i] == 'a'):
            count += 1
        #print(i)
        i += 1
    print(count)


def main():
    i = 0
    n = "aishwarya"
    test(i, n)


main()
