import pygame
import time
import random

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
black=(0,0,0)
white=(255,255,255)

red=(255,0,0)
light_red=(155,0,0)

yellow=(150,150,0)
light_yellow=(200,200,0)

green=(50,155,10)




aqua=(0,255,255)
orange=(255,69,0)
maroon=(128,0,0)
dark_red=(139,0,0)
brown=(165,42,42)
firebrick=(178,34,34)
crimson=(220,20,60)
sky_blue=(135,206,250)

tomato=(255,99,71)
coral=(255,127,80)
indian_red=(205,92,92)
light_coral=(240,128,128)
dark_salmon =(233,150,122)
salmon=(250,128,114)
light_salmon=(255,160,122)
orange_red=(255,69,0)
dark_orange =(255,140,0)
orange=(255,165,0)
gold=(255,215,0)
dark_golden_rod	=(184,134,11)
golden_rod  =(218,165,32)
pale_golden_rod	=(238,232,170)
dark_khaki=(189,183,107)
khaki=(240,230,140)
olive=(128,128,0)
yellow=(255,255,0)
yellow_green=(154,205,50)
dark_olive_green= (85,107,47)
olive_drab=(107,142,35)
lawn_green  =(124,252,0)
chart_reuse =(127,255,0)
green_yellow=(173,255,47)
dark_green=(0,100,0)

forest_green=(34,139,34)
lime=(0,255,0)
lime_green= (50,205,50)
light_green=(144,238,144)
pale_green=(152,251,152)
dark_sea_green	=   (143,188,143)
medium_spring_green=(0,250,154)
spring_green=(0,255,127)
sea_green   =(46,139,87)
medium_aqua_marine  =(102,205,170)
medium_sea_green=(60,179,113)
light_sea_green	=(32,178,170)
dark_slate_gray	=(47,79,79)
teal=(0,128,128)
dark_cyan=(0,139,139)
aqua=(0,255,255)
cyan=(0,255,255)
light_cyan= (224,255,255)

turquoise=(64,224,208)

midnight_blue=	(25,25,112)
navy	=(0,0,128)

medium_blue=(0,0,205)
blue=(0,0,255)
royal_blue=(65,105,225)
blue_violet =(138,43,226)
indigo=(75,0,130)

purple=(128,0,128)

plum=(221,160,221)
violet=(238,130,238)
magenta=(255,0,255)
orchid=(218,112,214)
medium_violet_red=(199,21,133)
pale_violet_red=(219,112,147)
deep_pink=(255,20,147)
hot_pink=(255,105,180)
light_pink=(255,182,193)

chocolate=	(210,105,30)

 

smallfont = pygame.font.SysFont("Purisa",20)
medfont = pygame.font.SysFont("Purisa",50)
largefont = pygame.font.SysFont("Purisa",80)

disp_width=800
disp_heig=600



tankwidth = 40
tankheight =20

shell_radius= 5

barrier_width=50
turretwidth=3
turretlength=20
wheelradius=5
ground_height=35


clock=pygame.time.Clock()
pygame.display.set_caption("AVI")
gameDisplay = pygame.display.set_mode((disp_width,disp_heig))

gameDisplay.fill(white)
pygame.display.update()

def screen_obj(msg,color,size):
    if size =="medium":
        textsurface=medfont.render(msg,True,color)
    elif size =="small":
        textsurface=smallfont.render(msg,True,color)
    elif size =="large":
        textsurface=largefont.render(msg,True,color)
    
    return textsurface,textsurface.get_rect()

def barrier(xlocation,randomheight,barrier_width=50):

    pygame.draw.rect(gameDisplay,crimson ,[xlocation,disp_heig - randomheight , barrier_width ,randomheight])



def pause():
    paused = True
    toscreen("GAME PAUSED!!.",black,-50)
    toscreen("Press c to continue or n to start a new game",green,100)
    toscreen("Press q to quit the game",green,120)
    pygame.display.update()
    while paused:
        
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                       

                if event.key == pygame.K_n:
                    
                    menu()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                

                
def tobutton(msg,color,buttonx,buttony,button_w,button_h,size="small"):
   
    textsurf,textrect= screen_obj(msg,color,size)
    textrect.center =(buttonx + button_w/2 , buttony + button_h/2 )
    gameDisplay.blit(textsurf,textrect)

def toscreen(msg,color,y_displace,size="small"):
    ##    text=font.render(msg,True,color)
    ##    gameDisplay.blit(text,[disp_width/2-len(msg),disp_heig/2])
    textsurf,textrect= screen_obj(msg,color,size)
    textrect.center =(disp_width/2 , disp_heig /2 + y_displace)
    gameDisplay.blit(textsurf,textrect)

def explosion(x,y):
    
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q :
                    
                    menu()

        startpoint= x,y

        colors =[red,light_red,yellow,light_yellow]

        magnitude=1
        while magnitude < 50:

            explode_x = x + random.randrange(-1*magnitude,magnitude) 
            explode_y = y + random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay,colors[random.randrange(0,4)],(explode_x,explode_y),random.randrange(1,5))
            magnitude += 1
            pygame.display.update()
            clock.tick(100)

        explode =False        

    
def power(level,xlocation,shooter):
    if (shooter == 'e'):
        text = smallfont.render ("Power:" + str(level) + "%",True,brown)
        gameDisplay.blit(text,[ int(xlocation/2), 0 ])
    else:
        text = smallfont.render ("Power:" + str(level) + "%",True,brown)
        gameDisplay.blit(text,[int((xlocation + disp_width)/2) , 0 ])
    
def tank(x,y,color,turpos):
    x=int(x)
    y=int(y)

    possible_turret =[(x-27 , y-2),(x-24 , y-7),(x-21 , y-10),(x-18 , y-14),(x-15 , y-18),(x-12 , y-21),(x-5,y-25),(x-8 , y-25)]
    
    pygame.draw.circle(gameDisplay,color,(x,y),int(tankheight/2))
    pygame.draw.rect(gameDisplay,color,(x-tankwidth/2,y, tankwidth,tankheight))
    pygame.draw.line(gameDisplay,color,(x,y),possible_turret[turpos] ,turretwidth )

    pygame.draw.circle(gameDisplay,color , (x-int(tankwidth/4) , y + tankheight ) ,int(tankheight/4)  )
    pygame.draw.circle(gameDisplay,color , (x+int(tankwidth/4) , y + tankheight ) ,wheelradius  )
    pygame.draw.circle(gameDisplay,color , (x , y + tankheight ) ,wheelradius  )   

    return possible_turret[turpos]

def enemy_tank(x,y,color,turpos):
    x=int(x)
    y=int(y)

    possible_turret =[(x+27 , y-2),(x+24 , y-7),(x+21 , y-10),(x+18 , y-14),(x+15 , y-18),(x+12 , y-21),(x+5,y-25),(x+8 , y-25)]
    
    pygame.draw.circle(gameDisplay,color,(x,y),int(tankheight/2))
    pygame.draw.rect(gameDisplay,color,(x-tankwidth/2,y, tankwidth,tankheight))
    pygame.draw.line(gameDisplay,color,(x,y),possible_turret[turpos] ,turretwidth )

    pygame.draw.circle(gameDisplay,color , (x-int(tankwidth/4) , y + tankheight ) ,int(tankheight/4)  )
    pygame.draw.circle(gameDisplay,color , (x+int(tankwidth/4) , y + tankheight ) ,wheelradius  )
    pygame.draw.circle(gameDisplay,color , (x , y + tankheight ) ,wheelradius  )   

    return possible_turret[turpos]
    
def fire(xy,tankx,tanky,turpos,fire_power,xlocation,randomheight,enemyx,enemyy):
    
    fire=True
    startshell = list(xy)
    a=0
    while fire:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q :
                    
                    menu()

        power(fire_power,xlocation,'m') 
        
        pygame.draw.circle(gameDisplay,indigo , (startshell[0] , startshell[1] ) ,shell_radius  )
        
        startshell[0] -= (12 - turpos )*2
        
        
            
        startshell[1] +=  int(( ( (startshell[0] - xy[0])*(0.75/fire_power))**2) - (turpos + turpos/(12-turpos)))

        if startshell[1] > disp_heig - ground_height:
            hit_x = int((startshell[0] * disp_heig - ground_height) / startshell[1] )
            hit_y = int(disp_heig -ground_height)
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startshell[0] <=  xlocation + barrier_width 
        check_x_2 = startshell[0] >= xlocation

        check_y_1 = startshell[1] <= disp_heig
        check_y_2 = startshell[1] >= disp_heig - randomheight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2 :
            hit_x = int(startshell[0] )
            hit_y = int(startshell[1])
            explosion(hit_x,hit_y)
            fire = False
        check_x_1 = startshell[0] <= enemyx + int(tankheight/2)
        check_x_2 = startshell[0] >= enemyx - int(tankheight/2)

        check_x_3 = startshell[0] <= enemyx + int(tankwidth/2)
        check_x_4 = startshell[0] >= enemyx + int(tankheight/2)

        check_x_5 = startshell[0] >= enemyx - int(tankwidth/2)
        check_x_6 = startshell[0] <= enemyx - int(tankheight/2)        
        
        check_y_1 = startshell[1] <= disp_heig - ground_height 
        check_y_2 = startshell[1] >= disp_heig - ground_height - tankheight -wheelradius - int(tankheight/2)


        if check_y_1 and check_y_2 :
            
            if check_x_1 and check_x_2 :
                a=-20
            elif (check_x_3 and check_x_4 ) or  (check_x_5 and check_x_6 ):
                a=-10
            else :
                a=5
            
        pygame.display.update()
        clock.tick(50)
    return a  
        
def e_fire(xy,tankx,tanky,turpos,fire_power,xlocation,randomheight,enemyx,enemyy):
    
    fire=True
    startshell = list(xy)
    a=0
    while fire:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q :
                    
                    menu()
        pygame.draw.circle(gameDisplay,indigo , (startshell[0] , startshell[1] ) ,shell_radius  )
        
        startshell[0] += (12 - turpos )*2

        startshell[1] +=  int(( ( (startshell[0] - xy[0])*(0.75/fire_power))**2) - (turpos + turpos/(12-turpos)))

        if startshell[1] > disp_heig - ground_height:
            hit_x = int((startshell[0] * (disp_heig - ground_height)) / startshell[1] )
            hit_y = int(disp_heig -ground_height)
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startshell[0] <=  xlocation + barrier_width 
        check_x_2 = startshell[0] >= xlocation

        check_y_1 = startshell[1] <= disp_heig
        check_y_2 = startshell[1] >= disp_heig - randomheight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2 :
            hit_x = int(startshell[0] )
            hit_y = int(startshell[1])
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startshell[0] <= enemyx + int(tankheight/2)
        check_x_2 = startshell[0] >= enemyx - int(tankheight/2)

        check_x_3 = startshell[0] <= enemyx + int(tankwidth/2)
        check_x_4 = startshell[0] >= enemyx + int(tankheight/2)

        check_x_5 = startshell[0] >= enemyx - int(tankwidth/2)
        check_x_6 = startshell[0] <= enemyx - int(tankheight/2)        
        
        check_y_1 = startshell[1] <= disp_heig - ground_height 
        check_y_2 = startshell[1] >= disp_heig - ground_height - tankheight -wheelradius - int(tankheight/2)


        if check_y_1 and check_y_2 :
            
            if check_x_1 and check_x_2 :
                a=-20
            elif (check_x_3 and check_x_4 ) or  (check_x_5 and check_x_6 ):
                a=-10
            else :
                a=5
            
        pygame.display.update()
        clock.tick(50)           
    return a
            

def controls():
    
    gcont=True
   
    while gcont:
        for event in  pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    
                    menu()
                   
                    

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
       
        toscreen("1. Press spacebar to fire ", royal_blue,-150 )
        toscreen("2. down arrow key to move down ", medium_aqua_marine,-70 )
        toscreen("3. left arrow key to move left ", violet,0 )
        toscreen("4. right arrow key to move right ", light_salmon,100)
        
        toscreen("Press b to go back", red,200)
        draw_rect(150,25,100,50,light_green,green,"Play")
        draw_rect(350,25,100,50,light_yellow,yellow,"main")
        draw_rect(550,25,100,50,light_red,red,"Quit")
        pygame.display.update()

def gameover(player):
    toscreen("GAME OVER",violet , -150,size= "large")
    if player == 1:
        toscreen("LEFT PLAYER WINS",blue_violet, 0,size ="medium" )
    else:
        toscreen("RIGHT PLAYER WINS",blue_violet, 0,size ="medium" )
   
    toscreen("Press q to quit the game or n to start a new game",dark_olive_green, 125,size ="small" )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_n:
                menu()
                    
def health_bars(player_health,enemy_health):
    if player_health > 75:
        if player_health >100:
            player_health =100
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        if player_health <=0:
            gameover(1)
        player_health_color = red        
        
    if enemy_health > 75:
        if enemy_health >100:
            enemy_health =100
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
        if enemy_health <=0 :
            gameover(2)
            
        enemy_health_color = red      

    pygame.draw.rect(gameDisplay,player_health_color,(680,40,player_health,25))
    pygame.draw.rect(gameDisplay,enemy_health_color,(20,40,enemy_health,25))

def game():
    
    gameDisplay.fill(white)
    gameexit= False
    gameover = False
    player_health,enemy_health = 100,100
    

    tankx=disp_width*0.9
    tanky=disp_heig*0.9
    tankmove=0
    changetur=0
    turpos=0
    fire_power = 100
    power_change =0


    enemytankx = disp_width * 0.1
    enemytanky=disp_heig*0.9
    etankmove=0
    echangetur=0
    eturpos=0
    efire_power = 100
    epower_change =0
    count =0
    
    xlocation= disp_width/2 + random.randint(-0.2*disp_width , 0.2 * disp_width)
    randomheight= random.randrange(0.1*disp_heig , 0.6*disp_heig)
    
    
    while not gameexit:
        gameDisplay.fill(white)
        gameDisplay.fill(green, rect =[0,disp_heig-ground_height,disp_width,ground_height])
        gameDisplay.fill(sky_blue , rect =[0,0,disp_width,disp_heig-ground_height])
        
        
        barrier(xlocation,randomheight,barrier_width)
        health_bars(player_health,enemy_health)
        gun=tank(tankx,tanky,orange_red,turpos)
        enemygun=enemy_tank(enemytankx,enemytanky,chocolate,eturpos)
        if count%2 == 0:
            power(fire_power,xlocation,'m')
            
        else:
            power(efire_power,xlocation,'e')

        pygame.display.update()    
        
        
        while gameover ==True:
            gameDisplay.fill(aqua)
            toscreen("Game Over",red,-50,size="medium")
            toscreen("Press c to play again or q to quit",orange,50,size="small")
            toscreen("YOUR SCORE IS",orange,80,size="small")
           
          

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit=True
                    gameover=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameloop()
                    if event.key == pygame.K_q:
                        gameexit=True
                        gameover=False
            pygame.display.update()                            
        if count % 2 ==0:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        tankmove=-5
                       
                    elif event.key == pygame.K_RIGHT:
                        tankmove=5
                        
                    elif event.key == pygame.K_UP:
                        changetur=1
                        
                    elif event.key == pygame.K_DOWN:
                        changetur=-1
                       
                    elif event.key == pygame.K_p:
                          pause()

                    elif event.key == pygame.K_q:
                          menu()
                    elif event.key == pygame.K_SPACE:
                       
                        
                            power(fire_power,xlocation,'m')
                            enemy_health += fire(gun,tankx,tanky,turpos,fire_power,xlocation,randomheight,enemytankx,enemytanky)
                            enemygun=enemy_tank(enemytankx,enemytanky,chocolate,eturpos)
                            count +=1

                            

                    elif event.key == pygame.K_a:
                        power_change=1
                          
                    elif event.key == pygame.K_d:
                        power_change=-1
                            
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT :
                        tankmove=0
                    elif event.key == pygame.K_UP or  event.key == pygame.K_DOWN :
                        changetur=0
                        
                    elif event.key == pygame.K_a or event.key == pygame.K_d:
                        power_change=0       
            
            if tankx - (tankwidth/2) < xlocation + barrier_width :
                tankx+=5
            elif tankx + (tankwidth/2) > disp_width:
                tankx -= 5

                
            tankx+=tankmove
            turpos+= changetur
            if  turpos>=0 and turpos<=7:
                pass
            elif turpos<0:
                turpos=0
                
            else:
                turpos=7

            fire_power += power_change
                

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        etankmove=-5
                       
                    elif event.key == pygame.K_RIGHT:
                        etankmove=5
                        
                    elif event.key == pygame.K_UP:
                        echangetur=1
                        
                    elif event.key == pygame.K_DOWN:
                        echangetur=-1
                       
                    elif event.key == pygame.K_p:
                          pause()

                    elif event.key == pygame.K_q:
                          menu()
                    elif event.key == pygame.K_SPACE:
                            
                            power(fire_power,xlocation,'e')
                            gun=tank(tankx,tanky,orange_red,turpos)
                            player_health +=e_fire(enemygun,enemytankx,enemytanky,eturpos,efire_power,xlocation,randomheight,tankx,tanky)
                            
                            count +=1

                    elif event.key == pygame.K_a:
                        epower_change=1
                          
                    elif event.key == pygame.K_d:
                        epower_change=-1
                            
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT :
                        etankmove=0
                    elif event.key == pygame.K_UP or  event.key == pygame.K_DOWN :
                        echangetur=0
                        
                    elif event.key == pygame.K_a or event.key == pygame.K_d:
                        epower_change=0       
            
            if enemytankx + (tankwidth/2) > xlocation  :
                enemytankx -=5
            elif enemytankx - (tankwidth/2) <0:
                enemytankx += 5

                
            enemytankx+=etankmove
            eturpos += echangetur
            if  eturpos>=0 and eturpos<=7:
                pass
            elif eturpos<0:
                eturpos=0
                
            else:
                eturpos=7

            efire_power += epower_change
                




##        gameDisplay.fill(green, rect =[0,disp_heig-ground_height,disp_width,ground_height])
##        gameDisplay.fill(sky_blue , rect =[0,0,disp_width,disp_heig-ground_height])
##        
##        barrier(xlocation,randomheight,barrier_width)
##        gun=tank(tankx,tanky,orange_red,turpos)
##        enemygun=enemy_tank(enemytankx,enemytanky,chocolate,7)
        pygame.display.update()


        
        
        
        clock.tick(25)



    time.sleep(2)
    pygame.quit()
    quit()
            
    

def draw_rect(buttonx,buttony,button_w,button_h,active_color,inactive_color,msg):
    
    csr = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    
    if csr[0] > buttonx and csr[0] < buttonx + button_w  and csr[1] > buttony and csr[1] < buttony + button_h :
        pygame.draw.rect(gameDisplay,active_color,(buttonx,buttony,button_w,button_h))
        if click[0] == 1:
            if(msg == "Play"):
                game()

            elif (msg == "Controls"):
                controls()
                
            elif (msg == "main"):

                menu()

            elif (msg == "Quit"):
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(buttonx,buttony,button_w,button_h))

    tobutton(msg,black,buttonx,buttony,button_w,button_h)

    
def menu():
    
    gameDisplay.fill(white)
    pygame.display.update()
    gameover = False
    toscreen("Welcome to My Game",turquoise,-50,size="medium")
    toscreen("Press p to pause and q to quit at any time in the game.", dark_olive_green,250 )
    toscreen("Click on the desired option",orange,100 )
    toscreen("TANKS", indigo,-250,size="large" )
    while not gameover:

        draw_rect(150,450,100,50,light_green,green,"Play")
        draw_rect(350,450,100,50,light_yellow,yellow,"Controls")
        draw_rect(550,450,100,50,light_red,red,"Quit")
        pygame.display.update()

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                

        pygame.display.update()




menu()
