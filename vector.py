import turtle as t

print("벡터 연산")
mode = int(input('합: 0 | 차: 1  '))

t.shape('turtle')

t.speed(0)
t.penup()
t.goto(0, 350)
t.pendown()
t.goto(0, -350)
t.penup()
t.goto(-350, 0)
t.pendown()
t.goto(350, 0)
t.penup()

print('좌표 찍기 모드')
mmode=input('마우스: 0 | 콘솔: 1  ')

t.speed(50)

vector1 = [None, None, None, None] #초점x , 초점y , 종잠 x, 종점y
vector2 = [None, None, None, None]

def plusVector(x, y):
    if vector1[0] is None or vector1[1] is None:
        vector1[0] = x
        vector1[1] = y

        t.goto(x, y)
        label(x, y)
    elif vector1[2] is None or vector1[3] is None:
        vector1[2] = x
        vector1[3] = y

        t.pendown()
        t.pencolor("red")
        t.goto(x, y)
        t.penup()

        label(x, y)

        vector2[0] = vector1[2]
        vector2[1] = vector1[3]
    else:
        vector2[2] = x
        vector2[3] = y

        t.pendown()
        t.pencolor("blue")
        t.goto(x, y)
        t.penup()

        label(x, y)

        t.goto(vector1[0], vector1[1])
        t.pendown()
        t.pencolor("purple")
        t.goto(vector2[2], vector2[3])
        t.penup()

        label(vector2[2], vector2[3])

        for i in range(4):
            vector1[i] = None
            vector2[i] = None

def minusVector(x, y):
    if vector1[0] is None or vector1[1] is None:
        vector1[0] = x
        vector1[1] = y

        t.goto(x, y)
        label(x, y)

        vector2[0] = vector1[0]
        vector2[1] = vector1[1]
    elif vector1[2] is None or vector1[3] is None:
        vector1[2] = x
        vector1[3] = y

        t.pendown()
        t.pencolor("red")
        t.goto(x, y)
        t.penup()

        label(x, y)
    else:
        vector2[2] = x
        vector2[3] = y

        t.goto(vector1[0], vector1[1])
        t.pendown()
        t.pencolor("blue")
        t.goto(x, y)
        t.penup()

        label(x, y)

        t.goto(vector2[2], vector2[3])
        t.pendown()
        t.pencolor("purple")
        t.goto(vector1[2], vector1[3])
        t.penup()

        label(vector1[2], vector1[3])

        for i in range(4):
            vector1[i] = None
            vector2[i] = None


def label(x, y):
    t.goto(x + 5, y + 5)
    t.write(f"({int(x)}, {int(y)})", font=("Arial", 10, "normal"))
    t.goto(x, y)

def draw(x, y):
    t.color('black')
    try:
        if mode == 0:
            plusVector(x, y)
        elif mode == 1:
            minusVector(x, y)
    except:
        print("SOMETHING WRONG")

if mmode=='1':
    v1 = list(map(int, input(f'벡터 1의 초점 입력: ').split(' ')))
    draw(v1[0], v1[1])
    v2 = list(map(int, input(f'벡터 1의 종점 입력: ').split(' ')))
    draw(v2[0], v2[1])
    v3 = list(map(int, input(f'벡터 2의 초점 입력: ').split(' ')))
    draw(v3[0], v3[1])
    t.done()
else:
    t.onscreenclick(draw)
    t.done()
