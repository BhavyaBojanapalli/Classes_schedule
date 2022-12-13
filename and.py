#Write a program to check if x is divided by y and y is divided by z(print 'true' and else 'false')(x=100, y =10 and z=5)

def test(x,y,z):
    if(x%y==0 and y%z==0):
        print("true")
    else:
        print("false")
def main():
    test(100,10,5)
main()