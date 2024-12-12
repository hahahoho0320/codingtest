N = input()

s = len(str(N))
sum1 = 0
sum2 = 0

for i in range(s//2):
    sum1 += int(N[i])
    
for i in range(s//2, s):
    sum2 += int(N[i])

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')