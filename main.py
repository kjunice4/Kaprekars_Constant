
i = 0
while i == 0:
    print()
    a = input("Enter a 4 digit number:")
    print()
    if len(a.replace(" ","")) == 4:
        i = 1
    else:
        print()
        print("Not a 4 digit number!!!")
        print()


a_list = []
for x in a:
    a_list.append(int(x))

a_list_sorted_LOW_TO_HIGH = sorted(a_list)
print("a_list_sorted_LOW_TO_HIGH",a_list_sorted_LOW_TO_HIGH)
print()
a_list_sorted_HIGH_TO_LOW = sorted(a_list_sorted_LOW_TO_HIGH, reverse=True)
print("a_list_sorted_HIGH_TO_LOW",a_list_sorted_HIGH_TO_LOW)
print()

Low_High = ""
for x in a_list_sorted_LOW_TO_HIGH:
    Low_High = Low_High + str(x)
    
print("Low_High = ",Low_High)
print()

High_Low = ""
for x in a_list_sorted_HIGH_TO_LOW:
    High_Low = High_Low + str(x)
    
print("High_Low = ",High_Low)
print()

i = 0
j = 1
while i == 0:
    print("Attempt #",j)
    answer = str(int(High_Low) - int(Low_High)) 
    print(High_Low + " - " + Low_High + " = " + str(answer))
    print()
    if int(answer) == 6174:
        print("Answer = 6174")
        print("Achieved 6174 after ",j," attempt(s)")
        i = 1
        break
    elif int(answer) == 0:
        print("Bad input of all similar numbers")
        break
    else:
        if len(answer) == 3:
            answer = "0" + answer
        a_list = []
        for x in str(answer):
            a_list.append(int(x))

        a_list_sorted_LOW_TO_HIGH = sorted(a_list)
        print("a_list_sorted_LOW_TO_HIGH",a_list_sorted_LOW_TO_HIGH)
        print()
        a_list_sorted_HIGH_TO_LOW = sorted(a_list_sorted_LOW_TO_HIGH, reverse=True)
        print("a_list_sorted_HIGH_TO_LOW",a_list_sorted_HIGH_TO_LOW)
        print()

        Low_High = ""
        for x in a_list_sorted_LOW_TO_HIGH:
            Low_High = Low_High + str(x)
            
        print("Low_High = ",Low_High)
        print()

        High_Low = ""
        for x in a_list_sorted_HIGH_TO_LOW:
            High_Low = High_Low + str(x)
            
        print("High_Low = ",High_Low)
        print()
    j = j + 1
    
