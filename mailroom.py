#----------------------------------------#
# Title: mailroom.py
# Initial File
# Claire Yoon,2019-01-28,New file
#----------------------------------------#

# data structure for -  a list of your donors, a history of the amounts they have donated.
# populate at first with at least five donors
# with between 1 and 3 donations each

#prompt - to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

donor_list = [('Will Gates', 10000), ('Will Gates', 20000), ('Will Gates', 300000),
              ('Conan Obrien', 20000),
              ('Mark Zucker', 30000), ('Mark Zucker', 12000),
              ('Jeff Bezos', 50000),
              ('Tom Hardy', 12000), ('Tom Hardy', 40000)]

def main_menu():

    while(True):
        menu = input("Please choose the number to enter one of the menus. \n 1 - Send a Thank you \n 2 - Create a Report \n 3 - quit \n : ")
        if menu == '1' :
            send_Thx()
        elif menu == '2' :
            create_Report()
        elif menu == '3' :
            break
        else :
            print("Please enter a valid menu")

def send_Thx():
    while(True):
        temp = []
        for i in range(len(donor_list)):
            if donor_list[i][0] not in temp:
                temp.append(donor_list[i][0])
        name = input("Please enter a full name (enter 'list' to see list): ")
        # If user types 'list'
        if name.lower() == 'list':
            print(temp)
        # If user types other than list - applies the same logic
        else:
            amount = float(input("Please enter amount of donation (in numbers): "))
            donor_list.append((name, amount))

            history_amount = 0
            for i in range(len(donor_list)):
                if(donor_list[i][0] == name):
                    history_amount += donor_list[i][1]

            print("Dear ", name, "\n\n I would like to thank you for your donation of $",history_amount,"so far.\n",
                  "Our organization relies on the generosity of donors such as yourself. \n Thank you once again. \n")

            break
    return

def create_Report():
    temp_lst = []
    report_lst= []

    for i in range(len(donor_list)):
        if donor_list[i][0] not in temp_lst:
            temp_lst.append(donor_list[i][0])

    for i in range(len(temp_lst)):
        report_lst.append([temp_lst[i], 0.0, 0, 0.0])

    for i in range(len(temp_lst)):
        for j in range(len(donor_list)):
            if donor_list[j][0] == temp_lst[i]:
                name = donor_list[j][0]
                amount = donor_list[j][1]
                report_lst[i] = ([name, amount + report_lst[i][1], report_lst[i][2] + 1, (amount + report_lst[i][1])/(report_lst[i][2] + 1)])


    print("<<DONATION REPORT>>")

    print("Donor Name        | Total Given | Num Gifts | Average Gift\n------------------------------------------------------------")
    for l in report_lst:
        print ('{:<20}'.format(l[0]), end='')
        print ('$','{:<12}'.format(l[1]), end='')
        print ('{:<11}'.format(l[2]), end='')
        print ('$','{:<12}'.format(l[3]))

if __name__ == '__main__':
    main_menu()