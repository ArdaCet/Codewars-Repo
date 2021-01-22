def create_phone_number(n):
    i = str(n[0:3])
    b = str(n[3:6])
    e = str(n[6:])
    
    final_i = i.replace(",","").replace("[","").replace("]","").replace(" ","")
    final_b = b.replace(",","").replace("[","").replace("]","").replace(" ","")
    final_e = e.replace(",","").replace("[","").replace("]","").replace(" ","")
    
    dials = "(" + final_i + ") " + final_b + "-" + final_e
    return dials
