a = int (input())
b = int (input())
c = int (input())

if a>b and a>c:
    print (" %d 'e o maior numero" % (a))
elif b>a and b>c:
    print (" %d 'e o maior numero" % (b))
elif c>a or c>b:
    print (" %d 'e o maior numero" % (c))
