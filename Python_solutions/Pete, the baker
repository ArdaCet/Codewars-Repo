def cakes(recipe, available):
    ingredient_coef = []
    available_key_list = list(available.keys())
    recipe_key_list = list(recipe.keys())
    cont = True
    
    for element in range(0, len(recipe_key_list)):
        if recipe_key_list[element] not in available_key_list:
            cont = False
            return 0
            
    if cont:
        for i in range(0, len(recipe)):
            for j in range(0, len(available_key_list)):
                if recipe_key_list[i] == available_key_list[j]:
                    div_result = int(available[available_key_list[j]]) // int(recipe[recipe_key_list[i]])
                    ingredient_coef.append(div_result)
                    
    if sum(ingredient_coef) > 0:
         return min(ingredient_coef)
