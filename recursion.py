def look_for_key(mainBox):
    pile = mainBox.Make_Pile_To_Look_Through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("You found the key!")
            
    
    