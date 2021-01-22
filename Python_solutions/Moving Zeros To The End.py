def move_zeros(array):
    new_array = []
    zero_list = []
    
    for e in array:
        if e != 0:
            new_array.append(e)
        
        if e == 0:
            if isinstance(e, bool):
                if e == False:
                    new_array.append(e)
                    
            if isinstance(e, int) or isinstance(e, float):
                if e == 0 or e == 0.0:
                    zero_list.append(e)
                    
    for end_value in zero_list:
        if str(end_value) == "False":
            continue
            
        elif str(end_value) == "0" or str(end_value) == "0.0":
            new_array.append(end_value)
    
    return new_array
