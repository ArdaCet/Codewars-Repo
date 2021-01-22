def longest_consec(strarr, k):
    whole_sentence = ""
    sentence_length = 0
    output = ""
    
    if k <= len(strarr):
        for i,_ in enumerate(strarr[:]):
            value = strarr[i:i+k]
            
            if len(value) == k:
                whole_sentence = str(value)[1:-1].replace(",","").replace(" ","").replace("'","")
                word_count = len(whole_sentence)
                
                if sentence_length < word_count:
                    sentence_length = word_count
                    output = whole_sentence
                    
        return output

    elif k > len(strarr):
        return ""
    
    elif k <= 0:
        return ""
    
    elif len(strarr) <= 0:
        return ""
