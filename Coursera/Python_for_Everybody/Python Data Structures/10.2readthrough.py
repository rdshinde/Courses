'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''


fname = input("Enter file name: ")

file = open(fname)
count = 0
lst1=list()
dict1=dict()
for lines in file:
    lines.rstrip()

    if lines.startswith('From'):
        if lines.startswith('From:'):
            continue
        else:
            count=count+1
            lst=lines.split()
            str1=''.join(lst[5])
            lst1.append(str1[0:2])
for word in lst1:
    dict1[word]=dict1.get(word,0)+1
for i,y in sorted (dict1.items()):
    print(i,y)
