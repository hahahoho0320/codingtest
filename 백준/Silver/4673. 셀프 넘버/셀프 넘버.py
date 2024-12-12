box = [1]*10001

for i in range(1,10001):
    if sum(list(map(int, list(str(i))))) + i <= 10000:
        box[sum(list(map(int, list(str(i))))) + i]=0 

for i in range(1, 10001):
    if box[i] == 1:
        print(i)
