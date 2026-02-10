print("caution please enter roll number start from 24")

libary__members={24811:"chaitanya",
                 24812:"satya",
                 24813:"nandhu"}
print("----libary system----")

try:
    roll_num=int(input("roll_num :"))
    name=input("name :")

    if roll_num in libary__members:
        print("member allready  existe")
        print(f"roll number:{roll_num}")
        print(f"name:{libary__members[roll_num]}")
    else:
       print("new member found:updating")
       libary__members[roll_num]=name
       print("updated successfully")

       print("\n updated member")
       print(libary__members)

except valueerror:
    print("enter valid roll_num")
    
