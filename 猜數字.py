#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
ansbase=[]
bingo=0

print('規則:')
print('請在心中想一串數字或是把它寫下來。(不能有重複的數字)')
print('等等我會開始猜你想的數字但是你必須給我一些提示')
print('當我猜一個答案時A值等於我猜的數字與你的答案中位置與數值都相同的位數量，B值等於數值對但位置錯的位數量')
print('請你告訴我A、B值，我一定會猜到答案!')
yes = True
while yes:
    x = input('看完規則後請輸入yes並按enter繼續：')
    if x == 'yes':
        yes = False
      
n = input('你想的是幾位數呢?')
n = int(n)

for i in range(10**n):
    x = 10
    num_list = []
    for j in range(n):
        num_list.insert(0,i % x)
        i = i //x
    num_list_set = set(num_list)
    if len(num_list_set) == n:
        ansbase.append(num_list)

def ask():
    print('我猜是...')
    print(guess)
    
def ans():
    a=int(input('A值是?'))
    b=int(input('B值是?'))
    return a,b

def think(a,b):
    ref=[]
    for i in range(n):
        ref.append(guess[i])
    for i in range(len(ansbase)):
        target = ansbase[i]
        aa=0
        bb=0
        for j in range(n):
            for k in range(n):
                if target[j]==ref[k]:
                    if j==k:
                        aa+=1
                    else:
                        bb+=1
        if aa!=a or bb!=b:
            ansbase[i]=[-1]
    c=ansbase.count([-1])
    #print(ansbase)
    for i in range(c):
        ansbase.remove([-1])
    #print(len(ansbase))
        
    if len(ansbase)==1:
        print('答案是>>>',ansbase[0])
        return 1
    else:
        return 0

while bingo==0: 
    randnum=random.randint(0,len(ansbase)-1)
    guess = ansbase[randnum]
    ask() 
    tmp=ans()
    a,b=tmp[0],tmp[1]
    bingo=think(a,b)
    #print(bingo)


# In[ ]:




