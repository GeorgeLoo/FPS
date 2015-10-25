


'''

                         _
 _._ _..._ .-',     _.._(`))
'-. `     '  /-._.-'    ',/
   )         \            '.
  / _    _    |             \
 |  a    a    /              |
 \   .-.                     ;  
  '-('' ).-'       ,'       ;
     '-;           |      .'
        \           \    /
        | 7  .__  _.-\   \
        | |  |  ``/  /`  /
       /,_|  |   /,_/   /
          /,_/      '`-'
          



-----------------------------------------          



30 round shotgun
grenade delayed
cluster bombs delayed
waves of tangos
flanking tangos
stealth covered tangos, emerge to shoot, then hide
mortar! use sniper enhance

magnum gun
modify the grenade launcher to be similar
to the claymore
shotguns

MOUSE TO GO NEXT, PREV SCENES
children as terrorists! with RPGs
hide and seek tactics from the terrorists
Child suicide bombers
mortar from the top
RPG from the sides and bottom

/two bullets to kill one normal trooper

/run or walk via caps lock
mission selection screen
injured face like Duke Nukem
/moving hostages panic
/taking cover
/Claymore 700 ball bearings

night shootouts
mp7 rifle with silencer

/2 images for hostages      
/Barrett Browning  M82 CQ
/go through walls, kill tango commandos with one shot    
      /see through walls with scope

?tablet version
Fellow shooters with Ai
/medical kits
shoot and shatter glass
guards and evasion
/trigger waypoints
long distance shooting! sniper rifle!
?show dead bodies in 3 positions: left, right, upside down!
assassinations
deeper missions
scenario announcement
scenario chooser
improve tango generation
background music
show next mission
give a summary of the performance
/fight against special forces who take 5 shots before dying


/weapons restriction!
/pause that pauses the bullets - important!
/campaign mode
          
/reset stats    F1 key 13.3.2015
/prevent hero from going off screen   14.3.2015 pi day
tango random shooters
tango intelligent fire
tango intelligent movement, flanking!

game suicide bombers
/game hostages
hostage with timer shootings

/different rates of auto fire
small message window
bullets that can shoot through the walls!
blow cover away with bombs
/Hero cursor wasd movement
/Tangos will target Hero
RPG countdown to explosion

tangos
hostages
cover
sniper rifle and distances
blood?
/headshots

/leg shots

shield for storming rooms

weapon accuracy
range
rate of auto fire

Pistol
    Name
    Graphic
    Aiming cursor
    Sound firing
    Sound hit
    Safe, Semi
    Number of rounds
    Reload()
    Choose()
    Draw()
    DrawRounds()
    Fire()
    Selector()

Knife - sheathed, stab/slash/throw

Silenced Pistol

Glock automatic pistol

Samurai sword

Parachute avoid 'obstacles'

Maze grid when covert missions


    
Rifle
Safe Semi Auto

Sniper Rifle
Safe Semi

Mini-gun
50 round a second!
4400 round box

SAW
safe Auto

Shotgun
spread shot

Stun granade
safe armed

Grenade
Safe Armed

Rocket
Safe Semi

Artillery
Coords
Confirm

auto fire

---------------

explosion objects

Grenades as well.
Grenade multiple launcher


use proper consts
better structure for 
changing weapons
use hash to get to weapons instead of if-then-else


'''

import pyglet
from pyglet.window import key
from pyglet import clock
import random

#import Tkinter, tkMessageBox

class Const():
    foo = 15589888
    
    folder = '.\\draw\\'
    backgroundFolder = '.\\background\\'
    knifeKbar = 'KBar knife'
    pistol1911 = 'M1911 pistol'
    knifeSafe = 'safe'
    knifeArmed = 'armed'
    knifeThrow = 'throw'
    knifeModes = (knifeSafe,knifeArmed,knifeThrow)
    pistolSafe = 'safe'
    pistolSemi = 'semi'
    pistolModes = (pistolSafe,pistolSemi)
    M4assaultRifle = 'M4 Carbine'
    assaultRifleSafe = 'safe'
    assaultRifleSemi = 'semi'
    assaultRifleAuto = 'auto'
    assaultRifleModes = (assaultRifleSafe,assaultRifleSemi,assaultRifleAuto)
    machineGunModes = (assaultRifleSafe,assaultRifleAuto)
    SAR21Rifle = 'SAR21'
    Ultimax100SAW = 'Ultimax 100 SAW'
    M134MiniGun = 'M134 Mini-Gun'
    M32GRENADElauncher = 'M32 Multi-Grenade Launcher'
    STCPW = 'ST KINETICS CPW'
    GLOCK = 'GLOCK 18'
    M249SAW = 'M249 SAW'
    M107sniper = 'M107 Sniper Rifle'
    ClaymoreMine = 'M18 Claymore'
    MP5 = 'MP5 PDW'
    AK47 = 'AK 47'
    MP7silent = 'MP7 silencer'
    
    suicideBomber = not False #whether can get close to tangos
    HandToolConst = 'Hand Tool'
    
class Sounds:
    soundpath='.\\sound\\'
    MuteSound = 0

    def __init__(self):
        try:
            self.minigunSound = self.Load('minigunsound.wav')
            self.sar21 = self.Load('sar21.wav')
            self.reLoad = self.Load('reload.wav')
            self.m1911 = self.Load('M1911pistolsound.wav')
            self.m4carbine = self.Load('M4carbineSound.wav')
            self.pain = self.Load('Pain-SoundBible.com-1883168362.wav')
            self.heropain = self.Load('Pain-Hero.wav')
            self.m32MGL = self.Load('grenadeLauncher.wav') #grenadeLauncher.wav
            self.hostageHitsound = self.Load('HostageFemaleScream1.wav')
            self.hostageRescuedSound = self.Load('ThankYouBritishWoman.wav')
            self.stcpwsnd = self.Load('CPWsound.wav')
            self.glocksnd = self.Load('Glocksound.wav')
            self.m249sawSound = self.Load('M249_SAW.wav')
            self.m107Sound = self.Load('M107.wav')
            self.m18Sound = self.Load('Claymore.wav')
            self.reliefSound = self.Load('Ahhh.wav')
            self.curedSound = self.Load('Ahhhh.wav')
            self.mp5sound = self.Load('mp5sound.wav')
            self.AK47sound = self.Load('ak47a.wav')
            self.mp7sound = self.Load('mp7silencer.wav')
            #self.stcpwsnd = self.Load('')
                #self.wallhit = self.Load('wallhit.mp3')
            self.player = pyglet.media.Player()
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

    def Player(self,s):
        self.player.queue(s)
        self.player.play()

    def Play(self,s):
        if self.MuteSound != 1:
            #print 'sound play'
            s.play()

    def Stop(self):
        self.player.pause()
        pass

    def On(self):
        #print 'sound on'
        self.MuteSound = 0

    def Off(self):
        self.MuteSound = 1

gSound = Sounds()


def SpriteLoad(name, centre=False):
    image = pyglet.image.load(name)
    if centre:
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2
    return pyglet.sprite.Sprite(image)

class MessageWin(pyglet.window.Window):
    def __init__(self,title):
        super(MessageWin, self).__init__(resizable = False) 
        self.set_size(800, 600)
        self.set_location(300,50)
        self.maximize() 
        self.set_caption(title)
        
        self.lines = []
        i = 0
        g = self.height - 50
        while i < 4:
            self.label = pyglet.text.Label('line '+str(i),
                                  font_name='Times New Roman',
                                  font_size=16,
                                  x=50, y=g)
                                  #anchor_x='center', anchor_y='center')        
                                  
            self.lines.append(self.label)
            g -= 25
            i+=1
        
    def on_mouse_release(self,x, y, button, modifiers):	 
        #self.close()
        #self.set_visible(visible=False)
        #self.minimize() 
        #self.set_visible(visible=False) 
        pass
    def on_draw(self):
        self.clear()
        #self.switch_to()
        for i in self.lines:
            i.draw()
    def hide(self):
        self.set_fullscreen(False, screen=None)
        self.set_visible(visible=False) 
    def show(self):
        self.set_visible(visible=True) 
        self.set_fullscreen(True, screen=None)
    def on_close(self):
        #self.set_visible(visible=False) 
        pass
    def setText(self,text,line):
        self.lines[line].text = text
    def on_key_press(self, symbol, modifiers):
        if symbol == key.I:
            self.hide()
            
            
        
gmw = MessageWin('Battle Report')

class BattleReport():
    def __init__(self):
        self.init()
    def init(self):
        print 'Battle report init'
        self.numberheadshot = 0
        self.numberbodyhit = 0
        self.numberblasted = 0
        self.numLegHits = 0
        self.herohit = 0
        self.heroblasted = 0
        self.hostagesHit = 0
        self.hostagesRescued = 0
        self.herokilled = 0
        self.TangoShotDead = 0
    #alternative way to gather data
    #but delay in reporting data
    def add(self,v):
        self.report()
        return v + 1
        
    def report(self):
        if self.herohit > 9:
            self.herokilled += 1
            self.herohit = 0
        s = 'hero hit '+str(self.herohit)+ \
            ' blasted '+ str(self.heroblasted) +\
            ' killed ' + str(self.herokilled)
        gmw.setText(s,0)
        s = 'tango headhit ' + str(self.numberheadshot) + \
            ' tango bodyhits ' + str(self.numberbodyhit) + \
            ' tango leg hits ' + str(self.numLegHits)
        gmw.setText(s,1)
        s = 'tango blown up ' + str(self.numberblasted)
        gmw.setText(s,2)
        #totalTangoHits = self.numberheadshot + \
            #self.numberbodyhit + self.numLegHits + \
            #self.numberblasted + self.heroblasted
        s = 'Total Tango casualties ' + str(self.TangoShotDead) +\
            ' Hostages hit ' + str(self.hostagesHit) + \
            ' Rescued ' + str(self.hostagesRescued)
        gmw.setText(s,3)
        pass
    
gBattleRep = BattleReport()
#gBattleRep.numberbodyhit += 1
#BattleReport.bullshit = 37
#print gBattleRep.numberbodyhit, BattleReport.bullshit
#gBattleRep.report()
#tkMessageBox.showinfo('Battle Report','Stuff')
#gmw.switch_to()
#gmw.show()
#gmw.setText('fuck'+' pap',0)     




'''

       Bystanders
Movement all over the place
stats
explosions
bullets


'''


'''

      Hostages
Moving / stationary
crying sounds
statistics tracked
different looks
statistics
drawing

'''    


class Hostages():
    def __init__(self):
        self.hostageList = []
        self.deadhostagelist = []
        self.hostageSprite = SpriteLoad(Const.folder+'hostage1.jpg',centre=False)
        self.hostageSprite.scale = 0.25
        self.deadhostageSprite = SpriteLoad(Const.folder+'hostage1.jpg',centre=False)
        self.deadhostageSprite.scale = 0.25
        self.deadhostageSprite.rotation = -90.0
        
        h2s = 0.1
        self.hostage2Sprite = SpriteLoad(Const.folder+'hostage2.jpg',centre=False)
        self.hostage2Sprite.scale = h2s
        self.deadhostage2Sprite = SpriteLoad(Const.folder+'hostage2.jpg',centre=False)
        self.deadhostage2Sprite.scale = h2s
        self.deadhostage2Sprite.rotation = 90.0
        
        
        self.panic = False
        self.sound = gSound
        self.moveDir = 'up'
        self.winw = 0
        self.winh = 0
        clock.schedule_interval(self.autocall, 1.0)
    
    def setPanic(self,v):
        self.panic = v
        
    def autocall(self,dt):
        if self.panic:
            self.panicMove()
        else:
            self.move()
        pass
    def panicMove(self):
        gw = self.hostageSprite.width / 1
        gh = self.hostageSprite.height / 1
        for i in self.hostageList:
            tx = i[0]
            ty = i[1]
            d = random.randrange(1,9)
            if d == 1:
                self.moveDir = 'up'
            elif d == 2:
                self.moveDir = 'down'
            elif d == 3:
                self.moveDir = 'left'
            elif d == 4:
                self.moveDir = 'right'
                
                
            if self.moveDir == 'up':
                if ty - gh > 0:
                    ty -= gh
            elif self.moveDir == 'down':
                if ty + gh < self.winh:
                    ty += gh
            elif self.moveDir == 'left':
                if tx - gw > 0:
                    tx -= gw
            elif self.moveDir == 'right':
                if tx + gw < self.winw:
                    tx += gw
            i[0] = tx    
            i[1] = ty
    
        pass
    
    
    def move(self):
        gw = self.hostageSprite.width / 8
        gh = self.hostageSprite.height / 8
        for i in self.hostageList:
            tx = i[0]
            ty = i[1]
            if self.moveDir == 'up':
                ty -= gh
            elif self.moveDir == 'down':
                ty += gh
            elif self.moveDir == 'left':
                tx -= gw
            elif self.moveDir == 'right':
                tx += gw
            i[0] = tx    
            i[1] = ty
            
        if self.moveDir == 'up':
            self.moveDir = 'down'
        elif self.moveDir == 'down':
            self.moveDir = 'left'
        elif self.moveDir == 'right':
            self.moveDir = 'up'
        elif self.moveDir == 'left':
            self.moveDir = 'right'
        pass
    def create(self,num,winWidth,winHeight):
        self.winw = winWidth
        self.winh = winHeight
        i = 0
        self.deadhostagelist = []
        while i < num:
            x = random.randrange(1,winWidth-100)
            y = random.randrange(1,winHeight-100)
            t = random.randrange(1,3)
            self.hostageList.append([x,y,t])
            i += 1
        
    def Rescue(self,bx,by):
        for i in self.hostageList:
            tx = i[0]
            ty = i[1]
            l = tx
            t = ty 
            r = tx + self.hostageSprite.width
            b = ty + self.hostageSprite.height
            rect = [l, t, r, b]
            if withinrect( bx, by, rect):
                #print 'hostage saved'
                self.sound.Play(self.sound.hostageRescuedSound)
                gBattleRep.hostagesRescued += 1
                gBattleRep.report()
                self.hostageList.remove(i)
        
    def hit(self,bx,by):
        for i in self.hostageList:
            tx = i[0]
            ty = i[1]
            ht = i[2]
            l = tx
            t = ty 
            if t == 1:
                r = tx + self.hostageSprite.width
                b = ty + self.hostageSprite.height
            else:
                r = tx + self.hostage2Sprite.width
                b = ty + self.hostage2Sprite.height
                
            rect = [l, t, r, b]
            if withinrect( bx, by, rect):
                #print 'hostage hit'
                self.sound.Play(self.sound.hostageHitsound)
                gBattleRep.hostagesHit += 1
                gBattleRep.report()
                a = [tx,ty,ht]
                self.deadhostagelist.append(a)
                self.hostageList.remove(i)
        pass
    def HitGrenade(self,grenaderect):
        for i in self.hostageList:
            tx = i[0]
            ty = i[1]
            ht = i[2]
            if withinrect( tx, ty, grenaderect):
                self.sound.Play(self.sound.hostageHitsound)
                gBattleRep.hostagesHit += 1
                gBattleRep.report()
                self.hostageList.remove(i)
                a = [tx,ty,ht]
                self.deadhostagelist.append(a)
        
        pass
    def draw(self):
        for i in self.hostageList:
            x = i[0]
            y = i[1]
            t = i[2]
            if t == 1:
                self.hostageSprite.set_position(x,y)
                self.hostageSprite.draw()
            else:
                self.hostage2Sprite.set_position(x,y)
                self.hostage2Sprite.draw()
                
        for i in self.deadhostagelist:
            x = i[0]
            y = i[1]
            t = i[2]
            if t == 1:
                self.deadhostageSprite.set_position(x,y)
                self.deadhostageSprite.draw()
            else:
                self.deadhostage2Sprite.set_position(x,y)
                self.deadhostage2Sprite.draw()
    
        
class BulletHoles():
    def __init__(self):
        self.maxholes = 40
        self.bulletHoles = []
        self.holeSprite = SpriteLoad(Const.folder+'bulleth.png',centre=True)
        self.holeSprite.scale = 0.5
    def record(self,x,y):
        self.bulletHoles.append((x,y))
    def draw(self):
        for i in self.bulletHoles:
            self.holeSprite.x = i[0]
            self.holeSprite.y = i[1]
            self.holeSprite.draw()
        if len(self.bulletHoles) > self.maxholes:
            self.bulletHoles = []

'''

animate explosions
sound handled elsewhere
'''
class Explosion():
    def __init__(self):
        self.exploList = []
        self.imageFrames = []
        self.maxframe = 4
        self.ex0 = SpriteLoad(Const.folder+'explo0.png',centre=True)
        self.ex1 = SpriteLoad(Const.folder+'explo1.png',centre=True)
        self.ex2 = SpriteLoad(Const.folder+'explo2.png',centre=True)
        self.ex3 = SpriteLoad(Const.folder+'explo3.png',centre=True)
        self.imageFrames.append(self.ex0)
        self.imageFrames.append(self.ex1)
        self.imageFrames.append(self.ex2)
        self.imageFrames.append(self.ex3)
        clock.schedule_interval(self.autocall, 0.05)
    def autocall(self,dt):
        for i in self.exploList:
            f = i[2] #which frame
            f += 1
            if f < self.maxframe:
                i[2] = f
            else:
                self.exploList.remove(i)
        pass
    
    def add(self,x,y):
        a = [x,y,0]
        self.exploList.append(a)
        pass
    def draw(self):
        for i in self.exploList:
            f = i[2]
            self.imageFrames[f].set_position(i[0],i[1])
            self.imageFrames[f].draw()
        pass


            
class Hero():
    def __init__(self):
        self.heroSprite = SpriteLoad(Const.folder+'hero1.png',centre=True)
        self.heroSprite.scale = 0.25
        self.heroSprite.set_position(100,100)
        self.factor = 2
        self.heroHITSprite = SpriteLoad(Const.folder+'hero1hit.jpg',centre=True)
        self.heroHITSprite.scale = 0.25
        self.heroHITSprite.set_position(100,100)
        
        self.move = 'stop'
        clock.schedule_interval(self.autocall, 0.125)
        self.heroHittimer = 0
        self.status = pyglet.text.Label('Hero Health',
                                        font_name='Times New Roman',
                                        font_size=24,
                                        x=1000, y = 20)
        
    def autocall(self,dt):
        self.doMovement()
        if self.heroHittimer > 0:
            self.heroHittimer -= 1
        pass
    def setRunning(self, run):
        if not run:
            self.factor = 2
        else:
            self.factor = 1  #run
            
    def setscreen(self,w,h):
        self.winWidth = w
        self.winHeight = h
        print 'setscreen'
    def doMovement(self):
        self.saveherox = self.heroSprite.x
        self.saveheroy = self.heroSprite.y
        if self.move == 'up':
            self.heroSprite.y += self.heroSprite.height / self.factor
        elif self.move == 'left':
            self.heroSprite.x -= self.heroSprite.width / self.factor
        elif self.move == 'back':
            self.heroSprite.y -= self.heroSprite.height / self.factor
        elif self.move == 'right':
            self.heroSprite.x += self.heroSprite.width / self.factor
        
        if self.heroSprite.x > self.winWidth or \
           self.heroSprite.x < 0:
            self.heroSprite.x = self.saveherox
            
        if self.heroSprite.y > self.winHeight or \
           self.heroSprite.y < 0:
            self.heroSprite.y = self.saveheroy
        
        
        pass
    def resetPos(self):
        self.heroSprite.set_position(100,100)
    
    def draw(self):
        s = 'Hits '+ str(gBattleRep.herohit) \
            + ' Killed ' + str(gBattleRep.herokilled)
        self.status.text = s
        self.status.draw()
        if self.heroHittimer == 0:
            self.heroSprite.draw()
        else:
            x = self.heroSprite.x
            y = self.heroSprite.y
            self.heroHITSprite.set_position(x,y)
            self.heroHITSprite.draw()
    def goUp(self):
        self.move = 'up'
        #print 'up'
        #self.heroSprite.y += self.heroSprite.height / self.factor
        pass
    def goLeft(self):
        self.move = 'left'
        #self.heroSprite.x -= self.heroSprite.width / self.factor
        pass
    def goBack(self):
        self.move = 'back'#self.heroSprite.y -= self.heroSprite.height / self.factor
        pass
    def goRight(self):
        self.move = 'right'#self.heroSprite.x += self.heroSprite.width / self.factor
    def stopMoving(self):
        self.move = 'stop'
        pass
    def hit(self):
        #print 'hero hit check'
        #print 'xxx hero hit'
        self.heroHittimer = 20  #how long to show the 'hit' drawing
    
def HandleModeSelect(modes,currMode):
    #print Const.foo
    i = 0
    while i < len(modes):
        if currMode == modes[i] and i < len(modes)-1:
            return modes[i+1]
        i += 1
    return modes[0]


def withinrect( x,y,r):
    x1,y1=r[0],r[1]
    x2,y2=r[2],r[3]
    if x>x1 and x<x2 and y>y1 and y<y2:
        return True
    return False


'''

man figure must go past to trigger
red to green

1   2   3

'''
class Waypoints():
    def __init__(self):  
        self.redSpr = SpriteLoad(Const.folder+'wayRed.png',centre=False)
        self.greenSpr = SpriteLoad(Const.folder+'wayGreen.png',centre=False)
        self.orangeSpr = SpriteLoad(Const.folder+'wayOrange.png',centre=False)
        #self.coverSpr.scale = 0.2
        self.stateOff = 'Orange'
        self.stateOn = 'Green'
        self.stateWrong = 'Red'
        self.reset()
        clock.schedule_interval(self.autocall, 2.0)
        pass
    def autocall(self,dt):
        for i in self.waylist:
            if i[2] == self.stateWrong:
                i[2] = self.stateOff
                
    def draw(self):
        for i in self.waylist:
            x = i[0]
            y = i[1]
            state = i[2]
            if state == self.stateOff:
                self.orangeSpr.set_position(x,y)
                self.orangeSpr.draw()
            elif state == self.stateOn:
                self.greenSpr.set_position(x,y)
                self.greenSpr.draw()
            elif state == self.stateWrong:
                self.redSpr.set_position(x,y)
                self.redSpr.draw()
                
        pass
    
    def checkhit(self,x,y):
        for i in self.waylist:
            wx = i[0]
            wy = i[1]
            wx1 = wx + self.orangeSpr.width
            wy1 = wy + self.orangeSpr.height
            r = [wx,wy,wx1,wy1]
            
            if withinrect(x, y, r):
                if i[2] != self.stateOn \
                   and self.checkNum(i[3]):
                    i[2] = self.stateOn
                    return True
                elif i[2] == self.stateOff:
                    i[2] = self.stateWrong
                
        return False
    
    def checkNum(self,n):
        if n == self.expected:
            self.expected += 1
            return True
        return False
    
    def complete(self):
        if self.waylist == []:
            return False
        ret = 0
        for i in self.waylist:
            if i[2] == self.stateOn:
                ret += 1
        return (ret == len(self.waylist))
    
    def add(self,x,y):
        state = self.stateOff
        a = [x,y,state,self.number]
        self.waylist.append(a)
        self.number += 1
        pass
    def reset(self):
        self.waylist = []
        self.number = 1
        self.expected = 1
        
        
    
'''
goes in front of the tangos to provide cover for bullets
typeofcover
'''
class CoverLayer():
    def __init__(self):  
        self.coverSpr = SpriteLoad(Const.folder+'brick_texture___9_by_agf81-d3a20h2.jpg')
        self.coverSpr.scale = 0.2
        #self.coverSpr.set_position(x,y)
    def Hit(self,where,x,y):
        #tx = self.coverSpr.x
        #ty = self.coverSpr.y
        tx = where[0]
        ty = where[1]
        l = tx
        t = ty 
        r = tx + self.coverSpr.width
        b = ty + self.coverSpr.height
        rect = [l, t, r, b]
        if withinrect( x, y, rect):
            #print 'cover hit'
            return True
        
        pass
    def Draw(self,where):
        x = where[0]
        y = where[1]
        self.coverSpr.set_position(x,y)
        self.coverSpr.draw()

def GetDirection():
    d = random.randrange(1,9)
    return d
def MoveXY(d,x,y,tw,th,ww,wh):
    base = 50
    mx = x
    my = y
    if d == 1:
        if my + th < wh:
            my += th
    elif d == 5:        
        if my - th > base:
            my -= th
    elif d == 3 or d == 2:
        if mx + tw < ww:
            mx += tw
    elif d == 7 or d == 4:        
        if mx - tw > 0:
            mx -= tw
    return mx,my


'''
ninja stealth
five bullets to kill one
cannot be killed by grenade
dead bodies list
'''
class TangoCommando():
    def __init__(self):
        self.target = SpriteLoad(Const.folder+'tango1image.png')
        self.target.scale = 0.2
        self.deadtarget = SpriteLoad(Const.folder+'tango1image.png')
        self.deadtarget.scale = 0.2
        self.deadtarget.rotation = 90 #degrees
        self.deadlist = []
        self.sound = gSound
        self.boardlist = []
        print 'init Target'
        print self.target.width, self.target.height
    def create(self,number,winW,winH):
        i = 0
        self.boardlist = []
        self.deadlist = []
        while i < number:
            x = random.randrange(1,winW)
            y = random.randrange(500,winH)
            a = [x,y,0]
            self.boardlist.append(a)
            i+=1
            
        pass
    def getList(self):
        return self.boardlist
    def tangoDead(self):
        if not self.boardlist == []:
            return False
        return True
    def move(self,w,h):
        i = 0
        while i < len(self.boardlist):
            d = GetDirection()
            tw = self.target.width / 2 
            th = self.target.height / 2
            x = self.boardlist[i][0]
            y = self.boardlist[i][1]
            numhit = self.boardlist[i][2]
            #x = self.target.x
            #y = self.target.y
            #if not numhit > 4:
            rx,ry = MoveXY(d, x,y,tw, th, w, h)
            self.boardlist[i][0] = rx
            self.boardlist[i][1] = ry
            i+=1
            #return rx,ry
    def TangoShotcheck(self,x,y):
        for where in self.boardlist:
            if self.Hit(x, y, where):
                self.sound.Play(self.sound.pain)
                self.boardlist.remove(where)
            pass
        
    def Hit(self,x,y,where): #commmando
        tx = where[0]
        ty = where[1]
        numhit = where[2]
        
        l = tx
        t = ty + self.target.height/4*3
        r = tx + self.target.width
        b = ty + self.target.height
        recthead = [l, t, r, b]
        
        l = tx
        t = ty + self.target.height/4
        r = tx + self.target.width
        b = ty + self.target.height/4*3
        rectbody = [l, t, r, b]
        
        l = tx
        t = ty 
        r = tx + self.target.width
        b = ty + self.target.height/4
        rectlegs = [l, t, r, b]
        
        if withinrect( x, y, recthead):
            #print 'head hit'
            gBattleRep.numberheadshot += 1
            gBattleRep.report()
            numhit += 1
            #return True
        elif withinrect( x, y, rectbody):
            #print 'body hit'
            gBattleRep.numberbodyhit += 1
            gBattleRep.report()
            #self.sound.Play(self.sound.pain)
            numhit += 1
            #return True
        elif withinrect( x, y, rectlegs):
            #print 'leg hit'
            #gBattleRep.numLegHits = gBattleRep.add( gBattleRep.numLegHits)
            gBattleRep.numLegHits += 1
            gBattleRep.report()
            #self.sound.Play(self.sound.pain)
            numhit += 1
            #return True
        else:
            #print 'miss'
            return False
        
        where[2] = numhit
        if numhit > 4:
            a = [where[0],where[1]]
            self.deadlist.append(a)
            gBattleRep.TangoShotDead += 1
            gBattleRep.report()
            return True  #to have sound and register as dead
        else:
            return False
        
    def Draw(self):
        for i in self.boardlist:
            self.target.set_position(i[0],i[1])
            self.target.draw()
            
        for i in self.deadlist:
            self.deadtarget.set_position(i[0],i[1])
            self.deadtarget.draw()
            

class TargetBoard():
    def __init__(self):
        #self.target = SpriteLoad(Const.folder+'terrorist.png')
        #self.target.scale = 0.3
        #self.sound = gSound
        #self.deadtarget = SpriteLoad(Const.folder+'terrorist.png')
        #self.deadtarget.scale = 0.3
        #self.deadtarget.rotation = 90
        #self.target.set_position(x,y)
        #self.target.rotation = -90.0
        #self.hitlist = []
        self.boardlist = []
        self.deadlist = []
    def create(self,number,winW,winH,Tangotype):
        
        print 'init Target'
        if Tangotype == 'real':
            name = 'terrorist.png'
            sz = 0.3
            self.target = SpriteLoad(Const.folder+name)
            self.target.scale = sz
            self.sound = gSound
            self.deadtarget = SpriteLoad(Const.folder+name)
            self.deadtarget.scale = sz
            self.deadtarget.rotation = 90
            print self.target.width, self.target.height
        else:
            name = 'target0.jpg'
            sz = 0.2
            self.target = SpriteLoad(Const.folder + name)
            self.target.scale = sz
            self.sound = gSound
            self.deadtarget = SpriteLoad(Const.folder + name)
            self.deadtarget.scale = sz
            self.deadtarget.rotation = 90
            print self.target.width, self.target.height
        
        i = 0
        self.boardlist = []
        self.deadlist = []
        while i < number:
            x = random.randrange(1,winW)
            y = random.randrange(500,winH)
            a = [x,y,0]
            self.boardlist.append(a)
            i+=1
            
        pass
    def getList(self):
        return self.boardlist
    def getDeadlist(self):
        return self.deadlist
    def tangoDead(self):
        if self.boardlist != []:
            return False
        return True
    
    def move(self,w,h):
        #print 'move',self.target.x,w,h
        i = 0
        while i < len(self.boardlist):
            d = GetDirection()
            tw = self.target.width / 2 
            th = self.target.height / 2
            x = self.boardlist[i][0]
            y = self.boardlist[i][1]
            numhit = self.boardlist[i][2]
            #x = self.target.x
            #y = self.target.y
            rx,ry = MoveXY(d, x,y,tw, th, w, h)
            self.boardlist[i][0] = rx
            self.boardlist[i][1] = ry
            i+=1
            #return rx,ry
            
    def TangoShotcheck(self,x,y):
        for where in self.boardlist:
            if self.Hit(x, y, where):
                self.sound.Play(self.sound.pain)
                a = [x,y]
                #self.deadlist.append(a)
                self.boardlist.remove(where)
            pass
        
    def Hit(self,x,y,where):
        tx = where[0]
        ty = where[1]
        numhit = where[2]
        
        l = tx
        t = ty + self.target.height/4*3
        r = tx + self.target.width
        b = ty + self.target.height
        recthead = [l, t, r, b]
        
        l = tx
        t = ty + self.target.height/4
        r = tx + self.target.width
        b = ty + self.target.height/4*3
        rectbody = [l, t, r, b]
        
        l = tx
        t = ty 
        r = tx + self.target.width
        b = ty + self.target.height/4
        rectlegs = [l, t, r, b]
        
        if withinrect( x, y, recthead):
            #print 'head hit'
            gBattleRep.numberheadshot += 1
            gBattleRep.report()
            numhit += 1
            #return True
        elif withinrect( x, y, rectbody):
            #print 'body hit'
            gBattleRep.numberbodyhit += 1
            gBattleRep.report()
            numhit += 1
            #return True
        elif withinrect( x, y, rectlegs):
            #print 'leg hit'
            #gBattleRep.numLegHits = gBattleRep.add( gBattleRep.numLegHits)
            gBattleRep.numLegHits += 1
            gBattleRep.report()
            numhit += 1
            #return True
        else:
            #print 'miss'
            return False
        
        where[2] = numhit
        if numhit > 1:
            a = [where[0],where[1]]
            self.deadlist.append(a)
            gBattleRep.TangoShotDead += 1
            gBattleRep.report()
            return True  #to have sound and register as dead
        else:
            return False
        
    def Draw(self):
        for i in self.boardlist:
            self.target.set_position(i[0],i[1])
            self.target.draw()
        for d in self.deadlist:
            self.deadtarget.set_position(d[0],d[1])
            self.deadtarget.draw()

#class TargetBoard0():
    #def __init__(self,x,y):
        #self.target = SpriteLoad(Const.folder+'target.jpg')
        #self.target.scale = 0.25
        #self.target.set_position(x,y)
        ##self.target.rotation = -90.0
        ##self.hitlist = []
        #print 'init Target'
        #print self.target.width, self.target.height
    #def move(self,w,h):
        ##print 'move',self.target.x,w,h
        #d = GetDirection()
        #tw = self.target.width
        #th = self.target.height
        #x = self.target.x
        #y = self.target.y
        #self.target.x,self.target.y = MoveXY(d, x,y,tw, th, w, h)
        #pass
    #def Hit(self,x,y):
        #tx = self.target.x
        #ty = self.target.y
        #l = tx
        #t = ty + self.target.height/4*3
        #r = tx + self.target.width
        #b = ty + self.target.height
        #recthead = [l, t, r, b]
        
        #l = tx
        #t = ty + self.target.height/4
        #r = tx + self.target.width
        #b = ty + self.target.height/4*3
        #rectbody = [l, t, r, b]
        
        #l = tx
        #t = ty 
        #r = tx + self.target.width
        #b = ty + self.target.height/4
        #rectlegs = [l, t, r, b]
        
        #if withinrect( x, y, recthead):
            #print 'head hit'
            #return True
        #elif withinrect( x, y, rectbody):
            #print 'body hit'
            ##self.sound.Play(self.sound.pain)
            #return True
        #elif withinrect( x, y, rectlegs):
            #print 'leg hit'
            ##self.sound.Play(self.sound.pain)
            #return True
        #else:
            ##print 'miss'
            #return False
        
    #def Draw(self):
        #self.target.draw()


'''
appear near hero
dot moves randomly
dot moves toward hero
tries to hit hero

number
skill
speed
location of hero
add attacks
timed attacks, then end each
check hit
RPG

sound of hero hit
/graphic


'''
class AttackHero():
    def __init__(self):
        self.attackL = []
        clock.schedule_interval(self.autocall, 0.05)
        self.attackSpr = SpriteLoad(Const.folder+'attackDot.png',centre=True)
        self.attackSpr.scale = 0.5
        self.hero = None
        self.sound = gSound
        self.badguys = []
        self.pauseBool = False
        pass
    def autocall(self,dt):
        #after some time, remove the bullet
        #for i in self.attackL:
            #t = i[2]
            #t -= 1
            #if t < 1:
                #self.attackL.remove(i)
            #else:
                #i[2] = t
        if self.pauseBool: return
        
        self.move()        
        pass
    def addHero(self, hero):
        self.hero = hero
    def addBadGuys(self, badguys):
        self.badguys = badguys
        pass
    def draw(self):
        for i in self.attackL:
            x = i[0]
            y = i[1]
            self.attackSpr.set_position(x, y)
            self.attackSpr.draw()
    def add(self,hero):
        '''position,time'''
        random.shuffle(self.badguys)
        maxb = 2 # means 3 bullets
        if len(self.attackL) > maxb: return #not too many bullets!
        i = 0
        while i < len(self.badguys):
            #h = random.randrange(100,200)
            #w = random.randrange(-500,500)
            #for i in self.badguys:
            bp = self.badguys[i]
            hx = hero.heroSprite.x
            hy = hero.heroSprite.y
            x = bp[0]
            y = bp[1]
            a = [x,y,hx,hy]
            self.attackL.append(a)
            i += 1
            if i > maxb: break
        
        pass
    def move(self):
        s = self.attackSpr.height * 2
        for i in self.attackL:
            x = i[0]
            y = i[1]
            hx = i[2]
            hy = i[3]
            if hx < x:
                x -= s
            elif hx > x:
                x += s
            if hy < y:
                y -= s
            elif hy > y:
                y += s
            if abs(x-hx)<s and abs(y-hy)<s:
                self.attackL.remove(i)
            #y -= self.attackSpr.height
            i[0] = x
            i[1] = y
            if self.Hit(x, y): break
        pass
    def Hit(self,x,y):
        #tx = self.coverSpr.x
        #ty = self.coverSpr.y
        tx = self.hero.heroSprite.x
        ty = self.hero.heroSprite.y
        tx -= self.hero.heroSprite.width / 2  # back from the centre
        ty -= self.hero.heroSprite.height / 2
        l = tx
        t = ty 
        r = tx + self.hero.heroSprite.width
        b = ty + self.hero.heroSprite.height
        rect = [l, t, r, b]
        if withinrect( x, y, rect):
            self.sound.Play(self.sound.heropain)
            self.hero.hit()
            gBattleRep.herohit += 1
            gBattleRep.report()
            return True
        return False
    def pause(self):
        self.pauseBool = not self.pauseBool


class ScreenTime():
    def __init__(self,countup=True,inittime=0):
        self.seconds = inittime
        self.countup = countup
        self.status = pyglet.text.Label('Time Reading',
                                        font_name='Times New Roman',
                                        font_size=24,
                                        x=800, y = 20)
        clock.schedule_interval(self.autocall, 1.0)
        self.mode = 'stop'
    def autocall(self,dt):  
        if self.mode == 'start':
            if self.countup:
                self.seconds += 1
            elif not self.countup:
                self.seconds -= 1
            
        pass
    def start(self):
        self.mode = 'start'
        pass
    def stop(self):
        self.mode = 'stop'
        pass
    def reset(self):
        self.seconds = 0
    def draw(self):
        self.status.text = str(self.seconds)
        self.status.draw()
        pass
    


'''

to allow the number keys to be programmed with different weapons
as to the mission at hand.

'''
class EquipmentKeys():
    def __init__(self):
        self.keydata = []
        i = 0
        for i in range(10):
            self.keydata.append(Const.HandToolConst)
        pass
    def changekey(self,key,equipment):
        assert(key > -1 and key < 10)
        self.keydata[key] = equipment
    def get(self,key):
        assert(key > -1 and key < 10)
        return self.keydata[key]
    def reset(self):
        self.__init__()
    
    
    
'''
Place where stuff that can be shot at are placed.
Tango
Hostages
Cover
can be distant and nearby
distant for sniper
How to account for the shot?
Scoring?


'''
class ShootingGallery():
    def __init__(self):
        # prevent the tangos get faster and faster
        self.runauto = 0 # ensure autocall run once only?
        self.gamestage = 0 # to allow staging of different scenarios
        self.stageDepth = 0 # deeper missions
        self.attHero = AttackHero()
        self.CBattHero = AttackHero()
        self.CBattHero2 = AttackHero()
        self.pauseBool = False
        self.timers = ScreenTime(countup=True,inittime=0)
        self.wayp = Waypoints()
        self.NuclearPowerStationDefence = 5
        self.MansionAssassinationMission = 6
        
    def initAttack(self,hero):
        self.herotarget = hero
        self.herotarget.setscreen(self.winWidth,self.winHeight)
        self.running = False
        self.attHero.addHero(hero)
        self.CBattHero.addHero(hero)
        self.CBattHero2.addHero(hero)
        self.explodeObj = Explosion()
        pass
    def setWinSize(self,w,h):
        self.winHeight = h
        self.winWidth = w
    def key9(self,which):
        return self.equipment.get(which)
        #pass
    def depthChange(self):
        if self.gamestage == 1 and self.stageDepth == 1:
            self.background = \
                pyglet.image.load(Const.backgroundFolder+\
                                  'aircraftcabin.jpg')
            self.sound.Play(self.sound.m32MGL) #breach sound
            self.equipment.reset()
            self.equipment.changekey(1, Const.knifeKbar)
            self.equipment.changekey(2, Const.MP7silent)
            self.equipment.changekey(3, Const.STCPW)
            self.equipment.changekey(4, Const.GLOCK)
            self.equipment.changekey(5, Const.pistol1911)
            self.equipment.changekey(6, Const.MP5)
 
            self.timers.reset()
            self.timers.start()
            i = 9
            self.TargetObj.create(i, self.winWidth, self.winHeight,'real')
            self.CommandoBaddies.create(1, self.winWidth, self.winHeight)
            self.attHero.addBadGuys(self.TargetObj.getList())    
            self.CBattHero.addBadGuys(self.CommandoBaddies.getList())  
            self.hostages = Hostages()
            self.hostages.create(30,self.winWidth,self.winHeight)
            self.hostages.setPanic(False)
            self.stageDepth = 0
        pass
    
    def init(self):
        self.sound = gSound
        #self.boardlist = []
        self.TargetObj = TargetBoard()
        self.CommandoBaddies = TangoCommando()
        self.coverlist = []
        self.equipment = EquipmentKeys()
        if self.gamestage == 0:
            i = 0
            self.equipment.reset()
            self.equipment.changekey(1, Const.M32GRENADElauncher)
            self.equipment.changekey(2, Const.pistol1911)
            self.equipment.changekey(3, Const.STCPW)
            self.equipment.changekey(4, Const.GLOCK)
            self.equipment.changekey(5, Const.MP5)
            self.equipment.changekey(6, Const.M107sniper)
            self.equipment.changekey(7, Const.MP7silent)
            self.equipment.changekey(8, Const.ClaymoreMine)
            self.equipment.changekey(9, Const.AK47)
            
            
            
            self.hostages = Hostages()
            self.hostages.create(0,self.winWidth,self.winHeight)
            self.background = \
                pyglet.image.load(Const.backgroundFolder+\
                                  'rifle_range.jpg')
            self.TargetObj.create(10, self.winWidth, self.winHeight,'dummy')
            
            #self.gamestage = 4  #quick jump during testing

        elif self.gamestage == 1:
            gBattleRep.init() #reset stats            
            self.equipment.reset()
            self.equipment.changekey(1, Const.knifeKbar)
            self.equipment.changekey(2, Const.MP7silent)
            self.equipment.changekey(3, Const.STCPW)
            self.equipment.changekey(4, Const.GLOCK)
            self.equipment.changekey(5, Const.pistol1911)
            #self.equipment.changekey(5, Const.M249SAW)
            
            self.wayp.add(460, 160)
            self.wayp.add(560, 160)
            self.wayp.add(660, 160)
            self.background = \
                pyglet.image.load(Const.backgroundFolder+\
                                  'tarmac.jpg')
                                  #'aircraftcabin.jpg')
            
            #while i > 0: #tangos
                #x = random.randrange(1,self.winWidth)
                #y = random.randrange(500,self.winHeight)
                #a = [x,y]
                #self.boardlist.append(a)
                #i-=1
        elif self.gamestage == 2:

            self.equipment.reset()
            self.equipment.changekey(1, Const.knifeKbar)
            self.equipment.changekey(2, Const.STCPW)
            self.equipment.changekey(3, Const.M4assaultRifle)
            self.equipment.changekey(4, Const.SAR21Rifle)
            self.equipment.changekey(5, Const.Ultimax100SAW)
            self.equipment.changekey(6, Const.M32GRENADElauncher)
            self.equipment.changekey(7, Const.M249SAW)
            self.equipment.changekey(8, Const.ClaymoreMine)
            
            self.background = \
                pyglet.image.load(Const.backgroundFolder+\
                    'Afghan_village_destroyed_by_the_Soviets.jpg')
            self.hostages = Hostages()
            self.hostages.create(0,self.winWidth,self.winHeight)
            self.hostages.setPanic(False)
            i = 100
            self.TargetObj.create(i, self.winWidth, self.winHeight,'real')
            #while i > 0: #tangos
                #x = random.randrange(1,self.winWidth)
                #y = random.randrange(500,self.winHeight)
                #a = [x,y]
                #self.boardlist.append(a)
                #i-=1
            
            self.attHero.addBadGuys(self.TargetObj.getList())    
            
            
        elif self.gamestage == 3:
            
            self.timers.reset()
            self.timers.start()
            self.equipment.reset()
            self.equipment.changekey(1, Const.knifeKbar)
            self.equipment.changekey(2, Const.STCPW)
            self.equipment.changekey(3, Const.M4assaultRifle)
            self.equipment.changekey(4, Const.SAR21Rifle)
            self.equipment.changekey(5, Const.MP7silent)
            self.equipment.changekey(6, Const.M32GRENADElauncher)
            self.equipment.changekey(7, Const.M134MiniGun)
            self.equipment.changekey(8, Const.M107sniper)
            self.equipment.changekey(9, Const.MP5)
            
            self.hostages = Hostages()
            self.hostages.create(30,self.winWidth,self.winHeight)
            self.hostages.setPanic(True)
            i = 10
            self.TargetObj.create(i, self.winWidth, self.winHeight,'real')
            #while i > 0: #tangos
                #x = random.randrange(1,self.winWidth)
                #y = random.randrange(500,self.winHeight)
                #a = [x,y]
                #self.boardlist.append(a)
                #i-=1
            
            self.attHero.addBadGuys(self.TargetObj.getList())    
            i = 20
            self.coverlist = []
            self.coverObj = CoverLayer()
            while i > 0: #cover
                x = random.randrange(1,self.winWidth)
                y = random.randrange(1,self.winHeight+300)
                #y = 200
                cov = (x,y)
                self.coverlist.append(cov)
                i-=1
            
            
        elif self.gamestage == 4:
            self.sound.Play(self.sound.hostageHitsound)
            
            self.equipment.reset()
            self.equipment.changekey(1, Const.pistol1911)
            self.equipment.changekey(2, Const.GLOCK)
            self.equipment.changekey(3, Const.STCPW)
            self.equipment.changekey(4, Const.MP5)
            self.equipment.changekey(5, Const.MP7silent)
            self.equipment.changekey(6, Const.M107sniper)           
            self.timers.reset()
            self.timers.start()
            self.background = \
                pyglet.image.load(Const.backgroundFolder+\
                'Kuala-Lumpur-Federal-Hotel-Street-Front.jpg')
            
            i = 10
            self.CommandoBaddies.create(i, self.winWidth, self.winHeight)
            #while i > 0: #tangos
                #x = random.randrange(1,self.winWidth)
                #y = random.randrange(500,self.winHeight)
                #a = [x,y]
                #self.boardlist.append(a)
                #i-=1
            self.CBattHero.addBadGuys(self.CommandoBaddies.getList())  
            
            self.hostages = Hostages()
            self.hostages.create(40,self.winWidth,self.winHeight)
            self.hostages.setPanic(True)
        elif self.gamestage == self.NuclearPowerStationDefence:
            
            self.equipment.reset()
            self.equipment.changekey(1, Const.knifeKbar)
            self.equipment.changekey(2, Const.GLOCK)
            self.equipment.changekey(3, Const.STCPW)
            self.equipment.changekey(4, Const.MP5)
            self.equipment.changekey(5, Const.M249SAW)
            self.equipment.changekey(6, Const.M134MiniGun)
            self.equipment.changekey(7, Const.M107sniper)
            self.equipment.changekey(8, Const.ClaymoreMine)
            self.equipment.changekey(9, Const.M32GRENADElauncher)          
            self.timers.reset()
            self.timers.start()
            self.background = \
                pyglet.image.load(Const.backgroundFolder+\
                'Nuclear.power.plant.Dukovany.jpg')
            
            i = 50
            self.CommandoBaddies.create(i, self.winWidth, self.winHeight)
            self.CBattHero.addBadGuys(self.CommandoBaddies.getList())  
            self.CBattHero2.addBadGuys(self.CommandoBaddies.getList())  
            self.hostages = Hostages()
            self.hostages.create(0,self.winWidth,self.winHeight)
            self.nextstage = 1 #another stage within this stage
        elif self.gamestage == self.MansionAssassinationMission:
            #assassination 
            self.equipment.reset()
            self.equipment.changekey(1, Const.knifeKbar)
            self.equipment.changekey(2, Const.pistol1911)
            self.equipment.changekey(3, Const.GLOCK)   
            self.equipment.changekey(4, Const.M107sniper)
            self.equipment.changekey(5, Const.MP5)
            self.equipment.changekey(6, Const.AK47)
            self.equipment.changekey(7, Const.MP7silent)
            self.equipment.changekey(8, Const.M249SAW)
            i = 1 #ONE GUARD to start the mission
            self.TargetObj.create(i, self.winWidth, self.winHeight,'real')   
            self.background = \
                 pyglet.image.load(Const.backgroundFolder+\
                                   'mansion.jpg')
            self.nextstage = 1 #another stage within this stage
            
            
            
        elif self.gamestage == 7:    
            #dining hall attack
            self.equipment.reset()
            self.equipment.changekey(1, Const.knifeKbar)
            self.equipment.changekey(2, Const.pistol1911)
            self.equipment.changekey(3, Const.GLOCK)  
            
            self.timers.reset()
            self.timers.start()

 
            self.hostages = Hostages()
            self.hostages.create(0,self.winWidth,self.winHeight)
            self.background = \
                 pyglet.image.load(Const.backgroundFolder+\
                                   'ptc-dining-hall.jpg')
            i = 4
            self.CommandoBaddies.create(i, self.winWidth, self.winHeight)
            self.CBattHero.addBadGuys(self.CommandoBaddies.getList())  
            self.CBattHero2.addBadGuys(self.CommandoBaddies.getList())  
            
            
            
            
        elif self.gamestage == 8:    

            
            self.equipment.reset()
            self.equipment.changekey(1, Const.M4assaultRifle)
            self.equipment.changekey(2, Const.MP5)
            self.equipment.changekey(3, Const.pistol1911)
            self.equipment.changekey(4, Const.Ultimax100SAW)
            self.hostages = Hostages()
            self.hostages.create(0,self.winWidth,self.winHeight)
            self.background = \
                 pyglet.image.load(Const.backgroundFolder+\
                                   'Arlington-National-Cemetery-during-Spring.jpg')
            i = 10
            self.TargetObj.create(i, self.winWidth, self.winHeight,'real')   
            self.attHero.addBadGuys(self.TargetObj.getList())  
                        
            pass
        elif self.gamestage == 9:
            self.hostages = Hostages()
            self.hostages.create(0,self.winWidth,self.winHeight)
            self.gamestage = -1
            self.timers.stop()
            self.timers.reset()
            gBattleRep.init() #reset stats
            gBattleRep.report()
            self.herotarget.resetPos()
        
        
        
        #gfwindow = pyglet.window.Window(style=pyglet.window.Window.WINDOW_STYLE_DIALOG)    
        #i = 0
        #self.coverlist = []
        #self.coverObj = CoverLayer()
        #while i > 0:
            #x = random.randrange(1,self.winWidth)
            #y = random.randrange(1,self.winHeight+300)
            ##y = 200
            #cov = (x,y)
            #self.coverlist.append(cov)
            #i-=1
            
        if self.runauto == 0: #run once
            clock.schedule_interval(self.autocall, 0.25)
            #self.background = pyglet.image.load(Const.backgroundFolder+'Afghan_village_destroyed_by_the_Soviets.jpg')
            self.runauto = 1
            
    def autocall(self,dt):
        if self.pauseBool: return
        i = 0
        #m = len(self.boardlist)-1
        
        
        if not self.TargetObj.tangoDead():
            self.attHero.add(self.herotarget) #keep attacking hero
        
        if not self.CommandoBaddies.tangoDead():    
            self.CBattHero.add(self.herotarget)    
            self.CBattHero2.add(self.herotarget) 
        
        self.TargetObj.move(self.winWidth,self.winHeight)
        self.CommandoBaddies.move(self.winWidth,self.winHeight)
        
        self.wayp.checkhit(self.herotarget.heroSprite.x,self.herotarget.heroSprite.y)
        
        if self.gamestage == 1 and self.wayp.complete():
            print 'complete'
            self.wayp.reset()
            self.stageDepth += 1
            self.depthChange()
        
        #if m >= 0:
            #self.attHero.add(self.herotarget) 
            #pass
        #while m > -1:
            #a = self.boardlist[m][0]
            #b = self.boardlist[m][1]
            #x,y = self.TargetObj.move(self.winWidth,self.winHeight,a,b)
            #if Const.suicideBomber and self.SuicideBomberHit(x,y):
                #print 'xxx bomber'
                #gBattleRep.heroblasted += 1
                #gBattleRep.report()
                #self.boardlist.remove(self.boardlist[m])
            #else:
                #self.boardlist[m][0] = x
                #self.boardlist[m][1] = y
            
            #m-=1
        #pass
    
    def Rescue(self,x,y):
        self.hostages.Rescue(x, y)
        
    def Hit(self,x,y,name):
        '''
        000
        000
        000
        '''
        def SniperEnhance(ix,iy):
            g = 10
            off = ((-g,-g),(-g,0),(-g,+g),(0,-g),(+g,+g),(+g,0),(+g,-g),(0,+g))
            
            for i in off:
                x = ix + i[0]
                y = iy + i[1]
                for p in xrange(0,5):
                    self.CommandoBaddies.TangoShotcheck(x,y)
                    self.TargetObj.TangoShotcheck(x,y)
            
            pass
            
        retz = False
        
        self.hostages.hit(x,y)
        
        if name != Const.M107sniper and \
           name != Const.M134MiniGun: #can go through walls if powerful weapon
            for c in self.coverlist:
                if self.coverObj.Hit(c,x,y):
                    retz= True
                    break
        if retz:
            return
        
        
        
        if name == Const.M107sniper: # \
           #name == Const.MP7silent: # or \
            SniperEnhance(x,y)
        elif name in [Const.M134MiniGun,Const.pistol1911]: #one shot equals 5 shots 
            for i in xrange(0, 5):
                self.CommandoBaddies.TangoShotcheck(x,y)
                self.TargetObj.TangoShotcheck(x,y)
        else:
            self.TargetObj.TangoShotcheck(x,y)
            self.CommandoBaddies.TangoShotcheck(x,y)
            
            
                
        if self.TargetObj.tangoDead() and \
           self.CommandoBaddies.tangoDead():
            self.timers.stop()
            if self.gamestage == 0:
                self.init() #set up target boards again
            elif self.gamestage == self.MansionAssassinationMission:  #assassination stage
                if self.nextstage == 4:
                    i = 3 #leaders without weapons
                    self.CommandoBaddies.create(i, self.winWidth, self.winHeight)
                    self.timers.start()
                    self.nextstage += 1
                elif self.nextstage < 4:
                    i = 10
                    self.TargetObj.create(i, self.winWidth, self.winHeight,'real')   
                    self.attHero.addBadGuys(self.TargetObj.getList())  
                    self.attHero.addBadGuys(self.TargetObj.getList())     
                    self.nextstage += 1
                #elif self.nextstage == 1:
                    #i = 10
                    #self.TargetObj.create(i, self.winWidth, self.winHeight,'real')   
                    #self.attHero.addBadGuys(self.TargetObj.getList())  
                    #self.attHero.addBadGuys(self.TargetObj.getList())     
                    #self.nextstage += 1
            elif self.gamestage == self.NuclearPowerStationDefence:
                if self.nextstage < 6:
                    i = 50
                    self.CommandoBaddies.create(i, self.winWidth, self.winHeight)
                    self.CBattHero.addBadGuys(self.CommandoBaddies.getList())  
                    self.CBattHero2.addBadGuys(self.CommandoBaddies.getList())  
                    self.nextstage += 1
                    
    
        #for i in self.boardlist:
            #if self.TargetObj.Hit(x,y,i):
                ##print 'hit hit'
                #self.sound.Play(self.sound.pain)
                #self.boardlist.remove(i)
                #break
            
        #if self.boardlist == []: #tangos dead
            #self.timers.stop()
            
    def SuicideBomberHit(self,x,y):
        br = 100
        gl = x - br
        gt = y - br
        gr = x + br
        gb = y + br
        grect = [gl,gt,gr,gb]
        hx = self.herotarget.heroSprite.x
        hy = self.herotarget.heroSprite.y
        if withinrect(hx,hy,grect):
            self.explodeObj.add(x, y)
            self.herotarget.hit()
            self.sound.Play(self.sound.m32MGL)
            return True
        else:
            return False
        
    def HitGrenade2(self,x,y):
            #print 'grenade'
            self.explodeObj.add(x, y)
            w = 100
            h = 100
            g = 5
            sx = x - w
            sy = y - h
            ex = x + w
            ey = y + h
            bx = sx
            by = sy
            p = 0
            while True:
                p += 1
                #bx = random.randrange(1,self.winWidth)
                #by = random.randrange(1,self.winHeight)
                self.Hit(bx, by, Const.M32GRENADElauncher)
                bx += g
                if bx > ex:
                    bx = sx
                    by += g
                if by > ey:
                    break
            print 'pellets', p    
            
    #def HitGrenade(self,x,y):
        #br = 200 #blast radius
        #self.explodeObj.add(x, y)
        #gl = x - br
        #gt = y - br
        #gr = x + br
        #gb = y + br
        #grect = [gl,gt,gr,gb]
        #tangos = self.TargetObj.getList()
        #dead = self.TargetObj.getDeadlist()
        #for i in tangos:
            #if withinrect(i[0],i[1],grect):
                #self.sound.Play(self.sound.pain)
                #tangos.remove(i)
                #dead.append([i[0],i[1]])
                #gBattleRep.numberblasted += 1
                #gBattleRep.report()
                
        #self.hostages.HitGrenade(grect)
        
        #if self.TargetObj.tangoDead(): #tangos dead
            #self.timers.stop()
                
    def Claymore(self,x,y):
        #print 'claymore'
        self.explodeObj.add(x, y)
        w = 250
        h = 300
        g = 20
        sx = x - w
        sy = y - h
        ex = x + w
        ey = y + h
        bx = sx
        by = sy
        p = 0
        while True:
            p += 1
            #bx = random.randrange(1,self.winWidth)
            #by = random.randrange(1,self.winHeight)
            self.Hit(bx, by, Const.ClaymoreMine)
            bx += g
            if bx > ex:
                bx = sx
                by += g
            if by > ey:
                break
        print 'pellets', p
    
    def Draw(self):
        # the 60 gives a status bar for free
        self.background.blit(0,60,width=self.winWidth,height=self.winHeight)
        #self.background.draw()  #cannot do this way - cannot set width/height
        self.explodeObj.draw()
        #for i in self.boardlist:
            #self.TargetObj.Draw(i)
        self.TargetObj.Draw()
        self.CommandoBaddies.Draw()
        
        for i in self.coverlist:
            self.coverObj.Draw(i)
            
        self.hostages.draw()
        self.attHero.draw()
        self.CBattHero.draw()
        self.timers.draw()
        self.wayp.draw()
        #self.hero.draw()   
    def pause(self):
        self.pauseBool = not self.pauseBool
        self.attHero.pause()
        self.CBattHero.pause()
        #print 'pause',self.pauseBool
    def runToggle(self):
        self.running = not self.running
        if self.running:
            self.herotarget.setRunning(True)
        else:
            self.herotarget.setRunning(False)
        
#class ShootingGallery():



         
#gTargetBoard = TargetBoard()
gShootGallery = ShootingGallery()
gBulletHoles = BulletHoles()

class Knife():
    def __init__(self,name):
        self.name = name
        print 'knife init'
        self.mode = Const.knifeSafe
        self.data = Const.folder
        weapondata = self.Database(name)
        self.drawing = SpriteLoad(self.data+weapondata[0])
        self.drawing.scale = weapondata[1]
        self.sound = gSound
        #self.bulleth = bulletholes
        self.mousex = 0
        self.mousey = 0
        self.magazine = weapondata[2]
        self.ammo = self.magazine
        self.reloadweapon = False
        self.status = pyglet.text.Label('Hello, world',
                                        font_name='Times New Roman',
                                        font_size=24,
                                        x=220, y = 20)
        self.SetText()
        self.reticle = weapondata[3]
    def SetText(self):
        self.report = self.name + ' ' + self.mode + ' ' + str(self.ammo)
        self.status.text = self.report
    def Database(self,name):
        #filename,scale,magazine capacity,
        if name == Const.knifeKbar:
            return 'kbar knife side 1217_h_lg.png', \
            0.25,1,'kbar knife side 1217_h_lgup.png'
        else:
            raise Exception("knife Weapon not exist!")
    
    def mouse(self,x,y):
        print self.name,x,y
        pass
    def mouseup(self,x,y):
        pass
    def mousedrag(self,x,y):
        #knife has drag    
        pass
    
    def mousepos(self,x,y):  #knife
        #print 'mouse',x,y
        if self.mode == Const.knifeArmed:
            gShootGallery.Hit(x, y,Const.knifeKbar)
    def select(self):
        self.mode = HandleModeSelect(Const.knifeModes, self.mode)
        self.SetText()
        
    def draw(self):
        self.drawing.draw()
        self.status.draw()
        pass
    def Reload(self):
        pass
    def SetSights(self,win): #knife
        image = pyglet.image.load(Const.folder+self.reticle)
        x = image.height / 2
        y = image.width / 2
        cursor = pyglet.window.ImageMouseCursor(image, x, y)
        win.set_mouse_cursor( cursor)
        pass
    
class HandTool():
    def __init__(self,name):
        self.name = name
        self.data = Const.folder
        print 'hand tool init'
        self.reticle = 'Cursor hand white.png'
        self.handName = 'Cursor hand whiteB.png'
        self.drawing = SpriteLoad(self.data+self.handName)
        self.drawing.set_position(20, 0)
        self.status = pyglet.text.Label('Hello, world',
                                        font_name='Times New Roman',
                                        font_size=24,
                                        x=220, y = 20)
        self.SetText()
    def SetText(self):
        self.report = 'This hand tool can rescue hostages'
        self.status.text = self.report
    def Database(self,name):
        #filename,scale,magazine capacity,
        if name == Const.knifeKbar:
            return 'kbar knife side 1217_h_lg.png', \
            0.25,1,'kbar knife side 1217_h_lgup.png'
        else:
            raise Exception("hand wanker not exist!")
    
    def mouse(self,x,y):
        print self.name,x,y
        if x < 100:
            gShootGallery.init()
        else:
            gShootGallery.gamestage += 1
            gShootGallery.init()
        pass
    def mouseup(self,x,y):
        #gShootGallery.Rescue(x, y)
        pass
    def mousedrag(self,x,y):
        #hand has drag    
        pass
    
    def mousepos(self,x,y):  #knife
        #print 'mouse',x,y
        gShootGallery.Rescue(x, y)
        pass
    def select(self):
        pass
    def draw(self):
        self.drawing.draw()
        self.status.draw()
        pass
    def Reload(self):
        pass
    def SetSights(self,win):
        image = pyglet.image.load(Const.folder+self.reticle)
        cursor = pyglet.window.ImageMouseCursor(image, 25, 25)
        win.set_mouse_cursor( cursor)
        pass

#class Pistol():    
    #def __init__(self,
                 #name,
                 ##sound,
                 ##bulletholes,
                 #):
        #self.name = name
        #print 'pistol init'
        #self.mode = Const.pistolSafe
        #self.data = Const.folder
        #weapondata = self.Database(name)
        #self.drawing = SpriteLoad(self.data+weapondata[0])
        #self.drawing.scale = weapondata[1]
        #self.sound = gSound
        #self.bulleth = gBulletHoles
        #self.mousex = 0
        #self.mousey = 0
        #self.magazine = weapondata[2]
        #self.ammo = self.magazine
        #self.reloadweapon = False
        #self.status = pyglet.text.Label('Hello, world',
                                        #font_name='Times New Roman',
                                        #font_size=24,
                                        #x=220, y = 20)
        #self.SetText()
        #self.reticle = weapondata[3]
        
        #pass
    #def Database(self,name):
        ##filename,scale,magazine capacity,
        #if name == Const.pistol1911:
            #return 'm1911pistol.jpg',0.25,15,'reticlePistol1911.png'
        #else:
            #raise Exception("pistol Weapon not exist!")
    #def reloadCall(self,dt):
        #if self.reloadweapon:
            #self.reloadtime -= 1
            #if self.reloadtime < 1:
                #self.ammo = self.magazine
                #self.SetText()
                #clock.unschedule(self.reloadCall)
                #self.reloadweapon = False
    
    #def mouse(self,x,y):
        #if self.mode != Const.pistolSafe:
            #self.trigger = True
            #self.mousex = x
            #self.mousey = y
            #self.Fire()
    #def mouseup(self,x,y):
        #self.trigger = False
    #def mousedrag(self,x,y):
        ##pistol got no drag    
        #pass
    #def Fire(self):
        #if self.ammo > 0:
            ##self.sound.Play(self.sound.sar21)
            #self.sound.Play(self.sound.m1911)
            #x = self.mousex
            #y = self.mousey
            #self.bulleth.record(x,y)
            #self.ammo -= 1
            #self.SetText()
            ##gTargetBoard.Hit(x, y)
            #gShootGallery.Hit(x, y)
    #def SetText(self):
        #self.report = self.name + ' ' + self.mode + ' ' + str(self.ammo)
        #self.status.text = self.report
    #def select(self):
        ##print 'pistol mode'
        #self.mode = HandleModeSelect(Const.pistolModes, self.mode)
        ##print self.mode
        #self.SetText()
        ##print self.mode

    #def draw(self):
        #self.drawing.draw()
        #self.bulleth.draw()
        #self.status.draw()
        #pass
    #def Reload(self):
        #self.sound.Player(self.sound.reLoad)
        #self.reloadweapon = True
        #self.reloadtime = 3
        #clock.schedule_interval(self.reloadCall, 1.0)
    #def SetSights(self,win):
        #image = pyglet.image.load(Const.folder+self.reticle)
        #cursor = pyglet.window.ImageMouseCursor(image, 25, 25)
        #win.set_mouse_cursor( cursor)
        #pass
        
class AssaultRifle():    
    def __init__(self,
                 name,
                 numberMagazines,
                 #bulletholes,
                 ):
        self.name = name
        print 'AssaultRifle init'
        self.mode = Const.assaultRifleSafe
        self.rateFire = 1.0
        self.trigger = False
        self.auto = False
        self.data = Const.folder
        self.sound = gSound
        self.weaponsound = None
        self.availableModes = None
        weapondata = self.Database(name)
        self.drawing = SpriteLoad(self.data+weapondata[0])
        self.drawing.scale = weapondata[1]
        self.bulleth = gBulletHoles
        self.mousex = 0
        self.mousey = 0
        self.magazine = weapondata[2]
        self.ammo = self.magazine
        self.reloadweapon = False
        self.magazines = numberMagazines
        self.status = pyglet.text.Label('Hello, world',
                                        font_name='Times New Roman',
                                        font_size=24,
                                        x=220, y = 20)
        self.SetText()
        self.reticle = weapondata[3]
        self.availableModes = weapondata[4]
        self.rateFire = weapondata[5]
        pass
    
    def Database(self,name):
        #filename,scale,magazine capacity,reticle,modes,rateOfFire
        if name == Const.M4assaultRifle:
            self.weaponsound = self.sound.m4carbine
            return 'm4_1.jpg',0.25,30,'reticleM4.png',\
                   Const.assaultRifleModes,0.1
        elif name == Const.SAR21Rifle:
            self.weaponsound = self.sound.sar21
            return 'sar21_1.jpg',0.3,30,'reticle.png',\
                   Const.assaultRifleModes,0.1
        elif name == Const.Ultimax100SAW:
            self.weaponsound = self.sound.sar21
            return 'ultimax_mk3_3.jpg',0.2,100,'reticle.png',\
                   Const.machineGunModes,0.1
        elif name == Const.M134MiniGun:
            self.weaponsound = self.sound.minigunSound #4400
            return 'minigun800px-DAM134DT.png',0.2,500,\
                   'reticleM4.png',Const.machineGunModes,0.01
        elif name == Const.pistol1911:
            self.weaponsound = self.sound.m1911
            return 'm1911pistol.jpg',0.25,7,\
                   'reticlePistol1911.png',Const.pistolModes,1.0
        elif name == Const.M32GRENADElauncher:
            self.weaponsound = self.sound.m32MGL
            return 'M32MGL.png',0.3,6,\
                   'M32_Iron_Sights_MW3DS.png',Const.pistolModes,1.0
        elif name == Const.STCPW:
            self.weaponsound = self.sound.stcpwsnd 
            return 'ST_Kinetics_CPW_Submachine_Gun_(SMG)_1.jpg',0.15,30,\
                   'reticle.png',Const.assaultRifleModes,0.1
        elif name == Const.GLOCK:
            self.weaponsound = self.sound.glocksnd
            return 'glockhqdefault.jpg',0.25,33,\
                   'reticlePistol1911.png',Const.assaultRifleModes,0.1
        elif name == Const.M249SAW:
            self.weaponsound = self.sound.m249sawSound
            return '800px-PEO_M249_Para_ACOG.jpg',0.25,200,\
                   'reticleM4.png',Const.machineGunModes,0.1
        elif name == Const.M107sniper:
            self.weaponsound = self.sound.m107Sound
            return 'M107Cq.jpg',0.5,10,\
                   'M107largeSights.png',Const.pistolModes,1.0
        elif name == Const.ClaymoreMine:
            self.weaponsound = self.sound.m18Sound
            return 'Claymore2.jpg',0.3,5,\
                   'Claymore2aimer.png',Const.pistolModes,1.0
        elif name == Const.MP5:
            self.weaponsound = self.sound.mp5sound
            return 'mp5a3.jpg',0.3,30,\
                   'mp5sights.png',Const.assaultRifleModes,0.05
        elif name == Const.AK47:
            self.weaponsound = self.sound.AK47sound
            return 'AK-47_type_II_Part_DM-ST-89-01131.jpg',0.6,30,\
                   'reticleM4.png',Const.assaultRifleModes,0.1
        elif name == Const.MP7silent:
            self.weaponsound = self.sound.mp7sound
            return 'MP7_2.5701_1web.jpg',0.2,30,\
                   'reticle.png',Const.assaultRifleModes,0.1
        else:
            raise Exception("Weapon not exist!")
        
    def SetText(self):
        self.report = self.name + ' ' + self.mode + ' ' + str(self.ammo) + ' ' + str(self.magazines)
        self.status.text = self.report
        
    def Fire(self):
        if self.ammo > 0:
            self.sound.Play(self.weaponsound)
            x = self.mousex
            y = self.mousey
            self.bulleth.record(x,y)
            self.ammo -= 1
            self.SetText()
            if self.name == Const.M32GRENADElauncher:
                gShootGallery.HitGrenade2(x, y)
            elif self.name == Const.ClaymoreMine:
                gShootGallery.Claymore(x, y)
            elif self.name != Const.M32GRENADElauncher:
                gShootGallery.Hit(x, y,self.name)
            
    def draw(self):
        self.drawing.draw()
        self.bulleth.draw()
        self.status.draw()
    def autocall(self,dt):
        if self.trigger:
            #print 'autofire'
            self.Fire()
    def reloadCall(self,dt):
        
        if self.reloadweapon:
            self.reloadtime -= 1
            if self.reloadtime < 1 and self.magazines > 0:
                self.magazines -= 1
                self.ammo = self.magazine
                self.SetText()
                self.reloadweapon = False
                self.sound.Stop()
                clock.unschedule(self.reloadCall)
                
    def mouse(self,x,y):
        #print self.name,x,y
        if self.mode != Const.assaultRifleSafe:
            self.trigger = True
            self.mousex = x
            self.mousey = y
            self.Fire()
            pass
    def mousepos(self,x,y):
        pass
    
    def mouseup(self,x,y):
        self.trigger = False
    def mousedrag(self,x,y):
        if self.mode == Const.assaultRifleAuto:
            #self.mouse(x, y)
            self.mousex = x
            self.mousey = y
            
            pass
    def Reload(self):
        if self.magazines > 0:
            self.sound.Play(self.sound.reLoad)
            self.reloadweapon = True
            self.reloadtime = 3
            clock.schedule_interval(self.reloadCall, 1.0)
    def select(self):
        #print 'pistol mode'
        #self.mode = HandleModeSelect(Const.assaultRifleModes, self.mode)
        self.mode = HandleModeSelect(self.availableModes, self.mode)
        
        self.SetText()
        print self.mode
        if self.mode == Const.assaultRifleAuto:
            clock.schedule_interval(self.autocall, self.rateFire)
            self.auto = True
        elif self.auto:
            clock.unschedule(self.autocall)
            self.auto = False
    def SetSights(self,win):
        image = pyglet.image.load(Const.folder+self.reticle)
        x = image.height / 2
        y = image.width / 2
        cursor = pyglet.window.ImageMouseCursor(image, x, y)
        win.set_mouse_cursor( cursor)
        pass
    def AddMagazines(self,numMags):
        self.magazines += numMags
            
class CurrentGame():
    def __init__(self):
        self.currentWeapon = 'nothing'
        self.weaponDict = {}
        
        #self.sound = Sounds()
        self.sound = gSound
        self.bulletholes = BulletHoles()
        
        self.knife = Knife(Const.knifeKbar)
        self.weaponDict[Const.knifeKbar] = self.knife
        
        
        self.hand = HandTool(Const.HandToolConst)
        self.weaponDict[Const.HandToolConst] = self.hand
        
        #self.pistol = Pistol(Const.pistol1911,
                             ##self.sound,
                             ##self.bulletholes
                             #)
        #self.weaponDict[Const.pistol1911] = self.pistol
        #self.M4assaultRifle = AssaultRifle(Const.M4assaultRifle,
                                         #self.sound,
                                         #self.bulletholes)
        #self.weaponDict[Const.M4assaultRifle] = self.M4assaultRifle
        
        
        #self.Sar21assaultRifle = AssaultRifle(Const.SAR21Rifle,
                                              #self.sound,
                                              #self.bulletholes)
        #self.weaponDict[Const.SAR21Rifle] = self.Sar21assaultRifle
                                        
        self.AddRifleWeapon(Const.M4assaultRifle,10)
        self.AddRifleWeapon(Const.SAR21Rifle,10)
        self.AddRifleWeapon(Const.Ultimax100SAW,3)
        self.AddRifleWeapon(Const.M134MiniGun,1)
        self.AddRifleWeapon(Const.pistol1911,6)
        self.AddRifleWeapon(Const.M32GRENADElauncher,6)
        self.AddRifleWeapon(Const.STCPW,5)
        self.AddRifleWeapon(Const.GLOCK,5)
        self.AddRifleWeapon(Const.M249SAW,2)
        self.AddRifleWeapon(Const.M107sniper,4)
        self.AddRifleWeapon(Const.ClaymoreMine, 2)
        self.AddRifleWeapon(Const.MP5, 5)
        self.AddRifleWeapon(Const.AK47, 9)
        self.AddRifleWeapon(Const.MP7silent, 9)
        
        self.choose(Const.HandToolConst) #default to hand
        
        self.hero = Hero()
        gShootGallery.initAttack(self.hero)
        #self.tb = TargetBoard()
        
    def AddRifleWeapon(self,name,magazinesCarried):
        self.weaponDict[name] = AssaultRifle(name,
                                             magazinesCarried
                                             #self.sound,
                                             #self.bulletholes
                                             )
        pass
        
    def choose(self,weapon):
        self.currentWeapon = weapon
        #print 'current weapon', self.currentWeapon
        try:
            self.cw = self.weaponDict[self.currentWeapon]
            #print 'namee', self.cw.name
            
        except:
            print '{ERROR} choose weapon'
    def mousedown(self,x,y):
        #print 'name m', self.cw.name
        self.cw.mouse(x,y)
        #self.tb.Hit(x, y)
    def mousepos(self,x,y):
        self.cw.mousepos(x,y)
    def mouseup(self,x,y):
        self.cw.mouseup(x,y)
    def mousedrag(self,x,y):
        self.cw.mousedrag(x,y)
    def reloadWeapom(self):
        self.cw.Reload()
    def select(self):
        self.cw.select()
    def draw(self):
        #gTargetBoard.Draw()
        gShootGallery.Draw()
        self.cw.draw()
        self.hero.draw() 
    def SetSight(self,win):
        self.cw.SetSights(win)
        #image = pyglet.image.load(Const.folder+'reticle.png')
        #cursor = pyglet.window.ImageMouseCursor(image, 25, 25)
        #return cursor
    def AddMagazines(self):
        self.cw.AddMagazines(5)
    def key9(self,whichkey):
        self.choose(gShootGallery.key9(whichkey))
        pass
#class CurrentGame():

class FPSWin(pyglet.window.Window):
    def __init__(self):
        super(FPSWin, self).__init__(resizable = True) 
        self.maximize() 
        #self.set_visible(visible=False)
        self.ikey = False # allow i key to toggle
        self.set_caption('SHOOTER the game by George Loo')
        self.set_fullscreen(True, screen=None)
        #self.set_exclusive_mouse()
        #self.set_size(1600, 900)
        #print 'winsize',Const.winHeight, Const.winWidth
        #self.set_location(300,50)
        self.clear()
        gShootGallery.setWinSize(self.width, self.height)
        gShootGallery.init()
        self.game = CurrentGame()
        self.game.SetSight(self) #pass in window self
        #gmw.set_visible(visible=True)
        self.set_visible(visible=True)

    def on_mouse_press(self,x, y, button, modifiers):
        if button==pyglet.window.mouse.LEFT:
            #print 'mouse left'
            self.game.mousedown(x,y)
            pass
            #self.set_fullscreen(False, screen=None)
        if button==pyglet.window.mouse.RIGHT:
            #print 'mouse right'
            pass 
        

    def on_mouse_release(self,x, y, button, modifiers):	   
        if button==pyglet.window.mouse.LEFT:
            #print 'mouse left up'
            self.game.mouseup(x,y)
            pass
        if button==pyglet.window.mouse.RIGHT:
            #print 'mouse right up'
            pass 
        

    def on_mouse_motion(self, x, y, dx, dy):
        ##print 'motion'
        self.game.mousepos(x,y)
        #pass
        
    #def on_resize(self, width, height):
        #print 'resize',width, height
        #self.set_size(width, height)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons==pyglet.window.mouse.LEFT:
            #print 'drag'
            self.game.mousedrag(x,y)
            pass   

    def on_key_press(self, symbol, modifiers):
        if symbol == key.F12:
            #print 'F12'
            pass
        elif symbol == key._1:
            #print '1',Const.knifeKbar
            #self.game.choose(Const.knifeKbar)
            self.game.key9(1)
            self.game.SetSight(self)
        elif symbol == key._2:
            #print '2',Const.pistol1911
            self.game.key9(2)
            #self.game.choose(Const.pistol1911)
            self.game.SetSight(self)
        elif symbol == key._3:
            #print '3'
            #self.game.choose(Const.M4assaultRifle)
            self.game.key9(3)
            self.game.SetSight(self)
        elif symbol == key._4:
            #self.game.choose(Const.SAR21Rifle)
            self.game.key9(4)
            #print '4'
            self.game.SetSight(self)
            #self.set_mouse_cursor( self.game.GetSight())
        elif symbol == key._5:
            #self.game.choose(Const.Ultimax100SAW)
            self.game.key9(5)
            self.game.SetSight(self)
            #print '5'
        elif symbol == key._6:
            self.game.key9(6)            
            #self.game.choose(Const.M134MiniGun)
            self.game.SetSight(self)
            #print '6'
        elif symbol == key._7:
            self.game.key9(7)
            #self.game.choose(Const.M32GRENADElauncher)
            self.game.SetSight(self)
            #print '7'
        elif symbol == key._8:
            self.game.key9(8)
            self.game.SetSight(self)
            pass #print '8'
            #gmw.hide()
        elif symbol == key._9:
            self.game.key9(9)
            self.game.SetSight(self)
            pass
            #print '9'
        elif symbol == key._0:
            #print '0'
            self.game.key9(0)
            #self.game.choose(Const.HandToolConst)
            self.game.SetSight(self)
            
            pass
        elif symbol == key.I:
            if not self.ikey: 
                self.set_fullscreen(False, screen=None)
                self.ikey = True
                gmw.show()
            elif self.ikey:
                #gmw.hide()
                self.set_fullscreen(True, screen=None)
                self.ikey = False
                
            #self.set_visible(visible=False) 
            #
            
        elif symbol == key.Z:
            #print 'Z'
            self.game.reloadWeapom()
        elif symbol == key.B:
            #print 'B - selector'
            self.game.select()
        elif symbol == key.W:
            self.game.hero.goUp()
        elif symbol == key.A:   
            self.game.hero.goLeft()
        elif symbol == key.S:
            self.game.hero.goBack()
        elif symbol == key.D:
            self.game.hero.goRight()
            
    def on_key_release(self, symbol, modifiers):
        if symbol == key.W:
            self.game.hero.stopMoving()
        elif symbol == key.A:   
            self.game.hero.stopMoving()
        elif symbol == key.S:
            self.game.hero.stopMoving()
        elif symbol == key.D:
            self.game.hero.stopMoving()
        elif symbol == key.F1:
            pass
            #gBattleRep.init() #reset stats
            #gBattleRep.report()
        elif symbol == key.F12 and modifiers & key.MOD_SHIFT:
            print 'shift F12'
            gShootGallery.init()
        elif symbol == key.F12:
            gShootGallery.gamestage += 1
            gShootGallery.init()
        elif symbol == key.F: #first aid = F
            if gBattleRep.herohit > 0:
                gSound.Play(gSound.reliefSound)
                gBattleRep.herohit -= 1  #first aid
                gBattleRep.report()
            if gBattleRep.herohit == 0:
                gSound.Play(gSound.curedSound)
        elif symbol == key.U:
            self.game.AddMagazines()
        elif symbol == key.P:
            gShootGallery.pause()
        elif symbol == key.CAPSLOCK:
            gShootGallery.runToggle()
        
    def on_draw(self):
        self.clear()
        self.game.draw()
        
    def on_close(self):
        gmw.close()
        self.close()
        

if __name__ == "__main__":
           
    #gmw = MessageWin('Messages')
    #gmw2 = MessageWin('Main')
    m = FPSWin() 
    pyglet.app.run()   
