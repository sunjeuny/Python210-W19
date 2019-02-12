#----------------------------------------#
# Title: mailroom3.py
# Revised mailroom2.py
# Claire Yoon,2019-02-09,New file
#----------------------------------------#


# Convert main donor data structure to be a dict.
donor_dict =  { 'Will Gates': [10000, 20000, 300000],
                'Conan Obrien': [20000],
                'Mark Zucker' : [30000, 12000],
                'Jeff Bezos' : [50000],
                'Tom Hardy' : [12000, 40000]
                }

name_mapping = {i: i.lower() for i in donor_dict.keys()}

def thx_single():
    while(True):
        name = input("Please enter a full name (enter 'list' to see list): ")

        # If user types 'list'
        if name.lower() == 'list':
            print([i for i in name_mapping.keys()])

        # If user types other than list - applies the same logic
        else:
            amount = float(input("Please enter amount of donation (in numbers): "))
            if name.lower() in name_mapping.values():
                for camel, lower in name_mapping.items():
                    if lower == name.lower():
                        name = camel
                donors_amount = donor_dict.get(name)
                # append input amount value to donors_amount list
                donors_amount.append(amount)
                history_amount = 0
                for i in range(len(donors_amount)):
                    history_amount += donors_amount[i]

            #for newly added name
            else :
                name_toList = name.lower().split(' ')
                for i in range(len(name_toList)):
                    name_toList[i] = name_toList[i].capitalize()
                name = " ".join(name_toList)
                new_amount = {name : [amount]}
                donor_dict.update(new_amount)
                print(donor_dict)
                history_amount = amount
                name_mapping.update({name: name.lower()})

            print("\nDear", name, ",\n\nOur organization would like to thank you for your donation of $",history_amount,"so far.\n",
                  "Our organization relies on the generosity of donors such as yourself. \n Thank you once again. \n")
            break
    return

def create_report():
    report_lst= []

    #using comprehension
    [report_lst.append([i, sum(donor_dict.get(i)), len(donor_dict.get(i)), sum(donor_dict.get(i))/len(donor_dict.get(i))]) for i in donor_dict.keys()]
    print()
    print("\t\t\t\t<<DONATION REPORT>>")

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
        filename = '_'.join(donor_name) + '_Thx_Letter'
        # open a file and write body
        letter = open(filename, "w")
        letter_body = str("\nDear "+ str(donor_name[0]) + ' ' + str(donor_name[1]) + ",\n\nOur organization would like to thank you for your donation of $" + str(amount) +" so far.\n" +
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
        menu_dict = {1: thx_single, 2: create_report, 3: thx_all, 4: equit}
        try:
            menu = int(input("Choose an action: \n 1 - Send a Thank You to a single donor \n 2 - Create a Report \n 3 - Send letters to all donors. \n 4 - Quit \n : "))
            menu_dict.get(menu)()
        except ValueError as e :
            print("** Warning: Please enter number **")
        except TypeError as e:
            print("** Warning: Please enter valid menu (1 - 4) **")

    return

if __name__ == '__main__':
    main_menu()