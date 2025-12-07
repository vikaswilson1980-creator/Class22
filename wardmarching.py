def match(words):
    ctr=0
    lst=[]
    for word in words:
        if (len(word)>1 and word[0]== word[-1]):
            ctr+=1
            lst.append(word)
    print("the list of words with first and last character same \n",list)
    return ctr
count=match(['abc','cfc','xyz','aba','1221'])
print("The number of words having first and last character same are ",count)