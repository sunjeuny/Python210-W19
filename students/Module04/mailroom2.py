#----------------------------------------#
# Title: mailroom2.py
# Initial File
# Claire Yoon,2019-02-03,New file
#----------------------------------------#


# Convert main donor data structure to be a dict.
donor_dict =  { 'Will Gates': [10000, 20000, 300000],
                'Conan Obrien': [20000],
                'Mark Zucker' : [30000, 12000],
                'Jeff Bezos' : [50000],
                'Tom Hardy' : [12000, 40000]
                }

def thx_single():
    while(True):
        temp = []
        for i in donor_dict.keys():
            temp.append(i)
        name = input("Please enter a full name (enter 'list' to see list): ")
        # If user types 'list'
        if name.lower() == 'list':
            print(temp)
        # If user types other than list - applies the same logic
        else:
            amount = float(input("Please enter amount of donation (in numbers): "))
            if name in temp:
                donors_amount = donor_dict.get(name)
                donors_amount.append(amount)
                history_amount = 0
                for i in range(len(donors_amount)):
                    history_amount += donors_amount[i]
            else :
                donor_dict.update({name : amount})
                history_amount = amount

            print("\nDear", name, "\n\n I would like to thank you for your donation of $",history_amount,"so far.\n",
                  "Our organization relies on the generosity of donors such as yourself. \n Thank you once again. \n")
            break
    return

def create_report():
    report_lst= []

    for i in donor_dict.keys():
        report_lst.append([i, sum(donor_dict.get(i)), len(donor_dict.get(i)), sum(donor_dict.get(i))/len(donor_dict.get(i))])

    print()
    print("<<DONATION REPORT>>")

    print("Donor Name        | Total Given | Num Gifts | Average Gift\n------------------------------------------------------------")
    for l in report_lst:
        print ('{:<20}'.format(l[0]), end='')
        print ('$','{:<12}'.format(l[1]), end='')
        print ('{:<11}'.format(l[2]), end='')
        print ('$','{:<12}'.format(l[3]))
    print()

def thx_all():
    for i in donor_dict.keys():
        # get donor's amount of donation
        amount = sum(donor_dict.get(i))
        donor_name = i.split(' ')
        filename = "thx_letter"
        # generate file name as : thx_letter_(firstname)_(lastname)
        for j in range(len(donor_name)):
            filename += '_'+(donor_name[j])
        # open a file and write body
        letter = open(filename, "w")
        letter_body = str("\nDear "+ str(donor_name[0]) + ' ' + str(donor_name[1]) + ",\n\nI would like to thank you for your donation of $" + str(amount) +" so far.\n" +
                  "Our organization relies on the generosity of donors such as yourself. \n\nThank you once again. \n")

        letter.write(letter_body)
        letter.close()
    print("\n All thank-you letters have been created. Please check your current folder. \n ")
    return

def equit():
     exit()


def main_menu():
    while(True):
        # a dict to switch between the user’s selections.
        menu_dict = {1: thx_single, 2: create_report, 3: thx_all, 4: equit }
        menu = int(input("Choose an action: \n 1 - Send a Thank You to a single donor \n 2 - Create a Report \n 3 - Send letters to all donors. \n 4 - Quit \n : "))
        menu_dict.get(menu)()

    return

if __name__ == '__main__':
    main_menu()
