import pygame


def update_dis(points,lines,screen):
    screen.fill((0,0,0))
    draw_points(points)
    draw_lines(lines)
    pygame.display.update()


def draw_points(points):
    for p in points:
        #print(p)
        #print(points)
        pygame.draw.circle(screen, (0,150,150), p[0], radius)
    pygame.display.update()

def get_n():
    global n_vertex
    return n_vertex+1

def add_n():
    global n_vertex
    n_vertex += 1
    return n_vertex

def point_with_edge(p):
    global lines
    pwe = []
    for [p1,p2,vxs] in lines:
        if p[1] in vxs:
            pwe.append([p1,p2,vxs])
    if len(pwe) == 0:
        return False
    else:
        return pwe

def remove_edge(line):
    global lines
    p1,p2 = line[2]
    for i,l in enumerate(lines):
        if p1 in l[2] and p2 in l[2]:
            del lines[i]



def update_edge(line,new_p):
    global points
    p1 = new_p[0]
    p2 = (0,0)
    for p in points:
        if p[1] in line[2] and p[1] != new_p[1]:
            p2 = p[0]
            pygame.draw.line(screen, (0,200,0), p1, p2)
            remove_edge(line)
            lines.append([p1, p2,line[2]])
            break
    



def moving_point(p):
    global lines, points,screen
    n = p[1]
    while True:
        #print('bla')
        #print(pygame.mouse.get_pressed())
        if pygame.mouse.get_pressed() == (0, 0, 1):
            print('blabla')
            points.remove(p)
            new_p = [pygame.mouse.get_pos(),n]
            p = new_p
            points.append(new_p)
            update_dis(points,lines,screen)
            #print('dentro')
            trash = pygame.event.get()
            pygame.event.clear()
            
            edges = point_with_edge(p)

            if edges:
                print('KKKKKKKKKKK')
                for ed in edges:
                    update_edge(ed,new_p)


        else:
            pygame.event.clear()
            return 0
        #break

def draw_lines(lines):
    for p1,p2,coord in lines:
        #print(lines)
        pygame.draw.line(screen, (0,200,0), p1, p2)

'''
def drag_line(p,points,lines):
    count = 0
    pygame.event.clear()
    while True:
        count += 1
        #print(pygame.mouse.get_pressed())
        #if pygame.mouse.get_pressed() == (0, 0, 1):
        pygame.draw.line(screen, (0,200,0), p, pygame.mouse.get_pos())
        print('l')
        
        if count%10 == 0: 
            update_dis(points,lines,screen)
            
        
        pygame.display.update()
        #trash = pygame.event.get()
        

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                (x,y) = pos
                for other_p in points:
                    (px,py) = other_p
                    if (((x-px)**2 + (y-py)**2)**(1/2)) < radius+5:
                        pygame.draw.line(screen, (0,200,0), p, other_p)
                        lines.append([p,other_p])
                        update_dis(points,lines,screen)
                        return pos
                update_dis(points,lines,screen)
                return 0
'''

def drag_line(p):
    global lines, points
    pygame.event.clear()
    count = 0
    while True:
        #print(pygame.mouse.get_pressed())
        if pygame.mouse.get_pressed() == (1, 0, 0):
            #print('ckaa')
            pygame.event.get()
            
            if count == 10:
                update_dis(points,lines,screen)
                pygame.draw.line(screen, (0,200,0), p[0], pygame.mouse.get_pos())
                count = 0
            pygame.display.update()
                
            count += 1
        else:
            pos = pygame.mouse.get_pos()
            (x,y) = pos
            for other_p in points:
                [(px,py),n] = other_p
                if (((x-px)**2 + (y-py)**2)**(1/2)) < radius+5:
                    #pygame.draw.line(screen, (0,200,0), p, other_p)
                    sorted_points = sorted([p[1],other_p[1]])
                    print(([p[0],other_p[0],sorted_points]))
                    lines.append([p[0],other_p[0],sorted_points])
                    update_dis(points,lines,screen)
                    print('entered')
                    break
            update_dis(points,lines,screen)
            break
   

# constants 
display_width = 800
display_height = 600
radius = 5 # node size
n_vertex = -1

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
screen.fill((0,0,0)) # param is color tuple

LEFT = 1
RIGHT = 3
count_double = False

points = []
lines = []
running = True
last_click = -2
while running:
    for event in pygame.event.get():

        # salir  
        if event.type == pygame.QUIT:
            running = False

        # create vertex or edge
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            now = pygame.time.get_ticks()
            pos = pygame.mouse.get_pos()

            toque = False
            (x,y) = pos
            for p in points:
                [(px,py),n] = p

                # create edge
                if (((x-px)**2 + (y-py)**2)**(1/2)) < radius+5:
                    #print("toqué puntito") 
                    toque = True
                    #rapid = True
                    
                    # borrando puntitos (doble click)
                    '''
                    double_click = False
                    if now - last_click <= 500:
                        double_click == True
                    last_click = pygame.time.get_ticks()
                    
                    if now - last_click <= 500: # miliseconds
                        print(now,last_click)
                        print('fast')
                        points.remove(p)
                        update_dis(points,lines,screen)
                    '''
                    
                    #if now - last_click >= 500:
                    print('línea')
                    drag_line(p)
                        #pygame.event.clear()
                        #rapid = False
                    
                    #print(pygame.mouse.get_pressed())  
                    #if rapid:  
                        #last_click = pygame.time.get_ticks()

            # create vertex
            if not toque:
                points.append([pos,add_n()])
                pygame.draw.circle(screen, 
                (0,150,150), pos, radius)
                pygame.display.update()
                #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]

    # moving vertex
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
        for p in points:
                [(px,py),n] = p
                (x,y) = pygame.mouse.get_pos()
                if (((x-px)**2 + (y-py)**2)**(1/2)) < radius: 
                    print('aksdjfalfjalsk')          ## ¡Por alguna razón entra aquí y se cicla si al mover un punto dejo el mouse sobre él al soltar el click!
                    new_p = pygame.mouse.get_pos()
                    #p = new_p
                    
                    moving_point(p)
                    pygame.event.clear()
                    


    #print(last_click)
    # clickear puntitos
print(points)
print(lines)
#print(clicked_sprites)