n = int(input())

lis = []
for  i in range(n):
        lis.append(input())

lis = list(set(lis))
lis.sort(key=lambda x : (len(x),x))


for j in range(len(lis)):
        print(lis[j])