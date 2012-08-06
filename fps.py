

'''
6.8.2012

'''

import pyglet

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

@window.event
def on_draw():
    window.clear()
    #backgroundspr.blit(0,0,width=window.width,height=window.height)
    ai.blit(0,0,width=window.width,height=window.height)
    
    
if __name__ == "__main__":
    pyglet.app.run()   
