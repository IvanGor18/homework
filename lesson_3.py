#1
n = int(input())
s = 0
for i in range(1, n+1):
    s += i ** 3
print(s)

##2
for i in range(1, 10):
    for j in range(1, 10):
        print("%5d" % (i * j),end='')
    print()

## 3

a = [1,2,4,5,6,7,8,9,10]

a.reverse()

for i in range(0,len(a)):
    print(str(a[i]))
