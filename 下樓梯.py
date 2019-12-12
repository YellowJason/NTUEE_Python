#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pygame as pg
import random
#初始化
pg.init()
#建立視窗
width,height = 450,700
screen = pg.display.set_mode((width, height))
pg.display.set_caption("下樓梯")        
#建立畫面
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((200,200,0))
#顯示
screen.blit(bg, (0,0))
pg.display.update()
#建立時間元件
clock = pg.time.Clock()

speed = 2#樓梯運動速度
boxs = []#樓梯
T = 0#時間

#程式運行
running = True
while running:
    clock.tick(100)
    T += 1
    speed += 0.0005
    period = 50
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    if T % period == 0:#新增樓梯
        x_rand = random.randint(-50,350)
        boxs.append([int(x_rand),680])
    
    screen.blit(bg,(0,0))#重繪視窗
    
    for i in boxs:#每個樓梯做一次
        i[1] -= speed
        if i[1] < 0:
            boxs.remove(i)
        box = pg.Surface((150,20))#建立繪圖區
        box.fill((255,255,255))
        pg.draw.rect(box,(100,100,100),[0,0,150,20],30)#畫樓梯
        rect = box.get_rect()#樓梯區塊
        rect.center = (i[0],i[1])#左上角起始位置
        screen.blit(box, rect.center)
    
    
    
    pg.display.update()#更新視窗
 
pg.quit()


# In[ ]:





# In[ ]:




