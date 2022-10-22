b=[[]*10 for _ in range(10)]
for i in range(10):
    b[i]=list(map(int,input().split()))
x=1
y=1
b[x][y]=9
while True:
    if(b[x][y]==2):
        b[x][y]=9
        break
    if(b[x][y+1]!=1):
        b[x][y]=9
        y+=1
    else:
        if(b[x+1][y]!=1):
            b[x][y]=9
            x+=1
        else:
          b[x][y]=9
          break
for i in range(10):
    for j in range(10):
        print(b[i][j],end=' ')
    print()
        