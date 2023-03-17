# The Longest String And Its Length
list = []
count = 1

for length in range(5):
    string = input("Enter 5 different sized string : ")
    list.append(string)
    count += 1

TheLongest = 0
TheLongestString = ''

for elem in range(5):
    if len(list[elem]) > TheLongest:
        TheLongest = len(list[elem])
        TheLongestString = list[elem]

print('The Longest String is :', TheLongestString)
print('Length of The Longest Word is: ', TheLongest)

