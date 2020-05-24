# import random
#
# print("나는 %s살입니다" %20)
# print("나는 %s에 다니고, %s년차 입니다" % ("???", 1))
#
# print(random.randint(9,44))
#
# print(round(3,3434))
# a = "1234567890"
# print(a[0:3])
#
# print("나는{}살입니다.".format(20))
# # print("내는{}살이고, {}대표입니다.".format("31","강소기업"))
# print("내는{1}살이고, {0}대표입니다.".format("31","강소기업"))
#
# print("내는{age}살이고, {name}대표입니다.".format(age = 31,name = "강소기업"))
#
# age = 20
# name = "초강소기업"
# print(f"나는 {age}살이며, {name}대표 입니다")
#
# print("백문이 불여일견 \n 백견이 불여일타")
# print("저는 '사장님' 입니다")
# print('''저는 "사장님" 입니다''')
# print("저는 \\사장님\\입니더")
#
#
# # 이스케이프 문자
# print("Red Apple\rPine")
# print("Redd\bAppple")
# print("Red\tapple")
# print("ddd")
#
#
# 주석 키가 안먹힐 때 ctrl + shift 눌러주면 된다
#
# url_1 = "https://naver.com"
# url_2 = (url_1[8:])
# print(url_2)
# url_3 = url_2[:-4]
# print(url_3)
#
# password = str(url_3[:3]) + str(len(url_3)) + str(url_2.count('e')) + "!"
# print("생성된 비밀번호 : " + password)
#
# url = "https://naver.com"
# my_str = url.replace("https://","") # 규칙1
# print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2
# print(my_str)
#
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
# print("'{0}' 의 비밀번호는 {1} 입니다.".format(url, password))
#
#
# def open_accouint():
#     print("계좌가 개설되었습니다.")
#
# open_accouint()
#
# def deposite(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance + money))
#     return balance + money
#
# def withdraw(balance, money): # 출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다".format(balance))
#         return balance
# def withdraw_night(balance, money):# 저녁에 출금
#     commission = 100 #수수료 100원
#     return commission, balance - money - commission
#
#
# balance = 0
# balance = deposite(balance, 1000)
# # balance = withdraw(balance, 2000)
# balance = withdraw(balance, 200)
#
# commission, balance = withdraw_night(balance, 500)
# print("수수료{0} 원이며, 잔액은 {1} 원입니다.".format(commission,balance))
#
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}"\
#           .format(name, age, main_lang))
#
# profile("김종혁",30,"파이썬")
#
# def profile(name, age = 17, main_lang="파이썬"): # 기본값
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}".format(name, age, main_lang))
#
# profile("김선민")
#
#
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
#
# profile(name="유재석", main_lang="파이썬", age=20)
#
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age, end=" "))
#     print(lang1, lang2, lang3, lang4, lang5)
#
# profile("유재석", 20, "파이썬", "자바", "C", "C#","C++")
# profile("김태호",20, "코틀린", "스위프트", "","","")
#
# def profile(name, age, *language): #가변인자
#     print("이름 : {0}\t나이 : {1}\t".format(name, age, end=" "))
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
# profile("유재석", 20, "파이썬", "자바", "C", "C#","C++","비쥬얼베이직")
#
# gun = 10
#
# def checkpoint(soldiers):
#     global gun # 전역변수 (권장되는 방법은 아님)
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}",format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun # 중요!!!
#
# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))
# '''2:54: 09 퀴즈 풀기'''
#
#
# import sys #????
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)
#
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#
#
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))
#
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다")
# print(type(answer))
#
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))
# print("{0: >10}".format(-500))
#
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 세자리 마다 콤마 찍기
# print("{0:,}".format(209874905872904875092874095872094837509))
#
# print("{0:+,}".format(-20745098729048750928479058270948570928475092874905))
#
# # 세자리 마다 콤마, 부호, 자릿수(30) 확보, 빈자리는 ^표시
# print("{0:^<+30,}".format(1987430987190384091873098471093))
#
# # #소숫점 출력
# print("{0:f}".format(6/7))
# #소숫점 자리 지정
# print("{0:.2f}".format(6/7))
#
#
# ### 파일 입출력 ###
#
#
# score_file = open("score.txt","w",encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
#
# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 100")
# score_file.write("\n공학 : 200")
#
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()
#
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# score_file.close()
#
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if line:
#         print(line)
#     if not line:
#         break
# score_file.close()
#
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end=" ")
# score_file.close()
#
# score_file = open("score.txt","r",encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end = " ")
# score_file.close()
#
#
# ### 피클
#
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수","나이":"30","취미":["축","골","코"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 파일에 저장
# profile_file.close()
#
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()
#
# ### with
#
# import pickle
#
# with open("profile.pickle", "rb") as profile_file:
#     print((pickle.load(profile_file)))
#
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중")
#
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())
#
#
#
# for i in range(1,51):
#    with open(str(i) + "주차.txt", "w", encoding="utf8") as weekly_report:
#         weekly_report.write( "-" + str(i) + "주차 주간보고-\n부서 : \n이름 : \n업무요약 : ")
#
#
# for i in range(1,4):
#     with open(str(i) + "주차 보고서.txt", "w", encoding="utf8") as weekly_report:
#         weekly_report.write("-{0} 주차 주간보고 -".format(i))
#         weekly_report.write("\n부서 : ")
#         weekly_report.write("\n이름 : ")
#         weekly_report.write("\n업무 요약: ")
#
# with open("1주차 보고서.txt", "r", encoding="utf8") as qwer:
#     print(qwer.read())
#
# ## 클래스 - 중요개념
#
# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# #
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
#
#
# marine3 = Unit("마린", 40, 4)
#
#
# ## 멤버변수
#
# 레이스 : 공주유 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
#
# wraith1 = Unit("레이스", 60 , 2)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#
# 마인드 컴트롤 : 상대방 유닛을 내 것으로 만드는 것 (뺴앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.cㅡlocking = True
#
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
#
# # 메쏘드
#
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]"\
#         .format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print(("{0} : 파괴되었습니다.".format(self.name)))
# #
#
# firebat1 = AttackUnit("파뱃", 50, 16)
# firebat1.attack("5시")
#
#
# firebat1.damaged(25)
# firebat1.damaged(25)
#
# ##상속
#
# # 메딕 : 의무병, 체력 회복, 공격력 0

from random import *



class Unit:
    def __init__(self,name,hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(("{0} 유닛이 생성되었습니다.".format(name)))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2} ]"\
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print(("{0} : 파괴되었습니다.".format(self.name)))


 ## 격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]"\
            .format(self.name, location, self.damage))

    # def damaged(self, damage):
    #     print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
    #     self.hp -= damage
    #     print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
    #     if self.hp <= 0:
    #         print(("{0} : 파괴되었습니다.".format(self.name)))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 징렂ㅇ 시간동안 이동 및 공격 속도를 증가, 체력 10 감소

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다 (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용 할 수 없습니다.".format(self.name))

## 탱크

class Tank(AttackUnit):
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

## 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동불가.
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

    # 현재 히즈모드가 아닐 때
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드 일때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False





# firebat1 = AttackUnit("파뱃", 50, 16)
# firebat1.attack("7시")
# firebat1.damaged(25)
# firebat1.damaged(25)

## 다중상속

# 드랍쉽, 공중유닛, 수송유닛, 공격하지 않음.

class Flyable: # 날 수 있는 기능을 가진 클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloked = False

    def clocking(self):
        if self.cloked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloked = False
        else:
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.cloked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Plyar] 님이 게임에서 퇴장하셨습니다.")



# game_start()
#
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
#
# t1 = Tank()
# t2 = Tank()
#
# w1 = Wraith()
#
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)
#
#
# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")
#
#
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
#
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()
#
# for unit in attack_units:
#     unit.attack("1시")
#
# for unit in attack_units:
#     unit.damaged(randint(5, 21))
#
# game_over()


# 발키리 공중 공격 유닛, 대공 공격만 가능합니다
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

## 연산자 오버로딩
#  # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)
#
# #배틀크루저: 공중유닛, 체력도 굉장히 좋음, 공격력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 35, 3)
#
# vulture.move("11시")
# battlecruiser.move( "7시")


## PASS

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass
#
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     pass
#
# game_start()
# game_over()

# Super

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location



# 총 "3대의" 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년


def show_me_the_sale_list():
    print("총 " + str(len(houses))+"개의 매물이 있습니다")

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        pass
        print("{0} {1} {2} {3} {4}" \
          .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

houses = []
gn = House("강남", "아파트", "매매", "10억", "2010년")
mp = House("마포", "오피스텔", "전세", "5억", "2007년")
sp = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(gn)
houses.append(mp)
houses.append(sp)

# sale_list = [gn, mp, sp]


# show_me_the_sale_list()

# for house in houses:
#     house.show_detail()

### 예외 처리! if elif  랑 같은 문법?

# try:
#     print("숫자를 입력하세요")
#     nums = []
#
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)
#
#

### 에러 발생시키기기

# try:
#     print("한 자리 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 > 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 /  num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
#
#
# ## 사용자 정의 에러

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg
# try:
#     print("한 자리 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 > 10:
#         raise BigNumberError("입력값 : {0}. {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 /  num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)

## finally


# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg
# try:
#     print("한 자리 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 > 10:
#         raise BigNumberError("입력값 : {0}. {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 /  num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")
#

    ### 예최처리 퀴즈!!!!!

#  동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
#  대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을
# 제작하였습니다
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오
#
# 조건 1 : 1 보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
# 출력 메세지 : " 잘못된 값을 입력하였습니다."
#
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#          치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#          출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."


#
# class SoldOutError(Exception):
#     pass
#
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
#
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <=0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더이상 주문을 받지 않습니다.")
#         break

#
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv # 모듈명이 길 때 줄여서 사용 가능
#
# mv.price_soldier(2)
#
# from theater_module import  *
#
# price_soldier(4)
#
# from theater_module import price, price_morning  # 필요한 것만 사용 선택 가능
#
# price(4)

# from  theater_module import price_soldier as ps
# ps(4)

## 패키지
#
# import travel.thiland # import .뒤에는 모듈이나 패키지만 가능하다
# trip_to = travel.thiland.ThailandPackage()
# trip_to.detail()
#
# from travel.thiland import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()
#
# from travel import vetnam
# trip_to = vetnam.VietnamPackage()
# trip_to.detail()

# __all __
#
from travel import *
#
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))