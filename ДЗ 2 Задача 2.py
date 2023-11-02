A=int(input("Введіть число: "))
B=int(input("Введіть число: "))
C=int(input("Введіть число: "))
if (A>0 and B<0 and C<0) or (B>0 and A<0 and C<0) or (C>0 and B<0 and A<0):
    print("TRUE")
else:
    print("FALSE")
    