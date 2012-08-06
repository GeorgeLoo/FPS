

'''
6.8.2012

'''

import pyglet
from pyglet import clock



window = pyglet.window.Window()
window.set_caption('FPS ver D-0.0')
window.set_size(640,480)
window.maximize()

data='.\\data\\'
drawpath='.\\draw\\'
fname=drawpath+'scene.jpg'
bg = pyglet.image.load(fname)
#backgroundspr.set_position(0,0)
#pyglet.image.ImageData
print bg.width
print bg.width-(bg.width/3)
ai = bg.get_region(bg.width/3, 0, bg.width-(bg.width/3*2), bg.height)

movestop=100
moveleft=110
moveright=120
direct=movestop
leftside=bg.width/3
rightside=bg.width/3*2

def moveleft():
    global leftside,rightside,ai
    move=10
    if leftside-move>0:
        print 'left'
        leftside-=move
        rightside-=move
        ai = bg.get_region(leftside, 0, rightside, bg.height)
    pass

def moveright():
    global leftside,rightside,ai
    move=10
    if rightside+move<bg.width-650:
        leftside+=move
        rightside+=move
        print 'right', leftside,rightside,bg.width
        ai = bg.get_region(leftside, 0, rightside, bg.height)
    pass


@window.event
def on_mouse_motion(x, y, dx, dy):
    global   movestop,moveleft,moveright,direct
    #print x, y, dx, dy
    w=window.width
    h=window.height
    if x>w/3*2:
        direct=moveright
        #moveright()
    elif x < w/3:
        direct=moveleft
        #moveleft()
    else:
        direct=movestop
        pass #print 'stopped'
    
    pass


@window.event
def on_draw():
    window.clear()
    #backgroundspr.blit(0,0,width=window.width,height=window.height)
    ai.blit(0,0,width=window.width,height=window.height)
    
def callback(dt):
    global   movestop,moveleft,moveright,direct
    if direct==moveleft:
        moveleft()
    elif direct == moveright:
        moveright()
    pass

clock.schedule_interval(callback, 0.025)
clock.set_fps_limit(60)

if __name__ == "__main__":
    pyglet.app.run()   




