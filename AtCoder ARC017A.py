a =int(input())
i = 5
flag = True
if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
    flag = False
while i * i <= a :
    if a % i == 0 or a % (i+2) == 0:
        flag = False
        break
    i += 6
if flag == True:
    print("YES")
else:
    print("NO")
