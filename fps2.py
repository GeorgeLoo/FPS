

'''


fps2.py 29.9.2012
----------------------

sounds, 
reload, 
reset
auto fire
fire selection
bullet holes

---------------------

one minute, 
Shots fired, 
on target, 


'''

import pyglet
from pyglet.window import key
from pyglet import clock
import random

class RangePractice:
    def __init__(self,w,h):
	s=self
        self.width = w
        self.height = h
        self.data = '.\\draw\\'
        self.hits = 0
        self.targets = 0
        s.target = self.SpriteLoad('target.jpg')
        self.target.set_position(0,0)
        self.target.scale = 0.3
        self.weapon = self.SpriteLoad('sar21_2.jpg')
        self.weapon.set_position(self.width/4, 1)
        self.weapon.scale = 0.3
        clock.schedule_interval(self.targetcallback, 1.0)
	clock.schedule_interval(self.timercall, 1.0)
        clock.schedule_interval(self.autofirecall, 0.05)
        self.rotc = 0
        self.ResetGame()
	self.sound = Sounds()
	self.status = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=24,
                          x=self.width//2, y = 20)
	self.mousex = 0
	self.mousey = 0
	self.trigger = False
	self.selector = 'safe'
	s.bhole = self.SpriteLoad('bulleth.png',centre=True)
	s.bullL = []
	
    def FireSelect(self):
	s=self.selector
	if s == 'safe':
	    self.selector = 'Semi'
	elif s == 'Semi':
	    self.selector = 'AUTO'
	elif s == 'AUTO':
	    self.selector = 'safe'
	
    def timercall(self, dt):
	if self.timeleft > 0: self.timeleft -= 1
	
    def autofirecall(self,dt):
	if self.trigger and self.selector == 'AUTO': 
	    x = self.mousex
	    y = self.mousey
	    self.mouseright(x,y)
        pass
        
    def ResetGame(self):
	self.magazine = 30
        self.shotsfired = 0
        self.shotsOnTarget = 0
        self.timeleft = 60 # seconds
    
    def SpriteLoad(self, name, centre=False):
        image = pyglet.image.load(self.data+name)
	if centre:
	    image.anchor_x = image.width / 2
	    image.anchor_y = image.height / 2
        return pyglet.sprite.Sprite(image)
        
    def targetcallback(self, dt):
        x = random.randrange(1,self.width-self.target.width)
        y = random.randrange(1,self.height-self.target.height)
        self.target.set_position(x,y)
        #print 'target callback'
    
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
    
    def mousepos(self,x,y):
	#print 'mouse pos'
	self.mousex = x
	self.mousey = y
	#self.mouseright(x,y)
    
    def mouseup(self):
	self.trigger = False
	
    def mouseright(self, x,y):
	s=self
	#print 'fire', self.target.x,self.target.y
	if self.selector == 'safe': return
	#s.bullL.append((x,y))
	s.bhole.x = x
	s.bhole.y = y
	
	self.trigger = True
	self.sound.Play(self.sound.sar21)
	self.magazine -= 1
        self.shotsfired += 1
        l = self.target.x
        t = self.target.y
        r = self.target.x + self.target.width
        b = self.target.y + self.target.height
        rect = [l, t, r, b]
        if self.withinrect(x, y, rect):
	    self.shotsOnTarget += 1
	    #print 'hit'
            self.rotc = 5
            self.target.rotation = -90.0
        pass
    
    def SetStatus(self):
	s=''
	s= 'Shots: '+str(self.shotsfired)
	s=s+' Hits: '+ str(self.shotsOnTarget)
	s=s+' Mode: '+ str(self.selector)
	s=s+' Time: '+ str(self.timeleft)
	
	self.status.text = s
	
    def draw(self):
	s=self
        if self.timeleft > 0: self.target.draw()
        self.weapon.draw()
        self.rotc -= 1
        if self.rotc == 0:
            self.target.rotation = 0.0
	self.SetStatus()
	self.status.draw()
	#for i in s.bullL:
	    #s.bhole.x = i[0]
	    #s.bhole.y = i[1]
	s.bhole.draw()
    
    
    


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
	    pass
            #self.set_fullscreen(False, screen=None)
        if button==pyglet.window.mouse.RIGHT:
            self.o.mouseright(x,y)
	    
    def on_mouse_release(self,x, y, button, modifiers):	   
	if button==pyglet.window.mouse.RIGHT:
	    #print 'mouseup'
	    self.o.mouseup()
	
    def on_mouse_motion(self, x, y, dx, dy):
	#print 'motion'
	#self.o.mousepos(x,y)
	pass
    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
	if buttons==pyglet.window.mouse.RIGHT:
	    #print 'drag'
	    self.o.mousepos(x,y)
	    pass   
    
    def on_key_press(self, symbol, modifiers):
	if symbol == key.F12:
	    self.o.ResetGame()
	elif symbol == key.B:
	    self.o.FireSelect()
	    
	    
    def on_draw(self):
        self.clear()
        self.o.draw()

class Sounds:
	soundpath='.\\sound\\'
	MuteSound = 0
	
	def __init__(self):
		try:
		        self.sar21 = self.Load('sar21.wav')
			#self.wallhit = self.Load('wallhit.mp3')
		except:
			print 'sound file fucked'
		# self. = self.Load('')
		#self.player.queue(self.gunsound)
		
	def Load(self,f):
		#print f
		s = pyglet.media.StaticSource(pyglet.media.load(self.soundpath+f, streaming=False))
		#print s.duration
		#s.play()
		return s

	def Play(self,s):
		if self.MuteSound != 1:
			#print 'sound play'
			s.play()

	def On(self):
		#print 'sound on'
		self.MuteSound = 0

	def Off(self):
		self.MuteSound = 1
	



if __name__ == "__main__":
    m = FPSWin() 
    pyglet.app.run()   
