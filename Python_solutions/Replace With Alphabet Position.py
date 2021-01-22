def alphabet_position(text):
    #alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabet_string = string.ascii_lowercase
    alphabet = list(alphabet_string)
    
    alph_dict = {}
    output = []
    
    for values, keys in enumerate(alphabet):
        alph_dict[keys] = values + 1
        
    for letter in text.lower():
        if letter in alph_dict.keys():
            output.append(alph_dict[letter])
            
        else:
            continue
            
    return str(output)[1:-1].replace(",","")
