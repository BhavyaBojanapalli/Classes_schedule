"""Write a program to print the below pattern
        *
      *   *
    *   *   *"""
def star(n):
  for i in range(1,n):
      print(' '*n, end='') #space for n times
      print('* ' *(i))  #repeat star for i times
      n-=1


def main():
    n=4
    star(4)
main()



