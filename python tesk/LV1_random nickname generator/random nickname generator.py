import random

firstname = ("기절초풍", "멋있는", "재미있는")
secondname = ("도전적인", "노란색의", "바보같은")
thirdname = ("돌고래", "개발자", "오랑우탄")

def generate_random_nickname():
    generated_name = firstname[random.randint(0, 2)]+secondname[random.randint(0, 2)]+thirdname[random.randint(0, 2)]
    return generated_name

my_nickname = generate_random_nickname()
print(my_nickname)
my_nickname = generate_random_nickname()
print(my_nickname)
my_nickname = generate_random_nickname()
print(my_nickname)
my_nickname = generate_random_nickname()
print(my_nickname)