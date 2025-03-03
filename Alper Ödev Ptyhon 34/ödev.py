import turtle

def draw_shape(choice):
    screen = turtle.Screen()
    screen.title("Şekil Çizim Uygulaması")
    t = turtle.Turtle()
    t.speed(3)

    if choice == 'A':
        # Sol üst üçgen
        t.begin_fill()
        t.goto(-100, 100)
        t.goto(0, 0)
        t.goto(-100, 0)
        t.goto(-100, 100)
        t.end_fill()
    elif choice == 'B':
        # Sağ üst üçgen
        t.begin_fill()
        t.goto(100, 100)
        t.goto(0, 0)
        t.goto(100, 0)
        t.goto(100, 100)
        t.end_fill()
    elif choice == 'C':
        # Sağ alt üçgen
        t.begin_fill()
        t.goto(100, -100)
        t.goto(0, 0)
        t.goto(100, 0)
        t.goto(100, -100)
        t.end_fill()
    elif choice == 'D':
        # Sol alt üçgen
        t.begin_fill()
        t.goto(-100, -100)
        t.goto(0, 0)
        t.goto(-100, 0)
        t.goto(-100, -100)
        t.end_fill()
    elif choice == 'E':
        # Çapraz X şeklinde (dört üçgen doldurulmuş)
        t.begin_fill()
        t.goto(-100, 100)
        t.goto(0, 0)
        t.goto(-100, 0)
        t.goto(-100, 100)
        t.end_fill()

        t.begin_fill()
        t.goto(100, 100)
        t.goto(0, 0)
        t.goto(100, 0)
        t.goto(100, 100)
        t.end_fill()

        t.begin_fill()
        t.goto(-100, -100)
        t.goto(0, 0)
        t.goto(-100, 0)
        t.goto(-100, -100)
        t.end_fill()

        t.begin_fill()
        t.goto(100, -100)
        t.goto(0, 0)
        t.goto(100, 0)
        t.goto(100, -100)
        t.end_fill()
    else:
        print("Geçersiz seçim yaptınız!")

    screen.mainloop()

# Kullanıcıdan seçim alma
print("Şekil Seçim Menüsü:")
print("A: Sol üst üçgen")
print("B: Sağ üst üçgen")
print("C: Sağ alt üçgen")
print("D: Sol alt üçgen")
print("E: Çapraz X şekli")

choice = input("Çizmek istediğiniz şekli seçin (A, B, C, D, E): ").upper()
draw_shape(choice)