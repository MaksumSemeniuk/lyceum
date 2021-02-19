skob_1 = input("Введите скобку 1")

num_1 = int(input("Введите первое число\n"))

znak_1 = input("Введите знак")

num_2 = int(input("Введите второе число\n"))

skob_2 = input("Введите скобку 2")

znak_2 = input("Введите знак")

num_3 = int(input("Введите третье число\n"))

skob_3 = input("Введите скобку 3")

if znak_1=="+":
    if znak_2=="+":
        result_1 = num_1 + num_2 + num_3
        print("Ответ :" + str(result_1))
    elif znak_2=="-":
        result_1 = num_1 + num_2 - num_3
        print("Ответ :" + str(result_1))
    elif znak_2=="*":
        result_1 = num_1 + num_2 * num_3
        print("Ответ :" + str(result_1))
    elif znak_2=="/":
        if num_3==0:
            print("Деление на ноль!!!")
        else:
            result_1 = num_1 + num_2 / num_3
            print("Ответ :" + str(result_1))
    else:
            print("Nothing")
elif znak_1=="-":
    if znak_2=="+":
        result_1 = num_1 - num_2 + num_3
        print("Ответ :" + str(result_1))
    elif znak_2=="-":
        result_1 = num_1 - num_2 - num_3
        print("Ответ :" + str(result_1))
    elif znak_2=="*":
        result_1 = num_1 - num_2 * num_3
        print("Ответ :" + str(result_1))
    elif znak_2=="/":
        if num_3==0:
            print("Деление на ноль!!!")
        else:
            result_1 = num_1 - num_2 / num_3
            print("Ответ :" + str(result_1)) 
    else:
        print("Nothing")
elif znak_1=="*":
    if znak_2=="+":
        result_1 = num_1 * num_2 + num_3
        print("Ответ :" + str(result_1))
    elif znak_2=="-":
        result_1 = num_1 * num_2 - num_3
        print("Ответ :" + str(result_1))
    elif znak_2=="*":
        if skob_1 =="(" and skob_2==")":
            result_1 = (num_1 * num_2) * num_3
            print("Ответ :" + str(result_1))
        elif skob_2=="(" and skob_3==")":
            result_1 = num_1 * (num_2 * num_3)
            print("Ответ :" + str(result_1))
        else:
                print("Nothing")
    elif znak_2=="/":
        if num_3==0:
            print("Деление на ноль!!!")
        else:
            if skob_1 =="(" and skob_2==")":
                result_1 = (num_1 * num_2) / num_3
                print("Ответ :" + str(result_1))
            elif skob_2=="(" and skob_3==")":
                result_1 = num_1 * (num_2 / num_3)
                print("Ответ :" + str(result_1)) 
            else:
                print("Nothing")
    else:
       print("Nothing")
elif znak_1=="/":
    if znak_2=="+":
        if num_2==0:
           print("Деление на ноль!!")
        else:
           result_1 = num_1 / num_2 + num_3
           print("Ответ :" + str(result_1))
    elif znak_2=="-":
        if num_2==0:
           print("Деление на ноль!!")
        else:
            result_1 = num_1 / num_2 - num_3
            print("Ответ :" + str(result_1))
    elif znak_2=="*":
        if skob_1=="(" and skob_2==")": 
            if num_2==0:
              print("Деление на ноль!!")
            else:
               result_1 = (num_1 / num_2) * num_3
               print("Ответ :" + str(result_1))        
        elif skob_2=="(" and skob_3==")":            
            if num_3==0 or num_2==0:
                print("Деление на ноль!!")
            else:
                result_1 = num_1 / (num_2  * num_3)
                print("Ответ :" + str(result_1))
    elif znak_2=="/":
        if num_2==0 or num_3==0:
            print("Деление на ноль!!")
        else:
            if skob_1=="(" and skob_2==")":
                result_1 = (num_1 / num_2 ) / num_3
                print("Ответ :" + str(result_1))
            elif skob_2=="(" and skob_3==")":
                result_1 = num_1 / ( num_2  / num_3 )
                print("Ответ :" + str(result_1))
            else:
                print("Nothing")
    else:
      print("Nothing")
else:
   print("Nothing")

            
    