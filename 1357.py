a,b = input().split()

a = list(a)
b = list(b)

a.reverse()
b.reverse()

a= "".join(a)
b= "".join(b)

sum = int(a)+int(b)
sum = list(str(sum))
sum.reverse()
sum= "".join(sum)
print(int(sum))