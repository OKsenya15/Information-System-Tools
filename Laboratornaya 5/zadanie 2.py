m = []
s = ['end'] 
while True:
    n = input().split() 
    if n == s:
        break
    else:
        k = min(n, key=int) 
        m.append(k)
for i in m: 
    print(i)
