dictionary = {
    "사이다": 1700,
    "콜라": 1900,
    "식혜": 2500,
    "솔의눈": 3000
    }

for key, value in dictionary.items():
    print(key, value)

food = input("구매할 음료를 적어주세요")

for key, value in dictionary.items():
    if key == food:
        money = int(input("돈을 넣어주세요"))
        if money >= value:
            print("구매를 완료하였습니다.")
            print("잔액 : ",(money-value))
        else:
            print("돈이 부족합니다.")