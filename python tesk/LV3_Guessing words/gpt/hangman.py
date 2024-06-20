import random

words = [
    "airplane", "apple", "arm", "bakery", "banana", "bank", "bean", "belt",
    "bicycle", "biography", "blackboard", "boat", "bowl", "broccoli", "bus",
    "car", "carrot", "chair", "cherry", "cinema", "class", "classroom",
    "cloud", "coat", "cucumber", "desk", "dictionary", "dress", "ear", "eye",
    "fog", "foot", "fork", "fruits", "hail", "hand", "head", "helicopter",
    "hospital", "ice", "jacket", "kettle", "knife", "leg", "lettuce", "library",
    "magazine", "mango", "melon", "motorcycle", "mouth", "newspaper", "nose",
    "notebook", "novel", "onion", "orange", "peach", "pharmacy", "pineapple",
    "plate", "pot", "potato", "rain", "shirt", "shoe", "shop", "sink",
    "skateboard", "ski", "skirt", "sky", "snow", "sock", "spinach", "spoon",
    "stationery", "stomach", "strawberry", "student", "sun", "supermarket",
    "sweater", "teacher", "thunderstorm", "tomato", "trousers", "truck",
    "vegetables", "vehicles", "watermelon", "wind"
]


def initialize_game(words):
    answer = list(random.choice(words))
    submit = ["_"] * len(answer)
    chances = 9
    used_alphabets = []
    return answer, submit, chances, used_alphabets


def check_guess(answer, submit, guess):
    is_correct = False
    for i, char in enumerate(answer):
        if char == guess:
            submit[i] = guess
            is_correct = True
    return is_correct, submit


def update_game_state(answer, submit, chances, used_alphabets, guess):
    if guess in used_alphabets:
        return chances, '이미 사용한 알파벳입니다.', False

    used_alphabets.append(guess)
    is_correct, submit = check_guess(answer, submit, guess)

    if not is_correct:
        chances -= 1

    game_over = chances == 0 or submit == answer
    message = '맞았습니다!' if is_correct else '정답에 포함된 알파벳이 아닙니다. 기회가 차감됩니다.'

    return chances, message, game_over
