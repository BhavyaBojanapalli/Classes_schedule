#Write a program to to print myList = [[1, 2, 3, 4, 5], [12, 13, 23], [10, 20, 30], [11, 22, 33], [12, 24, 36]]
#output:
#[1, 2, 3, 4, 5]
#[12, 13, 23]
#[10, 20, 30]
#[11, 22, 33]
#[12, 24, 36]

def test(myList):
    for i in myList:
         print(i)
def main():
    myList = [[1, 2, 3, 4, 5], [12, 13, 23], [10, 20, 30], [11, 22, 33], [12, 24, 36]]
    test(myList)
main()
