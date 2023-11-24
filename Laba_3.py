import re
def check_snils(snils):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{3} \d{2}$') #Шаблон снился
    last_Two = snils[-2:] # 2 Последних числа


    if pattern.match(snils):

        l = snils.replace("-", "")
        control_sum = 0 #Контрольная сумма

        for i in range(0, 9):
            control_sum = int(l[i]) * (9 - i) + control_sum

        if control_sum <= 101 and control_sum == int(last_Two):
            return f"{snils} | Является СНИЛСом"

        if control_sum > 101 and control_sum % 101 == int(last_Two):
            return f"{snils} | Является СНИЛСом"

    return f"{snils} | Не является СНИЛСом"


while(True):
    answer_user = input() 
    if answer_user == "stop":
        exit(0)

    print(check_snils(answer_user))

#осознанный commit №1
#Я молодец 