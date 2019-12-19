#!/usr/bin/env python
# coding: utf-8

# In[11]:


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
bg_color_r = 200
bg_color_g = 200
bg.fill((bg_color_r,bg_color_g,0))
#顯示
screen.blit(bg, (0,0))
pg.display.update()
#建立時間元件
clock = pg.time.Clock()
#樓梯
box_list = []
#時間
T = 0
#起始速度
speed = 3
#樓梯
class boxs:
    def __init__(self):
        self.x = random.randint(-70,380)
        self.y = 680
        self.width = random.randint(120,160)
        self.box = pg.Surface((self.width,20))#建立繪圖區
        self.box.fill((255,255,255))
        
    def built(self):
        pg.draw.rect(self.box,(100,100,100),[0,0,self.width,20],30)#畫樓梯
        self.rect = self.box.get_rect()#樓梯區塊
        self.rect.center = (self.x,self.y)
        
    def draw(self):
        screen.blit(self.box,self.rect.center)
        
    def update(self):
        self.y -= speed
#柴柴
class kids:
    def __init__(self):
        self.x = box_list[0].x + 50
        self.y = 625
        self.kid = pg.Surface((50,55))
        self.kid.fill((255,255,255))
        self.up = False
        
    def built(self):
        pg.draw.rect(self.kid,(255,255,255),[self.x,self.y,50,55],30)#畫小朋友
        self.rect = self.kid.get_rect()#小朋友區塊
        self.rect.center = (self.x,self.y)
        
    def draw(self):
        self.kid = pg.image.load("柴柴.png")
        self.kid.convert()
        screen.blit(self.kid,self.rect.center)
        
    def y_update(self):
        #確認是否在樓梯上
        self.up = False
        for i in box_list:
            if 40 < i.y - self.y < 55 and (i.x - 40) <= self.x <= (i.x + i.width -10):
                self.up = True
        #垂直移動
        if self.up:
            self.y -= speed
        else:
            self.y += speed
            
    def x_update(self):
        keys = pg.key.get_pressed()#按鍵dict
        #確認是否按方向鍵
        if keys[pg.K_LEFT] and keys[pg.K_RIGHT]:
            pass
        elif keys[pg.K_LEFT]:
            self.x -= speed
        elif keys[pg.K_RIGHT]:
            self.x += speed

#建立第一個樓梯
box = boxs()
box_list.append(box)
#建立柴柴
kid = kids()
#程式運行
running = True
while running:
    T += 1#算時間
    clock.tick(60)#幀數
    if speed <= 9:
        if T % 600 == 0:
            speed += 1#加速
            bg_color_r += 5#加深顏色
            bg_color_g -= 20
            bg.fill((bg_color_r,bg_color_g,0))
            
    period = int(100/speed)#樓梯出現時間
    
    for event in pg.event.get():#關閉程式
        if event.type == pg.QUIT:
            running = False
            
    if T % period == 0:#新增樓梯
        box = boxs()
        box_list.append(box)
    
    screen.blit(bg,(0,0))#重繪視窗
        
    for i in box_list:#每個樓梯畫一次
        i.update()
        if i.y < 0:
            box_list.remove(i)
        i.built()
        i.draw()
        
    kid.x_update()#更新柴柴座標
    kid.y_update()
    kid.built()#畫柴柴
    kid.draw()
    
    pg.display.update()#更新視窗
 
pg.quit()


# In[ ]:





# In[ ]:




