

'''


fps2.py 29.9.2012
----------------------



---------------------



'''

import pyglet
from pyglet.window import key
from pyglet import clock

def withinrect(x,y,r):
    x1,y1=r[0],r[1]
    x2,y2=r[2],r[3]
    if x>x1 and x<x2 and y>y1 and y<y2:
        return True
    return False

class RangePractice:
    def __init__(self):
        self.data = '.\\draw\\'
        self.hits = 0
        self.targets = 0
        image = pyglet.image.load(self.data+'target.jpg')
        self.target = pyglet.sprite.Sprite(image)
        self.target.set_position(100,100)
        self.target.scale = 0.3
        
    def GetSight(self):
        image = pyglet.image.load(self.data+'reticle.png')
        cursor = pyglet.window.ImageMouseCursor(image, 25, 25)
        return cursor
    
    def mouseright(self, x,y):
        pass
    
    def draw(self):
        self.target.draw()
        
        pass
    
    pass


class FPSWin(pyglet.window.Window):
    def __init__(self):
        super(FPSWin, self).__init__(resizable = True) 
        #self.maximize() 
        #self.set_fullscreen(True, screen=None)
        #self.set_exclusive_mouse()
        self.set_size(800, 500)
        self.set_location(500,100)
        self.o = RangePractice()
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
