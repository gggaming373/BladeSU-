import pgzrun
from pgzhelper import *
import PySimpleGUI as sg

WIDTH = 800
HEIGHT = 600
FPS = 400
TITLE = 'BladeSU!'


#MAP STUFF INFO : DELETE 0.78 FROM EVERY BEAT WHEN MAKING A MAP ( 078 )

gameIcon =pygame.image.load('images/zupscaled.png')
pygame.display.set_icon(gameIcon)



music.set_volume(0.5)


start = False
totalhits = 0
misses = 0
goodhits = 0
wronghits = 0
performance = 0
playtimeleft = 0

gamemode = 'menu'
selectedmusic = 'nothing'
isitfullscreen = False





zenemies = []

for i in range (100):
    zenemy = Actor('z', (1000, 300))
    zenemies.append(zenemy)

zenemy_index = 0



xenemies = []

for i in range (100):
    xenemy = Actor('x',(1000, 300))
    xenemy.scale = 8
    xenemies.append(xenemy)

xenemy_index = 0

logofontsize = 120

arkaplan = Actor('hud', (400, 300))
xenemy = Actor('x', (1000, 300))
xenemy.scale = 8
attackplace = Actor('attackplace',(170,300))
attackplace.scale = 8
player = Actor('idle1',(100,300))
player.images = ['idle1', 'idle2', 'idle3', 'idle4']
player.fps = 5

startbutton = Actor('buttonpink',(400, 380))
lvl1button = Actor('buttonsilver',(100, 550))
lvl2button = Actor('buttongold',(300, 550))
lvl3button = Actor('buttonblue',(500, 550))
settingsbutton = Actor('buttonsettings',(730, 550))

player.scale = 7
arkaplan.scale = 8
startbutton.scale = 8 
lvl1button.scale = 6 
lvl2button.scale = 6 
lvl3button.scale = 6 
settingsbutton.scale = 6

def gobackidle():
    player.images = ['idle1', 'idle2', 'idle3', 'idle4']
    player.fps = 5

def hits(hitkey):
    global totalhits
    global misses
    global goodhits
    global wronghits
    if gamemode == 'game':
        if hitkey == keys.Z:
            sounds.beat.play()
            totalhits += 1
            
        
            touchingz = attackplace.collidelist(zenemies)
            if touchingz != -1:
                print('z yes')
                goodhits += 1
                animate(zenemies[touchingz], tween='linear', duration=0.2, x = 1000, y = 1000)
                
            else:
                print('z no')
                wronghits += 1

            #animation
            player.fps = 20
            player.images = ['sweep1','sweep2', 'sweep3', 'sweep4']
            clock.schedule_unique(gobackidle, 0.12)
        elif hitkey == keys.X:
            sounds.beat.play()
            totalhits += 1
            touchingx = attackplace.collidelist(xenemies)
            if touchingx != -1:
                print('x yes')
                goodhits += 1
                animate(xenemies[touchingx], tween='linear', duration=0.2, x = 1000, y = 1000)
                
            else:
                print('x no')
                wronghits += 1

            #animation
            player.fps = 20
            player.images = ['sweep1','sweep2', 'sweep3', 'sweep4']
            clock.schedule_unique(gobackidle, 0.12)
    



def update():
    global logofontsize
    global performance
    player.animate()
    performance = goodhits - wronghits - misses
    
    
    

def draw():
    if gamemode == 'menu':
        arkaplan.draw()
        startbutton.draw()
        lvl1button.draw()
        lvl2button.draw()
        lvl3button.draw()
        settingsbutton.draw()
        screen.draw.text('START', (345, 365), color=(0,0,0), fontsize=50)
        screen.draw.text('So Cold', (45, 540), color=(0,0,0), fontsize=40)
        screen.draw.text('Ride', (270, 540), color=(0,0,0), fontsize=40)
        screen.draw.text('On & Off', (440, 540), color=(0,0,0), fontsize=40)
        screen.draw.text('BladeSU!', (200, 100), color=(0,0,50), fontsize=logofontsize, owidth=1, ocolor = (120,0,255))
    elif gamemode == 'game':
        arkaplan.draw()
        attackplace.draw()
        player.draw()
        for i in range (len(zenemies)):
            zenemies[i].draw()
        for i in range (len(xenemies)):
            xenemies[i].draw()
        xenemy.draw()
        screen.draw.text('Total Hits : '+str(totalhits), (10, 570), color="black", fontsize = 40)
        screen.draw.text('Time Left : '+ str(playtimeleft)+ 'sec' , (10, 550), color="black", fontsize = 30)
        screen.draw.text('Wrong Hits : '+str(wronghits), (570, 570), color="black", fontsize = 40)
        screen.draw.text('Good Hits : '+str(goodhits), (570, 540), color="black", fontsize = 40)
        screen.draw.text('Misses : '+str(misses), (570, 510), color="black", fontsize = 40)
        screen.draw.text('PERFORMANCE : '+str(performance), (10, 510), color="black", fontsize = 60)
    elif gamemode == 'intro':
        intro.draw()

def on_key_down(key):
    global totalhits
    hits(key)
    



def missed():
    global misses
    print('miss')
    sounds.miss.play()
    misses += 1

def create_xenemy():
    global xenemy_index
    zenemies[xenemy_index].scale = 8
    zenemies[xenemy_index].pos = (1000, 300)
    animate(xenemies[xenemy_index], tween='linear', duration=1.1, x = 110, y = 300, on_finished = missed)
    xenemy_index += 1

def create_zenemy():
    global zenemy_index

    zenemies[zenemy_index].scale = 8
    zenemies[zenemy_index].pos = (1000, 300)
    animate(zenemies[zenemy_index], tween='linear', duration=1.1, x = 110, y = 300, on_finished = missed)
    zenemy_index += 1

def gamestart(musicselected):
    global gamemode
    gamemode = 'game'
    music.play_once(musicselected)
    if musicselected == 'socold':
        clock.schedule(create_xenemy, 1.39)
        clock.schedule(create_zenemy, 3.32)
        clock.schedule(create_zenemy, 6.42)
        clock.schedule(create_xenemy, 9.32)
        clock.schedule(create_zenemy, 9.42)
        clock.schedule(create_xenemy, 10.27)
        clock.schedule(create_xenemy, 11.39)
        clock.schedule(create_zenemy, 11.45)
        clock.schedule(create_zenemy, 13.26)
        clock.schedule(create_xenemy, 15.31)
        clock.schedule(create_zenemy, 17.35)
        clock.schedule(create_zenemy, 18.42)
        clock.schedule(create_xenemy, 20.36)
        clock.schedule(create_zenemy, 22.28)
        clock.schedule(create_zenemy, 23.25)
        clock.schedule(create_xenemy, 23.45)
        clock.schedule(create_xenemy, 27.32)
        clock.schedule(create_xenemy, 29.25)
        clock.schedule(create_xenemy, 30.22)
        clock.schedule(create_zenemy, 30.42)
        clock.schedule(create_xenemy, 32.36)
    elif musicselected == 'onandoff':
        clock.schedule(create_xenemy, 5.30)
        clock.schedule(create_zenemy, 6.42)
        clock.schedule(create_xenemy, 7.33)
        clock.schedule(create_xenemy, 8.22)
        clock.schedule(create_xenemy, 8.37)
        clock.schedule(create_zenemy, 9.24)
        clock.schedule(create_zenemy, 9.38)
        clock.schedule(create_xenemy, 10.00)
        clock.schedule(create_zenemy, 10.25)
        clock.schedule(create_zenemy, 10.38)
        clock.schedule(create_xenemy, 11.26)
        clock.schedule(create_zenemy, 11.36)
        clock.schedule(create_xenemy, 12.22)
        clock.schedule(create_xenemy, 12.32)
        clock.schedule(create_zenemy, 12.95)
        clock.schedule(create_xenemy, 13.00)
    elif musicselected == 'ride':
        clock.schedule(create_xenemy, 1.10 - 0.78)
        clock.schedule(create_xenemy, 2.05 - 0.78)
        clock.schedule(create_zenemy, 2.24 - 0.78)
        clock.schedule(create_zenemy, 4.06 - 0.78)
        clock.schedule(create_xenemy, 5.21 - 0.78)
        clock.schedule(create_zenemy, 7.00 - 0.78)
        clock.schedule(create_xenemy, 7.21 - 0.78)
        clock.schedule(create_zenemy, 8.05 - 0.78)
        clock.schedule(create_xenemy, 8.15 - 0.78)
        clock.schedule(create_zenemy, 9.11 - 0.78)
        clock.schedule(create_xenemy, 9.20 - 0.78)
        clock.schedule(create_zenemy, 10.06 - 0.78)
        clock.schedule(create_zenemy, 10.16 - 0.78)
        clock.schedule(create_zenemy, 13.12 - 0.78)
        

        

        
        
        
    print(musicselected)

        

        

        

        



        
        


def on_mouse_down(button, pos):
    
    global gamemode
    global selectedmusic
    global isitfullscreen
    if gamemode == 'menu':
        if startbutton.collidepoint(pos):
            sounds.gamestart.play()
            if selectedmusic == 'ride':
                gamestart('ride')
            if selectedmusic == 'socold':
                gamestart('socold')
            if selectedmusic == 'onandoff':
                gamemode = 'game'
                gamestart('onandoff')
        elif lvl1button.collidepoint(pos):
            selectedmusic = 'socold'
            sounds.buttonpressmusic.play()
        elif lvl2button.collidepoint(pos):
            selectedmusic = 'ride'
            sounds.buttonpressmusic.play()
        elif lvl3button.collidepoint(pos):
            selectedmusic = 'onandoff'
            sounds.buttonpressmusic.play()
        elif settingsbutton.collidepoint(pos):
            sounds.buttonpressmusic.play()
            event, values = sg.Window('Settings', 
                                        [[sg.Text('Filename')], 
                                        [sg.Text('Music Sound'), sg.Slider((0,10),default_value= music.get_volume()*10, orientation='h', s=(10,15))], 
                                        [sg.Text('Fullscreen Mode') ,sg.Checkbox('',default=isitfullscreen)],
                                        [sg.OK(),] 
                                        ]).read(close=True)
            if values[0] != None:
                sounds.buttonpressmusic.play()
                music.set_volume(values[0]/10)
                print(music.get_volume())
            else:
                music.set_volume(0.5)
                sounds.buttonpressmusic.play()
                print(music.get_volume())
                sg.popup('You Exited Without Pressing "OK" Because Of That, These Happened.')
                sounds.buttonpressmusic.play()
                sg.popup('FullScreen Mode : OFF   Music Volume : 0.5')
                sounds.buttonpressmusic.play()
            if values[1] == True:
                set_fullscreen()
                isitfullscreen = True
                    
            else:
                set_windowed()
                isitfullscreen = False
                    
                    

                
                
                

def on_music_end():
    global gamemode
    global goodhits
    global wronghits
    global misses
    global performance
    print('bitti')
    sounds.ding.play()
    sg.popup('Your Stats','PERFORMANCE : ' + str(performance), 'Misses : ' + str(misses), 'Good Hits : ' + str(goodhits), 'Wronghits : ' + str(wronghits))
    sounds.buttonpressmusic.play()
    performance = 0 
    misses = 0
    goodhits = 0 
    wronghits = 0
    if gamemode == 'game':
        gamemode = 'menu'
        




pgzrun.go()
