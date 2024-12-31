
first_num = int(input("First number "))
second_num = int(input("Second number "))
operator = input("operator " )

if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "/" and second_num != 0:
    print(first_num / second_num)
else:
    print("invalid")