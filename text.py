
def revword(word:str) -> str:
    word=" "+word
    reWord=""
    counter=1
    counter1=0
    k=0
    for i in word:
        #We will separate the words according to the space and reverse the order of each one separately.
        if i==" ":
            #If there is a space then it is a sign that there is more than one word left that we need to reverse its order
            if " " in word[counter1+1:]:
                #In the next loop we will separate each word in a sentence and work only on the word
                for j in word[k:counter1]:
                    reWord=reWord+word[counter1-counter]
                    counter+=1
                    if counter>(counter1-k):
                        break
                #We will reset the counter for the next word
                counter=1
                #we will turn the k to the place where the first word ended. and continue with the rest of the word
                k=counter1
            # this part refers to the last two word in the sentens
            else :
                for j in word[k:counter1]:
                    reWord=reWord+word[counter1-counter]
                    counter+=1
                    if counter>(counter1-k):
                        break
                counter=1
                for g in word[counter1:]:
                    reWord=reWord+word[len(word)-counter]
                    counter+=1 
                    if counter>(len(word)-counter1):
                        reWord=reWord.rstrip()
                        return reWord.lower()
        counter1+=1
        
def countword()->int:
    file=open('text.txt',"r") 
    counter=0
    counter2=1
    #we will start a loop that goes over each line
    for i in file:
        #if it is the first line we will save the word
        if counter==0:
            x=i
            x=x.strip()
            x=x.lower()
        # for the rest of the lines
        else:
            #operate the revers function
            lineFile=revword(i)
            while True:
                #we will find the location for the word we are looking for
                location = lineFile.find(x)
                #if the word is not in the line we will break the loop and contionue to the next line
                if location==-1:
                    break
                #if the word is in the line 
                else:
                    #we will find the place that the word ends count the word and keep looking the word in the rest of the line
                    location+=len(x)
                    counter2+=1
                    lineFile=lineFile[location:]
                    continue
        counter+=1
    return counter2
