import pygame, random, easygui, time, sys, os

score = 0
name = "Anonymous"
Choice =  ''
seconds2 = 10
seconds = 5
rounds = 1
wins = 0
loses = 0
Bx = 1190
By = 120
Bl = 50
By1 = 340
By2 = 440
By3 = 540
Bran = 2
Hran = 2
border = 5 # width of border
SIHeight = 70 #Starting Image Height
ACHeight = 370 # Answer Choices Height
RHeight = 10
MHeight = 10
LHeight = 10
Scroll = 12
movevar2 = 0
addinterval = .125
divinterval = 12.5
otherdiv = 40

ranR = random.randint(0, 4)
ranM = random.randint(0, 4)
ranL = random.randint(0, 4)

black = [0, 0, 0]
white = [255, 255, 255]
grey = [122, 122, 122] # background color
grey2 = [200, 200, 200] # highlight color
grey3 = [90, 90, 90] # back of scroll bar
green = [0, 255, 0]
red = [255, 0, 0]
ScrollLen = [190, 250]

Anxiety1 = ['Anxiety1.jpg', 'Anxiety2.jpg', 'Anxiety3.jpg']
Ptsd1 = ['Ptsd1.jpg', 'Ptsd2.jpg', 'Ptsd3.jpg']
Anorexia1 = ['Anorexia1.jpg', 'Anorexia2.jpg', 'Anorexia3.jpg']
Bulimia1 = ['Bulimia1.jpg', 'Bulimia2.jpg', 'Bulimia3.jpg']
Schizophrenia1 = ['Schizophrenia1.jpg', 'Schizophrenia2.jpg', 'Schizophrenia3.jpg']
Adhd1 = ['Adhd1.jpg', 'Adhd2.jpg', 'Adhd3.jpg']
Bipolar1 = ['Bipolar1.jpg', 'Bipolar2.jpg', 'Bipolar3.jpg']
Depression1 = ['Depression1.jpg', 'Depression2.jpg', 'Depression3.jpg']
Anxiety2 = ['AnxietyT1.png', 'AnxietyT2.png', 'AnxietyT3.png', 'AnxietyT4.png', 'AnxietyT5.png']
Ptsd2 = ['PtsdT1.png', 'PtsdT2.png', 'PtsdT3.png', 'PtsdT4.png', 'PtsdT5.png',]
Anorexia2 = ['AnorexiaT1.png', 'AnorexiaT2.png', 'AnorexiaT3.png', 'AnorexiaT4.png', 'AnorexiaT5.png']
Bulimia2 = ['BulimiaT1.png', 'BulimiaT2.png', 'BulimiaT3.png', 'BulimiaT4.png', 'BulimiaT5.png']
Schizophrenia2 = ['SchizophreniaT1.png', 'SchizophreniaT2.png', 'SchizophreniaT3.png', 'SchizophreniaT4.png', 'SchizophreniaT5.png']
Adhd2 = ['AdhdT1.png', 'AdhdT2.png', 'AdhdT3.png', 'AdhdT4.png', 'AdhdT5.png']
Bipolar2 = ['BipolarT1.png', 'BipolarT2.png', 'BipolarT3.png', 'BipolarT4.png', 'BipolarT5.png']
Depression2 = ['DepressionT1.png', 'DepressionT2.png', 'DepressionT3.png', 'DepressionT4.png', 'DepressionT5.png']
Disorders = [Anxiety2, Ptsd2, Anorexia2, Bulimia2, Schizophrenia2, Adhd2, Bipolar2, Depression2]

home = True
repeat = True
reran = True
QuitTimer = True
Again = True
RHigh = False
MHigh = False
LHigh = False
HHigh = False
HHigh2 = False
IHigh = False
SHigh = False
move3 = True
Win = False
Lose = False
Info = False
Learn = False
Sources = False
ShowDisorder = False
mouse = False
First = True
stop = False
choose = False
movevar3 = True
timestop = False
start2 = True

screen = pygame.display.set_mode([1280, 660])

def background():
    global reran, ranR, ranM, ranL, RHigh, MHigh, LHigh, Scroll, ScrollLen, Bran, Hran, Bran2, Hran2, disorder, Disorders, ranA, ranR, ranM, ranL, ranR2, ranM2, ranL2, RHeight, MHeight, LHeight, Win, Lose, Info
    screen.fill(black)
    pygame.draw.rect(screen, grey, [10, 10, 1260, 630], 0)
    if not home:
        if ShowDisorder:
            if RHigh or MHigh or LHigh:
                if Lose:
                    color = red
                    if ranA == 1:
                        pygame.draw.rect(screen, green, [230 - border, ACHeight - border, 200 + (border * 2), RHeight + (border * 2)], 0)
                    elif ranA == 2:
                        pygame.draw.rect(screen, green, [530 - border, ACHeight - border, 200 + (border * 2), MHeight + (border * 2)], 0)
                    else:
                        pygame.draw.rect(screen, green, [830 - border, ACHeight - border, 200 + (border * 2), LHeight + (border * 2)], 0)
                    screen.blit(LoseT, (80, 50))
                elif Win:
                    color = green
                    screen.blit(WinT, (80, 50))
                else:
                    color = grey2
            if RHigh:
                pygame.draw.rect(screen, color, [230 - border, ACHeight - border, 200 + (border * 2), RHeight + (border * 2)], 0)
            elif MHigh:
                pygame.draw.rect(screen, color, [530 - border, ACHeight - border, 200 + (border * 2), MHeight + (border * 2)], 0)
            elif LHigh:
                pygame.draw.rect(screen, color, [830 - border, ACHeight - border, 200 + (border * 2), LHeight + (border * 2)], 0)
            screen.blit(Text2, (530, SIHeight - 35))
            screen.blit(pygame.image.load(os.path.join('img', disorder[ran3])), [530, SIHeight])
            if IHigh:
                pygame.draw.rect(screen, grey2, [710, SIHeight, 20, 20], 0)
            screen.blit(pygame.image.load(os.path.join('img', 'info.png')), [710, SIHeight])
            if Info:
                disorder3 = Disorders[disorder2]
                screen.blit(pygame.image.load(os.path.join('img', disorder3[0])), [730, SIHeight])
            if reran:
                ranA = random.randint(1, 3) #chooses where the correct answer will be
                if ranA == 1:
                    ranR = disorder2
                    ranM3 = random.choice([i for i in range(0,8) if i not in [ranR]])
                    ranL3 = random.choice([i for i in range(0,8) if i not in [ranM3, ranR]])
                    ranR = Disorders[disorder2]
                    ranM = Disorders[ranM3]
                    ranL = Disorders[ranL3]
                elif ranA == 2:
                    ranM = disorder2
                    ranR3 = random.choice([i for i in range(0,8) if i not in [ranM]])
                    ranL3 = random.choice([i for i in range(0,8) if i not in [ranR3, ranM]])
                    ranM = Disorders[disorder2]
                    ranR = Disorders[ranR3]
                    ranL = Disorders[ranL3]
                else:
                    ranL = disorder2
                    ranR3 = random.choice([i for i in range(0,8) if i not in [ranL]])
                    ranM3 = random.choice([i for i in range(0,8) if i not in [ranR3, ranL]])
                    ranL = Disorders[disorder2]
                    ranR = Disorders[ranR3]
                    ranM = Disorders[ranM3]
                ranR2 = random.randint(1, 4)
                ranM2 = random.randint(1, 4)
                ranL2 = random.randint(1, 4)
                reran = False
                RHeight = pygame.image.load(os.path.join('img', ranR[ranR2])).get_height()
                MHeight = pygame.image.load(os.path.join('img', ranM[ranM2])).get_height()
                LHeight = pygame.image.load(os.path.join('img', ranL[ranL2])).get_height()
            screen.blit(pygame.image.load(os.path.join('img', ranR[ranR2])), [230, ACHeight])
            screen.blit(pygame.image.load(os.path.join('img', ranM[ranM2])), [530, ACHeight])
            screen.blit(pygame.image.load(os.path.join('img', ranL[ranL2])), [830, ACHeight])
        font = pygame.font.Font('freesansbold.ttf', 25)
        if score == 0 or score <= -2 or score >= 2:
            ScoreT = font.render(("%s points" %score), True, white, grey)
        else:
            ScoreT = font.render(("%s point" %score), True, white, grey)
        if rounds == 1:
            RoundsT = font.render(("%sst round." %rounds), True, white, grey)
        elif rounds == 2:
            RoundsT = font.render(("%snd round." %rounds), True, white, grey)
        elif rounds == 3:
            RoundsT = font.render(("%srd round." %rounds), True, white, grey)
        else:
            RoundsT = font.render(("%sth round." %rounds), True, white, grey)
        screen.blit(ScoreT, (1100, 30))
        screen.blit(RoundsT, (1100, 70))
        if Bran == 1:
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join('img', "Brain.png")), (50, 50)), (Bran2, 590))
        if Hran == 1:
            screen.blit(pygame.transform.scale(pygame.image.load(os.path.join('img', "Heart.png")), (50, 50)), (Hran2, 590))
        if HHigh2:
            pygame.draw.rect(screen, grey2, [Bx, By, Bl, Bl], 0)# home button
        else:
            pygame.draw.rect(screen, grey, [Bx, By, Bl, Bl], 0)# home button
        home_button = pygame.image.load(os.path.join('img', "home2.png")) # or use home.png
        screen.blit(home_button, [Bx, By])
    elif Learn:
        if HHigh2:
            pygame.draw.rect(screen, grey2, [Bx, By - 100, Bl, Bl], 0)# home button
        else:
            pygame.draw.rect(screen, grey, [Bx, By - 100, Bl, Bl], 0)# home button
        home_button = pygame.image.load(os.path.join('img', "home2.png")) # or use home.png
        screen.blit(home_button, [Bx, By - 100])
        LearnDoc = pygame.image.load(os.path.join('img', "LearnDoc.png"))
        screen.blit(LearnDoc, [100, 50 + 2.7 * (12 - Scroll)])
        pygame.draw.rect(screen, black, [0, 640, 1280, 20], 0)
        pygame.draw.rect(screen, black, [0, 0, 1280, 10], 0)
        pygame.draw.rect(screen, grey3, [1250, 10, 20, 630], 0) # scroll bar back
        pygame.draw.rect(screen, grey2, [1252, Scroll, 16, ScrollLen[0]], 0) # scroll bar
        if Scroll < 12:
            Scroll = 12
        if Scroll + ScrollLen[0] > 638:
            Scroll = 638 - ScrollLen[0]
    elif Sources:
        if HHigh2:
            pygame.draw.rect(screen, grey2, [Bx, By - 100, Bl, Bl], 0)# home button
        else:
            pygame.draw.rect(screen, grey, [Bx, By - 100, Bl, Bl], 0)# home button
        home_button = pygame.image.load(os.path.join('img', "home2.png")) # or use home.png
        screen.blit(home_button, [Bx, By - 100])
        SourcesDoc = pygame.image.load(os.path.join('img', "SourcesDoc.png"))
        screen.blit(SourcesDoc, [200, 50 + 1.5 * (12 - Scroll)])
        pygame.draw.rect(screen, black, [0, 640, 1280, 20], 0)
        pygame.draw.rect(screen, black, [0, 0, 1280, 10], 0)
        pygame.draw.rect(screen, grey3, [1250, 10, 20, 630], 0) # scroll bar back
        pygame.draw.rect(screen, grey2, [1252, Scroll, 16, ScrollLen[1]], 0) # scroll bar
        if Scroll < 12:
            Scroll = 12
        if Scroll + ScrollLen[1] > 638:
            Scroll = 638 - ScrollLen[1]
    else:
        screen.blit(pygame.image.load(os.path.join('img', 'PEBackground.png')), [10, 10])
        font2 = pygame.font.Font('freesansbold.ttf', 100)
        title2 = font2.render('Mental Health', True, white)
        title3 = font2.render('is not a Game', True, white)
        screen.blit(title2, (290, 65))
        screen.blit(title3, (300, 165))
        if HHigh:
            pygame.draw.rect(screen, grey2, [605, By1, 70, 70], 0) # play button highlight
        if LHigh:
            pygame.draw.rect(screen, grey2, [605, By2, 70, 70], 0) # Learn button highlight
        if SHigh:
            pygame.draw.rect(screen, grey2, [605, By3, 70, 70], 0) # Sources button highlight
        font = pygame.font.Font('freesansbold.ttf', 25)
        Play = font.render('Play', True, white)
        Learn2 = font.render('Learn', True, white)
        Sources2 = font.render('Sources', True, white)
        screen.blit(Play, (612, By1 - 25))
        screen.blit(Learn2, (604, By2 - 22))
        screen.blit(Sources2, (590, By3 - 22))
        play_button = pygame.image.load(os.path.join('img', "play.png"))
        screen.blit(play_button, [605, By1]) # play button symbol
        learn_button = pygame.image.load(os.path.join('img', "Learn.png"))
        screen.blit(learn_button, [610, By2 + 5]) # learn button symbol
        sources_button = pygame.image.load(os.path.join('img', "Sources.png"))
        screen.blit(sources_button, [610, By3 + 5]) # sources button symbol
        Brain = pygame.image.load(os.path.join('img', "Brain.png"))
        Heart = pygame.image.load(os.path.join('img', "Heart.png"))
        screen.blit(Brain, [50, 200]) # displays brain
        screen.blit(Heart, [1050, 200]) # displays heart

def directions():
    easygui.msgbox("A mental health disorder is about to be randomly chosen for you.", "How to Play:")
    easygui.msgbox("Your job is to select which of the three random choices at the bottom of the screen correctly correspond with the disorder.", "How to Play:")
    easygui.msgbox("If you choose the correct option, you will gain a point. Otherwise, a point will be deducted from your score.", "How to Play:")
    easygui.msgbox("If you do not know the answer, you can click the information button at the top right of the image representing the disorder.", "How to Play:")
    easygui.msgbox("You can also go to the Learn page on the home screen or just guess.", "How to Play:")
    easygui.msgbox("There are many different options that are randomly selected to be an answer choice. These options include: coping methods, facts, symptoms, and causes.", "How to Play:")
    easygui.msgbox("Once you finish, close the window with the x in the top right corner to get your score.", "How to Play:")

def StartImg():
    global ran, ran2, ran3, disorder, disorder2, Text, Text2, ShowDisorder, reran, movevar3, movevar2, otherdiv, addinterval, divinterval, timestop
    ran = random.randint(1, 8)
    ran2 = random.randint(35, 90)
    ShowDisorder = False
    for i in range(ran2):
        if ran == 1:
            Text = 'Anxiety'
            disorder = Anxiety1
            disorder2 = 0
        elif ran == 2:
            Text = 'PTSD'
            disorder = Ptsd1
            disorder2 = 1
        elif ran == 3:
            Text = 'Anorexia'
            disorder = Anorexia1
            disorder2 = 2
        elif ran == 4:
            Text = 'Bulimia'
            disorder = Bulimia1
            disorder2 = 3
        elif ran == 5:
            Text = 'Schizophrenia'
            disorder = Schizophrenia1
            disorder2 = 4
        elif ran == 6:
            Text = 'ADHD'
            disorder = Adhd1
            disorder2 = 5
        elif ran == 7:
            Text = 'Bipolar'
            disorder = Bipolar1
            disorder2 = 6
        elif ran == 8:
            Text = 'Depression'
            disorder = Depression1
            disorder2 = 7
        ran3 = random.randint(0, 2)
        background()
        font = pygame.font.Font('freesansbold.ttf', 35)
        Text2 = font.render(str(Text), True, white, grey)
        screen.blit(Text2, (530, SIHeight - 35))
        screen.blit(pygame.image.load(os.path.join('img', disorder[ran3])), [530, SIHeight])
        ran += 1
        if ran == 9:
            ran = 1
        pygame.display.flip()
        pygame.time.delay(50)
    ShowDisorder = True
    reran = True
    background()
        
def game():
    global ran, Bran, stop, Hran, Bran2, Hran2, move, move2, move3, reran, score, repeat, Again, rounds, wins, loses, Choice, Win, Lose, LoseT, WinT, RHigh, MHigh, LHigh
    font = pygame.font.Font('freesansbold.ttf', 50)
    if ranA != Choice:
        LoseT = font.render("You Lost a Point", True, red, grey)
        score -= 1
        loses += 1
        Lose = True
        background()
    else:
        WinT = font.render("You Got a Point!", True, green, grey)
        score += 1
        wins += 1
        Win = True
        background()
    Choice = ''
    pygame.display.flip()
    stop = True
    
def continue1():
    global ran, Bran, RHeight, MHeight, LHeight, stop, Hran, Bran2, Hran2, move, move2, move3, reran, score, repeat, Again, rounds, wins, loses, Choice, Win, Lose, LoseT, WinT, RHigh, MHigh, LHigh
    rounds += 1
    Bran = random.randint (1, 8) # random var that gives a small chance of brain appearing at bottom of screen
    Hran = random.randint (1, 10) # random var that gives a small chance of heart appearing at bottom of screen
    Bran2 = random.randint(0, 1230) # random x cordinate where the brain will appear
    Hran2 = random.randint(0, 1230) # random y cordinate where the heart will appear
    if Bran == 1 and Hran == 1: # this prevents the heart and brain from overlapping
        if Hran2 in range (Bran2 - 110, Bran2 + 60):
            if Bran2 >= 615:
                Hran2 = Bran2 - 230
            else:
                Hran2 = Bran2 + 300
    move3 = True
    reran = True
    Lose = False
    Win = False
    choose = False
    StartImg()
    RHeight = pygame.image.load(os.path.join('img', ranR[ranR2])).get_height()
    MHeight = pygame.image.load(os.path.join('img', ranM[ranM2])).get_height()
    LHeight = pygame.image.load(os.path.join('img', ranL[ranL2])).get_height()
    if pygame.mouse.get_pos()[0] < 230 - border or pygame.mouse.get_pos()[0] > 430 + border or pygame.mouse.get_pos()[1] < ACHeight - border or pygame.mouse.get_pos()[1] > RHeight + ACHeight + border:
        RHigh = False
    if pygame.mouse.get_pos()[0] < 530 - border or pygame.mouse.get_pos()[0] > 730 + border or pygame.mouse.get_pos()[1] < ACHeight - border or pygame.mouse.get_pos()[1] > MHeight + ACHeight + border:
        MHigh = False
    if pygame.mouse.get_pos()[0] < 830 - border or pygame.mouse.get_pos()[0] > 1030 + border or pygame.mouse.get_pos()[1] < ACHeight - border or pygame.mouse.get_pos()[1] > LHeight + ACHeight + border:
        LHigh = False
    background()
    choose = True
    Choice = ''
    stop = False

pygame.init()
pygame.display.set_caption("Mental Health is not a Game")
mousePos = pygame.mouse.get_pos()
pygame.key.set_repeat(250, 60)
background()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit1 = easygui.buttonbox("Are you sure you would like to quit?", choices = ["Yes", "No"])
            if quit1 == "Yes":
                running = False
        elif event.type == pygame.KEYDOWN:
            if Learn or Sources:
                if Learn:
                    SLvar = 0
                else:
                    SLvar = 1
                if Scroll >= 22:
                    if event.key == pygame.K_UP:
                        Scroll -= 10
                        background()
                if Scroll + ScrollLen[SLvar] <= 628:
                    if event.key == pygame.K_DOWN:
                        Scroll += 10
                        background()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if choose or Learn or Sources:
                mouse = True
            if stop:
                continue1()
            elif not home:
                if pygame.mouse.get_pos()[0] >= Bx and pygame.mouse.get_pos()[0] <= Bx + Bl and pygame.mouse.get_pos()[1] >= By and pygame.mouse.get_pos()[1] <= By + Bl:
                    home = True # home button
                    Learn = False
                    Sources = False
                    HHigh2 = False
                    background()
                if pygame.mouse.get_pos()[0] >= 710 and pygame.mouse.get_pos()[0] <= 730 and pygame.mouse.get_pos()[1] >= SIHeight and pygame.mouse.get_pos()[1] <= SIHeight + 20:
                    if Info:
                        Info = False
                    elif not Info:
                        Info = True
                    background()
                if pygame.mouse.get_pos()[0] >= 230 - border and pygame.mouse.get_pos()[0] <= 430 + border and pygame.mouse.get_pos()[1] >= ACHeight - border and pygame.mouse.get_pos()[1] <= RHeight + ACHeight + border:
                    Choice = 1
                elif pygame.mouse.get_pos()[0] >= 530 - border and pygame.mouse.get_pos()[0] <= 730 + border and pygame.mouse.get_pos()[1] >= ACHeight - border and pygame.mouse.get_pos()[1] <= MHeight + ACHeight + border:
                    Choice = 2
                elif pygame.mouse.get_pos()[0] >= 830 - border and pygame.mouse.get_pos()[0] <= 1030 + border and pygame.mouse.get_pos()[1] >= ACHeight - border and pygame.mouse.get_pos()[1] <= LHeight + ACHeight + border:
                    Choice = 3
                if Choice == 1 or Choice == 2 or Choice == 3:
                    Info = False
                    background()
                    game()
            elif Learn:
                if pygame.mouse.get_pos()[0] >= Bx and pygame.mouse.get_pos()[0] <= Bx + Bl and pygame.mouse.get_pos()[1] >= By - 100 and pygame.mouse.get_pos()[1] <= By + Bl - 100:
                    home = True # home button
                    Learn = False
                    Sources = False
                    HHigh2 = False
                    LHigh = False
                    Scroll = 12
                    background()
            elif Sources:
                if pygame.mouse.get_pos()[0] >= Bx and pygame.mouse.get_pos()[0] <= Bx + Bl and pygame.mouse.get_pos()[1] >= By - 100 and pygame.mouse.get_pos()[1] <= By + Bl - 100:
                    home = True # home button
                    Learn = False
                    Sources = False
                    HHigh2 = False
                    SHigh = False
                    Scroll = 12
                    background()
            else:
                if pygame.mouse.get_pos()[0] >= 605 and pygame.mouse.get_pos()[1] >= By1 and pygame.mouse.get_pos()[0] <= 675 and pygame.mouse.get_pos()[1] <= By1 + 70:
                    home = False # play button
                    HHigh = False
                    if First:
                        choose = False
                        background()
                        pygame.display.flip()
                        directions()
                        StartImg()
                        choose = True
                        First = False
                if pygame.mouse.get_pos()[0] >= 605 and pygame.mouse.get_pos()[1] >= By2 and pygame.mouse.get_pos()[0] <= 675 and pygame.mouse.get_pos()[1] <= By2 + 70:
                    Learn = True
                if pygame.mouse.get_pos()[0] >= 605 and pygame.mouse.get_pos()[1] >= By3 and pygame.mouse.get_pos()[0] <= 675 and pygame.mouse.get_pos()[1] <= By3 + 70:
                    Sources = True
                background()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = False
        elif event.type == pygame.MOUSEMOTION:
            if Learn or Sources:
                if Learn:
                    SLvar = 0
                else:
                    SLvar = 1
                if mouse:
                    if pygame.mouse.get_pos()[0] >= 1252 and pygame.mouse.get_pos()[0] <= 1268 and pygame.mouse.get_pos()[1] >= Scroll and pygame.mouse.get_pos()[1] <= Scroll + ScrollLen[SLvar]:
                        if ((pygame.mouse.get_pos()[1] - mousePos[1]) < 0 and Scroll >= 12) or ((pygame.mouse.get_pos()[1] - mousePos[1]) > 0 and Scroll + ScrollLen[SLvar] <= 638):
                            Scroll += pygame.mouse.get_pos()[1] - mousePos[1]
                            mousePos = pygame.mouse.get_pos()
                            background()
                else:
                    if pygame.mouse.get_pos()[0] >= 1252 and pygame.mouse.get_pos()[0] <= 1268 and pygame.mouse.get_pos()[1] >= Scroll and pygame.mouse.get_pos()[1] <= Scroll + ScrollLen[SLvar]:
                        mousePos = pygame.mouse.get_pos()
            if not home:
                if not Win and not Lose:
                    if pygame.mouse.get_pos()[0] >= Bx and pygame.mouse.get_pos()[0] <= Bx + Bl and pygame.mouse.get_pos()[1] >= By and pygame.mouse.get_pos()[1] <= By + Bl:
                        HHigh2 = True
                    else:
                        HHigh2 = False
                    if pygame.mouse.get_pos()[0] >= 710 and pygame.mouse.get_pos()[0] <= 730 and pygame.mouse.get_pos()[1] >= SIHeight and pygame.mouse.get_pos()[1] <= SIHeight + 20:
                        IHigh = True
                    else:
                        IHigh = False
                    background()
                    if ShowDisorder:
                        if pygame.mouse.get_pos()[0] >= 230 - border and pygame.mouse.get_pos()[0] <= 430 + border and pygame.mouse.get_pos()[1] >= ACHeight - border and pygame.mouse.get_pos()[1] <= RHeight + ACHeight + border:
                            RHigh = True
                        else:
                            RHigh = False
                        if pygame.mouse.get_pos()[0] >= 530 - border and pygame.mouse.get_pos()[0] <= 730 + border and pygame.mouse.get_pos()[1] >= ACHeight - border and pygame.mouse.get_pos()[1] <= MHeight + ACHeight + border:
                            MHigh = True
                        else:
                            MHigh = False
                        if pygame.mouse.get_pos()[0] >= 830 - border and pygame.mouse.get_pos()[0] <= 1030 + border and pygame.mouse.get_pos()[1] >= ACHeight - border and pygame.mouse.get_pos()[1] <= LHeight + ACHeight + border:
                            LHigh = True
                        else:
                            LHigh = False
                        background()
            elif Learn:
                if pygame.mouse.get_pos()[0] >= Bx and pygame.mouse.get_pos()[0] <= Bx + Bl and pygame.mouse.get_pos()[1] >= By - 100 and pygame.mouse.get_pos()[1] <= By + Bl - 100:
                    HHigh2 = True
                else:
                    HHigh2 = False
                background()
            elif Sources:
                if pygame.mouse.get_pos()[0] >= Bx and pygame.mouse.get_pos()[0] <= Bx + Bl and pygame.mouse.get_pos()[1] >= By - 100 and pygame.mouse.get_pos()[1] <= By + Bl - 100:
                    HHigh2 = True
                else:
                    HHigh2 = False
                background()
            else:
                if pygame.mouse.get_pos()[0] >= 605 and pygame.mouse.get_pos()[1] >= By1 and pygame.mouse.get_pos()[0] <= 675 and pygame.mouse.get_pos()[1] <= 410:
                    HHigh = True
                else:
                    HHigh = False
                if pygame.mouse.get_pos()[0] >= 605 and pygame.mouse.get_pos()[1] >= By2 and pygame.mouse.get_pos()[0] <= 675 and pygame.mouse.get_pos()[1] <= By2 + 70:
                    LHigh = True
                else:
                    LHigh = False
                if pygame.mouse.get_pos()[0] >= 605 and pygame.mouse.get_pos()[1] >= By3 and pygame.mouse.get_pos()[0] <= 675 and pygame.mouse.get_pos()[1] <= By3 + 70:
                    SHigh = True
                else:
                    SHigh = False
                background()
        pygame.display.flip()
if not Win and not Lose:
    rounds -= 1
if rounds == 0 or rounds >= 2:
    if score == 0 or score <= -2 or score >= 2:
        easygui.msgbox("You got %s points in %s rounds!" %(score, rounds))
    else:
        easygui.msgbox("You got %s point in %s rounds!" %(score, rounds))
else:
    if score == 0 or score <= -2 or score >= 2:
        easygui.msgbox("You got %s points in %s round!" %(score, rounds))
    else:
        easygui.msgbox("You got %s point in %s round!" %(score, rounds))
pygame.quit()
quit()


