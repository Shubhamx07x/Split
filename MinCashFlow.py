#this is the code for minimising cash flow coded in python 3
import tkinter
win=tkinter.Tk()
win.geometry("386x200")
win.title("MoneySplit")
L1=tkinter.Label(win,text="Giver Index")
L1.grid(row=0,column=0)
L2=tkinter.Label(win,text="Receiver Index")
L2.grid(row=1,column=0)
L3=tkinter.Label(win,text="Amount")
L3.grid(row=2,column=0)

E1=tkinter.Entry(win,bd=3)
E1.grid(row=0,column=1)
E2=tkinter.Entry(win,bd=3)
E2.grid(row=1,column=1)
E3=tkinter.Entry(win,bd=3)
E3.grid(row=2,column=1)


def minCashFlowRec(amount):                  #main program for cost minimisation
    a=[]
    maxCredit=amount.index(max(amount))
    maxDebit=amount.index(min(amount))
    if amount[maxCredit]==0 and amount[maxDebit]==0:
        return a

    Min=min(-amount[maxDebit],amount[maxCredit])
    amount[maxCredit]-=Min
    amount[maxDebit]+=Min
    
    a.append(print('Person',maxDebit,'pays',Min,'to person',maxCredit))
    minCashFlowRec(amount)
    
    

n=100                                       #Manimum no. of nodes or friends
graph=[]                                    #initialising the graph with zeros
for i in range(n):
    b=[]
    for j in range(n):
        b.append(0)
    graph.append(b)

    

        
        
def inputfunc():                             #user inputs
        if(E1.get().isdigit()):
            a=int(E1.get())
        if(E2.get().isdigit()):
            b=int(E2.get())
        if(E3.get().isdigit()):
            c=int(E3.get())
            graph[a][b]=c 
  
        E1.delete(first=0,last=10)
        E2.delete(first=0,last=10)
        E3.delete(first=0,last=10)




def netcash():                               #function to find net amount with each node/friend
    amount=[]
    for i in range(n):
        amount.append(0)
    for i in range(n):
        for j in range(n):
            amount[i]+=(graph[j][i] - graph[i][j])
    return amount
    
    
B1=tkinter.Button(win,text=" Exit ",command=win.destroy)
B1.grid(row=4,column=0)
B2=tkinter.Button(win,text="Next Entry",command=inputfunc)
B2.grid(row=4,column=1)
B3=tkinter.Button(win,text=" Done ",command=lambda:minCashFlowRec(netcash()))
B3.grid(row=4,column=2)

win.mainloop()


