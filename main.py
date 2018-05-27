

a = '1-1'

x = None
y = None

if len(a) == 2 :
    x = int(a[0])
    y = int(a[1])
elif len(a) == 4:
    x = int(str(a[0])+str(a[1]))
    y = int(str(a[2])+str(a[3]))

elif len(a) == 3:
    if a[0] == '-':
        x = int(str(a[0])+str(a[1]))
        y = int(a[2])

    elif a[1] == '-':
        x = int(a[0])
        y = int(str(a[1])+str(a[2]))


print(x, y)