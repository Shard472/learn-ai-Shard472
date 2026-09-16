tree = list(map(int,input().split()))
hand = int(input())
## print(tree)
n=0

for i in range(0,len(tree)):
    if tree[i] <= hand + 30 :
        n+=1

print(n)

