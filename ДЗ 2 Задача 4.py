a=int(input("Введіть число: "))
b=int(input("Введіть число: "))
c=int(input("Введіть число: "))
if b<a<c or c<a<b:
    print(a)
elif a<b<c or c<b<a:
    print(b)
else:
    print(c)