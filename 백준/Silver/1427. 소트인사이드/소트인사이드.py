n = list(map(int, str(input())))

n.sort(reverse=True)
print(''.join(map(str,n)))