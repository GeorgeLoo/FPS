

'''


fps2.py 29.9.2012
----------------------



---------------------



'''

import pyglet
from pyglet.window import key
from pyglet import clock
import random

class RangePractice:
    def __init__(self,w,h):
        self.data = '.\\draw\\'
        self.hits = 0
        self.targets = 0
        self.target = self.SpriteLoad('target.jpg')
        self.target.set_position(100,100)
        self.target.scale = 0.3
        self.weapon = self.SpriteLoad('sar21_2.jpg')
        self.weapon.set_position(300,1)
        self.weapon.scale = 0.3
        clock.schedule_interval(self.callback, 1.0)
        self.width = w
        self.height = h
        self.rotc = 0
    
    def SpriteLoad(self, name):
        image = pyglet.image.load(self.data+name)
        return pyglet.sprite.Sprite(image)
        
    def callback(self, dt):
        x = random.randrange(1,self.width-self.target.width)
        y = random.randrange(1,self.height-self.target.height)
        self.target.set_position(x,y)
        #print 'callback'
    
    def withinrect(self, x,y,r):
        x1,y1=r[0],r[1]
        x2,y2=r[2],r[3]
        if x>x1 and x<x2 and y>y1 and y<y2:
            return True
        return False
    
    def GetSight(self):
        image = pyglet.image.load(self.data+'reticle.png')
        cursor = pyglet.window.ImageMouseCursor(image, 25, 25)
        return cursor
    
    def mouseright(self, x,y):
        l = self.target.x
        t = self.target.y
        r = self.target.x + self.target.width
        b = self.target.y + self.target.height
        rect = [l, t, r, b]
        if self.withinrect(x, y, rect):
            self.rotc = 5
            self.target.rotation = -90.0
        pass
    
    def draw(self):
        self.target.draw()
        self.weapon.draw()
        self.rotc -= 1
        if self.rotc == 0:
            self.target.rotation = 0.0
        pass
    
    pass


class FPSWin(pyglet.window.Window):
    def __init__(self):
        super(FPSWin, self).__init__(resizable = True) 
        self.maximize() 
        #self.set_fullscreen(True, screen=None)
        #self.set_exclusive_mouse()
        #self.set_size(800, 500)
        #self.set_location(500,100)
        self.o = RangePractice(self.width, self.height)
        self.set_mouse_cursor( self.o.GetSight())        
        
    def on_mouse_press(self,x, y, button, modifiers):
        if button==pyglet.window.mouse.LEFT:
            self.set_fullscreen(False, screen=None)
        if button==pyglet.window.mouse.RIGHT:
            self.o.mouseright(x,y)

    def on_draw(self):
        self.clear()
        self.o.draw()

if __name__ == "__main__":
    m = FPSWin() 
    pyglet.app.run()   
