import csv

def write_into_csv(info_list):
     with open('student_info.csv','a',newline='') as csv_file:
         writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
           writer. writerrow(["name","age","contact_number","e-mail_id"])
           
         writer.writerow(info_list)

condition = True

while(condition):
    student_info = input("enter student information in the following format(name age contact_number e-mail_id):")
    print ("entered  information:" + Student_info)

    student_info_list = student_info.spilt('')
    print("entered spilt up information is:" + str(student_info_list))

    write_into_csv(student_info_list)

    condition_check == input("enter (yes/no) if you want to enter information for another student:")
    if condition_check =="yes":
        condition=true
    elif condition_check =="no":
        condition = False