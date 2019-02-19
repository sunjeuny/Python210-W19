#----------------------------------------#
# Title: mailroom4.py
# Revised mailroom3.py
# Claire Yoon,2019-02-18,New file
#----------------------------------------#

# Convert main donor data structure to be a dict.
donor_dict =  { 'Will Gates': [10000, 20000, 300000],
                'Conan Obrien': [20000],
                'Mark Zucker' : [30000, 12000],
                'Jeff Bezos' : [50000],
                'Tom Hardy' : [12000, 40000]
                }

name_mapping = {i: i.lower() for i in donor_dict.keys()}

# listing donors
def print_list():
    return [i for i in name_mapping.keys()]

# adding or updating donors
def update_donor(name, amount):
    new_amount = {name: [amount]}
    donor_dict.update(new_amount)
    name_mapping.update({name: name.lower()})
    return (donor_dict)

# generating thank you text
def write_thx(name, history_amount):
    return "\nDear {},\n\nOur organization would like to thank you for your donation of ${} so far.\nOur organization relies on the generosity of donors such as yourself.\n\nThank you once again. \n".format(name, history_amount)

#  Unit tests should test the data manipulation logic code: generating thank you text, adding or updating donors, and listing donors.
def thx_single():
    while(True):
        name = input("Please enter a full name (enter 'list' to see list): ")
        name = name.rstrip().lstrip()

        # If user types 'list'
        # listing donors
        if name.lower() == 'list':
            print(print_list())

        # If user types other than list - applies the same logic
        else:
            amount = float(input("Please enter amount of donation (in numbers): "))

            #for existing name
            if name.lower() in name_mapping.values():
                for camel, lower in name_mapping.items():
                    if lower == name.lower():
                        name = camel
                donors_amount = donor_dict.get(name)
                # append input amount value to donors_amount list
                donors_amount.append(amount)
                print("Donor list has been updated: ",donor_dict)
                history_amount = 0
                for i in range(len(donors_amount)):
                    history_amount += donors_amount[i]

            #for newly added name
            else :
                name_toList = name.lower().split(' ')
                for i in range(len(name_toList)):
                    name_toList[i] = name_toList[i].capitalize()
                name = " ".join(name_toList)
                # adding or updating donors
                print("Donor list has been updated: ",update_donor(name,amount))
                history_amount = amount
            # generating thank you text
            print(write_thx(name, history_amount))
            break
    return

def get_report():
    #data logic
    #using comprehension
    report_lst = []
    [report_lst.append([i, int(sum(donor_dict.get(i))), len(donor_dict.get(i)),
                        round((sum(donor_dict.get(i)) / len(donor_dict.get(i))), 2)]) for i in donor_dict.keys()]
    print(report_lst)
    return report_lst

def print_report(report):
    print()
    print("\t\t\t\t<<DONATION REPORT>>")
    # user presentation
    print("Donor Name        | Total Given | Num Gifts | Average Gift\n------------------------------------------------------------")
    for l in report:
        print ('{:<20}'.format(l[0]), end='')
        print ('$','{:<12}'.format(l[1]), end='')
        print ('{:<11}'.format(l[2]), end='')
        print ('$','{:<12}'.format(l[3]))
    print()

def display_report():

    print_report(get_report())

def write_file(key):
    amount = sum(donor_dict.get(key))
    donor_name = key.split(' ')
    filename = '_'.join(donor_name) + '_Thx_Letter'
    # open a file and write body
    letter = open(filename, "w")
    letter_body = letter_text(donor_name[0], donor_name[1], amount)
    letter.write(letter_body)
    letter.close()

def letter_text(fname, lname, amount):
    return "\nDear {} {},\n\nOur organization would like to thank you for your donation of ${} so far.\nOur organization relies on the generosity of donors such as yourself.\n\nThank you once again. \n".format(fname, lname, amount)


def thx_all():
    for key in donor_dict.keys():
        write_file(key)
    print("\n All thank-you letters have been created. Please check your current folder. \n ")
    return

def equit():
     exit()

def main_menu():
    while(True):
        # a dict to switch between the user’s selections.
        menu_dict = {1: thx_single, 2: display_report, 3: thx_all, 4: equit}
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
