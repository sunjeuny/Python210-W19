#----------------------------------------#
# Title: strformat_lab.py
# Initial File
# Claire Yoon,2019-01-27,New file
#----------------------------------------#

# Task One
print('Task One: ')
tpl = ( 2, 123.4567, 10000, 12345.67)
print('file_' + '{0:0>3}'.format(tpl[0]) , " : " , "{:.2f}".format(float(tpl[1])) , ', ' , '{:0.2e}'.format(float(tpl[2])), ', ' , '{:3.2e}'.format(float(tpl[3])))
print('')

#Task Two
print('Task Two: ')
print('file_' + '{0:0>3}'.format(tpl[0]) , " : " , "{:.2f}".format(float(tpl[1])) , ', ' , '{:0.2e}'.format(float(tpl[2])), ', ' , '{:3.2e}'.format(float(tpl[3])))
print('')

# #Task Three
print('Task Three: ')
tpl3 = (2,3,5,7,9)

def formatter(in_tuple):
    num = (len(in_tuple))
    form_string = "the "+str(num)+" numbers are: "
    # form_string = 'the ',len(in_tuple),' numbers are:'
    for i in range(num-1):
        form_string += "{:d} , "
    form_string += "{:d}"
    return form_string.format(*in_tuple)

print(formatter(tpl3))
print('')

#Task Four
print('Task Four: ')
tpl4 = (4, 30, 2017, 2, 27)
print('{0:0>2}'.format(tpl4[3]),tpl4[4],tpl4[2],'{0:0>2}'.format(tpl4[0]),tpl4[1])
print('')

#Task Five
print('Task Five: ')
lst5 = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {lst5[0][:-1]} is {lst5[1]} and the weight of a {lst5[2][:-1]} is {lst5[3]}")
print(f"The weight of an {lst5[0][:-1].upper()} is {lst5[1]*1.2} and the weight of a {lst5[2][:-1].upper()} is {lst5[3]*1.2}")
print('')

#Task Six
print('Task Six: ')
for line in [['Name', 'Age', 'Cost'], ['Steve Jobs', '62', '$1000.00'],['Diana Hamington', '43', '$115.00'],['John Doe', '24','$200.00']]:
    print('{:>15} {:>15} {:>15}'.format(*line))


