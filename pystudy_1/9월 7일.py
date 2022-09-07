#구문오류
#코드에 문제가 있음
print(실행안됨)
#예외 런타임 오류
list_a = [1,2,3]


string_input = input("정수 입력> ")
if string_input.isdigit():
    number_input_a = int(string_input)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력해주세요!")


    try:
        print(float(input("> 숫자를 입력해주세요: ")) ** 2)
        break
except:
    print("숫자를 입력해주세요")


list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구무의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")
test()


students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 87, "math": 98, "english": 88, "science": 90},
    {"name": "나선주", "korean": 87, "math": 98, "english": 88, "science": 92},
    {"name": "신재용", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤인성", "korean": 64, "math": 88, "english": 92, "science": 92},
]

print("이름", "총점", "평균", sep="\t")


class Student:
    def __init__(self):
        print("객체가 생성되었습니다.")
    def __del__(self):
        print("객체가 소멸되었습니다.")
    def 출력(self):
        print(self.이름, self.나이)

student = Student("신재용", 3)
