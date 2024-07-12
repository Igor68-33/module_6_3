class Horse:
    """Horse - класс описывающий лошадь.
    атрибуты:
    x_distance = 0 - пройденный путь.
    sound = 'Frrr' - звук, который издаёт лошадь.
    методы:
    run(self, dx), где  dx - изменение дистанции, увеличивает
    x_distance на dx."""

    x_distance = 0

    sound = 'Frrr'  # Если Eagle.sound не в init, то Horse.sound-> Pegasus

    # def __init__(self): # Если Horse.sound в init, то Horse.sound-> Pegasus
    #     self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    """
    класс описывающий орла.
    атрибуты:
    y_distance = 0 - высота полёта
    sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
    методы:
    fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy."""

    y_distance = 0

    # sound = 'I train, eat, sleep, and repeat'

    def __init__(self):  # Если Horse.sound не в init, то Eagle.sound->Pegasus
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    """
    класс описывающий пегаса.
    методs:
    move(self, dx, dy) - где dx и dy изменения дистанции.
    В этом методе должны запускаться наследованные методы run и fly соответственно.
    get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance).
    voice - который печатает значение унаследованного атрибута sound."""

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# Вывод на консоль:
# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat
