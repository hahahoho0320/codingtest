n = input()
mylist = list(map(int, input().split()))

m = max(mylist)

for i in range(len(mylist)):
    mylist[i]=mylist[i]/m*100

print(sum(mylist)/int(n))
