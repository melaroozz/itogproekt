y=300
x=450
r1=random(860)
r2=random(560)
w=40
w1=40
k=0
j=59
p=0
s=43
def setup():
    size(900,600)
def draw():
    global y,x,r1,r2,w,w1,k,j,p,s
    background('#FFFFFF')
    l=loadImage('1.png')
    image(l,r1,r2,40,40)
    fill(0)
    ellipse(x,y,w,w)
    fill(100)
    textSize(30)
    text("00:",800,40)
    text(j,847,40)
    text(u"Очки: ",0,40)
    text(p,100,40)
    text("/86",135,40)
    if keyPressed==True:
        if key=='w':
            y=y-s
        if y<=0:
            y=599
        if key=='s':
            y=y+s
        if y>=600:
            y=1
        if key=='a':
            x=x-s
        if x<=0:
            x=899
        if key=='d':
            x=x+s
        if x>=900:
            x=1
        if x>r1-w//2 and x<r1+40+w//2 and y>r2-w//2 and y<r2+40+w//2:
            r1=random (860)
            r2=random (560)
            w=w+10
            p+=1
            s-=0.5
        if w>=900:
            background (0)
            textSize (100)
            textMode (CENTER)
            textAlign(CENTER)
            fill(255)
            text(u'Вы выиграли!',450,300)
            text(u"Вы пельмень на 100%",300,450)
            noLoop()
    k+=1
    if k==60:
        k=k*0
        j-=1
    if j==0:
        background (0)
        textSize (80)
        textMode (CENTER)
        textAlign(CENTER)
        fill(255)
        text(u'Вы проиграли :(',450,300)
        text(u"Вы пельмень на:",400,400)
        text(p+14,760,400)
        text("%",870,400)
        noLoop()
