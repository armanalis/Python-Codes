#Word counter, This program should find the words and how many times used in this file.
with open(FILE) as openfile:
    lines = openfile.readlines()
    d1 = dict()
    line = list()
    for line in lines:
        words = line.split()
        #print(words)
        for word in words:
            #print(word)
            if word in d1:
                d1[word] = d1[word]+1
            else:
                d1[word] = 1
    print(d1)