from django.db import models


# Create your models here.
class Cat:
    cats = []

    def __init__(self, name: str):
        self.name = name.capitalize()
        self.age = 1
        self.satiety = 40
        self.happiness = 40
        self.is_asleep = False
        self.state = ""
        self.cats.append(self)

    @staticmethod
    def play(cat_b):
        from random import randint
        if cat_b.is_asleep:
            cat_b.is_asleep = False
            cat_b.happiness -= 5
        else:
            if randint(1, 3) == 1:
                cat_b.satiety = 0
            else:
                cat_b.happiness += 15
                cat_b.satiety -= 10

    @staticmethod
    def feed(cat_b):
        if cat_b.is_asleep:
            pass
        else:
            if cat_b.satiety < 100:
                cat_b.satiety += 15
                cat_b.happiness += 5
                if cat_b.happiness >= 100:
                    cat_b.happiness = 100
            else:
                cat_b.satiety = 100
                cat_b.happiness -= 30
                if cat_b.happiness < 0:
                    cat_b.happiness = 0

    @staticmethod
    def put_to_sleep(cat_b):
        if cat_b.is_asleep:
            cat_b.is_asleep = False
        else:
            cat_b.is_asleep = True
