'''9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

fname = input("Enter file name: ")

file = open(fname)
#count = 0
lst1=list()
dict=dict()
for lines in file:
    lines.rstrip()

    if lines.startswith('From'):
        if lines.startswith('From:'):
            continue
        else:
            #count=count+1
            lst=lines.split()
            lst1.append(lst[1])
for word in lst1:
    dict[word]=dict.get(word,0)+1
high=None
highword=None
for emailid,senttimes in dict.items():
    if high is None or senttimes > high:
        high= senttimes
        highword=word
print(highword,high)
