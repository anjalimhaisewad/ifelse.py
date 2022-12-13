# password=input("enter the password---")
# if len(password)>6 or len(password)<9:
#     if "@" in password or "#" in password or "%" in password or "&" in password or "$" in password:
#         if "a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q" in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password:
#             if "A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R"in password or "S" in password or "T" in password or "U" in password or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password:
#                 if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
#                   print("strong password")
#                 else:
#                 print("enter upper character")
#         else:
#             print("enter lower character")
#     else:
#         print("enter the special character ")
# else:
#     print("week password")



# password=input("enter the password:-----")
# if len(password)>6 or len(password)<9:
#     if "@"in password or "$"in password or "#"in password:
#         if "a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q" in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password:
#             if "A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password or "v" in password or "W" in password or "X" in password or "Y" in password or "Z" in password:
#                 if "1" in password or "2" in password or "3" in password or"4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
#                     print("strong password")
#                 else:
#                     print("enter the digit")
#             else:
#                 print("enter the upper character")
#         else:
#             print("enter the lower character")
#     else:
#         print("enter the special character")
# else:
#     print("weak password")



rooms=int(input("enter the rooms"))
beds=int(input("enter the beds"))
if rooms in (101,103,201,203,204,301,302,303,304,401,402,403,404):
    if beds>=1 and beds<=10:
        print("10 beds in room")
    else:
        print("beds not in room")
elif rooms in (102):
    if beds==3:
        print("3 beds in room")
    else:
        print("not 3 beds in room")
elif rooms in (202):
    if beds==0:
        print("there no beds because of that room is kitchen")
    else:
        print("there is bed")
else:
    print("not in 10 beds")