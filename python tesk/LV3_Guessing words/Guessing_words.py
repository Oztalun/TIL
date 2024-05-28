import random

Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

word = [
    "airplane",
    "apple",
    "arm",
    "bakery",
    "banana",
    "bank",
    "bean",
    "belt",
    "bicycle",
    "biography",
    "blackboard",
    "boat",
    "bowl",
    "broccoli",
    "bus",
    "car",
    "carrot",
    "chair",
    "cherry",
    "cinema",
    "class",
    "classroom",
    "cloud",
    "coat",
    "cucumber",
    "desk",
    "dictionary",
    "dress",
    "ear",
    "eye",
    "fog",
    "foot",
    "fork",
    "fruits",
    "hail",
    "hand",
    "head",
    "helicopter",
    "hospital",
    "ice",
    "jacket",
    "kettle",
    "knife",
    "leg",
    "lettuce",
    "library",
    "magazine",
    "mango",
    "melon",
    "motorcycle",
    "mouth",
    "newspaper",
    "nose",
    "notebook",
    "novel",
    "onion",
    "orange",
    "peach",
    "pharmacy",
    "pineapple",
    "plate",
    "pot",
    "potato",
    "rain",
    "shirt",
    "shoe",
    "shop",
    "sink",
    "skateboard",
    "ski",
    "skirt",
    "sky",
    "snow",
    "sock",
    "spinach",
    "spoon",
    "stationary",
    "stomach",
    "strawberry",
    "student",
    "sun",
    "supermarket",
    "sweater",
    "teacher",
    "thunderstorm",
    "tomato",
    "trousers",
    "truck",
    "vegetables",
    "vehicles",
    "watermelon",
    "wind"
]
#정답 선정
answer = list(word[random.randint(0, 92)])
chance = 9
#정답 빈칸제작
submit = []
for i in range(0, len(answer)):
    submit.append("_")

#시작
while chance>0 and answer != submit:
    b = 0#알파벳 정답 유무
    count = 0
    print("현재 남은 기회 : ", chance)
    print(submit)#빈칸
    print(Alphabet)#알파벳/ 사용한 알파벳 제거
    a = input("단어를 입력해주세요 : ")
    if not a.encode().isalpha():
        print("영어를 입력하세요")
    elif len(a)>1:
        print("!!경고!! 한개의 알파벳만 입력하세요")
    else:
        # 사용한 알파벳 제거
        for i, value in enumerate(Alphabet):
            if a == value:
                Alphabet[i] = "_"
        for i, value in enumerate(answer):
            if value == a:
                submit[i] = a
                b = 1
        if b == 1:
            print("맞았습니다")
        else:
            print("정답에 포함된 알파벳이 아닙니다. 기회가 차감됩니다.")
            chance -= 1
        print("")
if answer == submit:
    print("정답입니다! ", submit)
else:
    print("기회를 모두 소진했습니다")
    print("정답은 ",answer,"였습니다!")