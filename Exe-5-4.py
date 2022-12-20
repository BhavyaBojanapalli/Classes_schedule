"""Write a program to print the below pattern
        *
      *   *
    *   *   *"""
def star(n):
  for i in range(n):
    for j in range(i+1):
        print(" * ", end='')
    print()

def main():
    n=3
    star(3)
main()
