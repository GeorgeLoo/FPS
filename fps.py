

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
backgroundspr = pyglet.image.load(fname)
#backgroundspr.set_position(0,0)


@window.event
def on_draw():
    window.clear()
    backgroundspr.blit(0,0,width=window.width,height=window.height)

if __name__ == "__main__":
    pyglet.app.run()   
