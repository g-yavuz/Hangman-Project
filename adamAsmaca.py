import turtle

class AdamAsmaca:
    def __init__(self, width_, height_):
        self.ekran = turtle.Screen()
        self.ekran.title("Adam Asmaca Oyunu")
        self.ekran.bgcolor("lightblue")
        self.ekran.setup(width=width_, height=height_)

        self.kalem = turtle.Turtle()
        self.kalem.shape("turtle")
        self.kalem.color("black")
        self.kalem.pensize(3)
        self.kalem.speed(5)
        self.cizim_asamasi = 0

        self.yazi_kalemi = turtle.Turtle()
        self.yazi_kalemi.hideturtle()
        self.yazi_kalemi.penup()
        self.yazi_kalemi.goto(-200, 250)
        self.yazi_kalemi.color("black")

    def gülen_yüz(self):
        
        self.kalem.clear()  
        self.kalem.penup()  
        self.kalem.goto(0, 0) 
        
        self.kalem.penup()
        self.kalem.goto(0, -100) 
        self.kalem.pendown()
        self.kalem.color("yellow")
        self.kalem.begin_fill()
        self.kalem.circle(100) 
        self.kalem.end_fill()

        
        self.kalem.penup()
        self.kalem.goto(-40, 40)  
        self.kalem.pendown()
        self.kalem.color("black")
        self.kalem.begin_fill()
        self.kalem.circle(10)
        self.kalem.end_fill()

        self.kalem.penup()
        self.kalem.goto(40, 40) 
        self.kalem.pendown()
        self.kalem.color("black")
        self.kalem.begin_fill()
        self.kalem.circle(10)  
        self.kalem.end_fill()

        # Ağzı çiz
        self.kalem.penup()
        self.kalem.goto(-40, -20)
        self.kalem.pendown()
        self.kalem.setheading(-60)  
        self.kalem.circle(50, 120) 

    def kafa(self):
        self.kalem.penup()
        self.kalem.goto(0, -50)
        self.kalem.left(90)
        self.kalem.pendown()
        self.kalem.circle(30)
        return self.kalem.position()

    def gövde(self):
        self.kalem.penup()
        self.kalem.goto(0, -50)
        self.kalem.pendown()
        self.kalem.left(90)
        self.kalem.backward(100)

    def bacak_right(self):
        self.kalem.penup()
        self.kalem.goto(0, -150)
        self.kalem.pendown()
        self.kalem.left(45)
        self.kalem.backward(50)

    def bacak_left(self):
        self.kalem.penup()
        self.kalem.goto(0, -150)
        self.kalem.pendown()
        self.kalem.right(90)
        self.kalem.backward(50)

    def kol_right(self):
        self.kalem.penup()
        self.kalem.goto(0, -100)
        self.kalem.pendown()
        self.kalem.right(45)
        self.kalem.forward(50)

    def kol_left(self):
        self.kalem.penup()
        self.kalem.goto(0, -100)
        self.kalem.pendown()
        self.kalem.left(180)
        self.kalem.forward(50)

    def stage(self):
        self.kalem.penup()
        self.kalem.goto(-100, -250)
        self.kalem.pendown()
        self.kalem.right(180)
        self.kalem.forward(200)
        self.kalem.left(180)

    def stage_1(self):
        self.kalem.penup()
        self.kalem.goto(-200, -250)
        self.kalem.left(90)
        self.kalem.pendown()
        self.kalem.forward(300)
        self.kalem.right(90)

    def stage_2(self):
        self.kalem.penup()
        self.kalem.pendown()
        self.kalem.forward(250)

    def stage_3(self):
        self.kalem.penup()
        self.kalem.goto(-200, -150)
        self.kalem.left(45)
        self.kalem.pendown()
        self.kalem.forward(280)
        return self.kalem.position()

    def stage_4(self,):
        self.kalem.penup()
        self.kalem.goto(0,50)
        self.kalem.right(135)
        self.kalem.pendown()
        self.kalem.forward(40)

    def kilic(self,):
        self.kalem.penup()
        self.kalem.goto(0,-50)  
        self.kalem.color("red")
        self.kalem.pendown()


        self.kalem.forward(50)
        self.kalem.backward(100) 

    def ilerlet(self):
        cizim_fonksiyonlari = [self.stage, self.stage_1, self.stage_2, self.stage_3, self.stage_4,self.kafa, self.gövde, self.bacak_left, self.bacak_right, self.kol_left,self.kol_right, self.kilic]
        if self.cizim_asamasi < len(cizim_fonksiyonlari):
            cizim_fonksiyonlari[self.cizim_asamasi]()
            self.cizim_asamasi += 1
    
    def yaziyi_guncelle(self, mesaj):
        self.yazi_kalemi.clear()
        self.yazi_kalemi.write(mesaj, align="left", font=("Arial", 16, "normal"))

def oyun_baslat():
    game = AdamAsmaca(600, 600)

    kelime = turtle.textinput("Kelime Seçimi", "Yönetici lütfen bir kelime seçsin:").lower()
    gizli_kelime = "_," * len(kelime)
    oyun_durumu = True
    yanlis_tahminler = 0
    max_yanlis = 12
    tahmin_edilenler = set()
    
    game.yaziyi_guncelle("Adam Asmaca Oyununa Hoş Geldiniz!\nKelimeyi tahmin etmeye çalışın: " + gizli_kelime)

    while oyun_durumu:
        tahmin = turtle.textinput("Harf Tahmini", "Bir harf tahmin edin (küçük harf):").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            game.yaziyi_guncelle("Lütfen sadece bir harf girin.")
            continue

        elif tahmin in tahmin_edilenler:
            game.yaziyi_guncelle("Bu harfi zaten tahmin ettiniz.")
            continue
        
        tahmin_edilenler.add(tahmin)

        if tahmin in kelime:
            gizli_kelimeyi_güncelle = ""
            for i in range(len(kelime)):
                if kelime[i] == tahmin:
                    gizli_kelimeyi_güncelle += tahmin
                else:
                    gizli_kelimeyi_güncelle += gizli_kelime[i]
            gizli_kelime = gizli_kelimeyi_güncelle
            game.yaziyi_guncelle("Doğru tahmin! Kelime: " + gizli_kelime)
        else:
            yanlis_tahminler += 1
            game.ilerlet()
            game.yaziyi_guncelle(f"Yanlış tahmin! {max_yanlis - yanlis_tahminler} hakkınız kaldı.\nKelime: {gizli_kelime}")

        if "_" not in gizli_kelime and "," not in gizli_kelime:
            game.yaziyi_guncelle("Tebrikler, kelimeyi doğru tahmin ettiniz!\nKelime: " + gizli_kelime)
            game.gülen_yüz()
            oyun_durumu = False

        elif yanlis_tahminler >= max_yanlis:
            game.yaziyi_guncelle(f"Oyunu kaybettiniz! Kelime: {kelime}")
            turtle.exitonclick()  
            oyun_durumu = False

oyun_baslat()

turtle.done()