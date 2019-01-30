#----------------------------------------#
# Title: slicing_lab.py
# Initial File
# Claire Yoon,2019-01-27,New file
#----------------------------------------#

# with the first and last items exchanged.
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1]+ seq[:1]

assert exchange_first_last("this is a string") == "ghis is a strint"
assert exchange_first_last((2, 54, 13, 12, 5, 32)) == (32, 54, 13, 12, 5, 2)

# with every other item removed.

def every_other_removed(seq):
    return seq[::2]

assert every_other_removed("this is a string") == "ti sasrn"
assert every_other_removed((2, 54, 13, 12, 5, 32)) == (2, 13, 5)

# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def remove4_every_other(seq):
    if(len(seq) <= 8):
        return print("Length should be bigger than 8")
    seq = seq[4:-4]
    return seq[::2]

assert remove4_every_other("this is a string") == " sas"
assert remove4_every_other((2, 54, 13, 12, 5, 32, 45, 28, 14, 8, 72)) == (5, 45)

# with the elements reversed (just with slicing).
def reverse(seq):
    return seq[::-1]

assert reverse("this is a string") == "gnirts a si siht"
assert reverse((2, 54, 13, 12, 5, 32)) == (32, 5, 12, 13, 54, 2)

# with the last third, then first third, then the middle third in the new order.
def new_order(seq):
    l = len(seq)
    return seq[int(l*(2/3)):] + seq[:int(l*(1/3))] + seq[int(l*(1/3)):int(l*(2/3))]

assert new_order("this is a string") == "stringthis is a "
assert new_order((2, 54, 13, 12, 5, 32)) == (5, 32, 2, 54, 13, 12)
