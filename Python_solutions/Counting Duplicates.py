def duplicate_count(text):
    number_holder = []
    t = 0
    
    LowerCase_text = text.lower()
    
    for e in LowerCase_text:
        if e not in number_holder:
            counter = LowerCase_text.count(e)
            
            if counter > 1:
                number_holder.append(e)
                t = t + 1
            else:
                continue
                
        else:
            continue
            
    return t    
