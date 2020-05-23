class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable,Unit ):
    def __init__(self):
        # super().__init__() # 다중상속 시 마지막 상속 클래스만 호출됨
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()