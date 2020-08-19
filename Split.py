def minCashFlowRec(amount):
    maxCredit=amount.index(max(amount))
    maxDebit=amount.index(min(amount))
    if amount[maxCredit]==0 and amount[maxDebit]==0:
        return
    
    Min=min(-amount[maxDebit],amount[maxCredit])
    amount[maxCredit]-=Min
    amount[maxDebit]+=Min
    
    print('Person',maxDebit,'pays',Min,'to person',maxCredit)
    minCashFlowRec(amount)
    
n=int(input('Enter no nodes: '))

graph=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append(0)
    graph.append(b)
        
d=0
while d==0:
    a,b,c=map(int,input('Enter the value: ').split())
    graph[a][b]=c
    d=int(input('enter 1 to break 0 to continue: '))
    
amount=[]
for i in range(n):
    amount.append(0)


for i in range(n):
    for j in range(n):
        amount[i]+=(graph[j][i] - graph[i][j])


minCashFlowRec(amount)
