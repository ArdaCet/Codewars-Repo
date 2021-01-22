def to_camel_case(text):
    main_list = []
    tag = False
    
    for word in text:
        if word == "-" or  word == "_":
            word = ""
            main_list.append(word)
            tag = True
            
        else:
            if tag is True:
                main_list.append(word.upper())
                tag = False
            else:
                main_list.append(word)
                
    output = str(main_list)[1:-1].replace(", ","").replace("'","")
    
    return output
