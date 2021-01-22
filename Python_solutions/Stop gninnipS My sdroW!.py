def spin_words(sentence):
    new_list_2 = []
    
    if " " not in sentence:
        if len(sentence) >= 5:
            c2_words = sentence[::-1]
            new_list_2.append(c2_words)
        else:
            new_list_2.append(sentence)
            
    if " " in sentence:
        intowords = sentence.split(" ")
        for elements in intowords:
            #print(elements)
            if len(elements) >= 5:
                reversed_word = elements[::-1]
                #print(reversed_word)
                new_list_2.append(reversed_word)
            else:
                new_list_2.append(elements)
                
    return str(new_list_2).replace("[","").replace("]","").replace("'","").replace(",","")
