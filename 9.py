wool = input("Собака короткошерстной породы? ").lower()
if wool == "да":
    height = input("Рост собаки менее 50 см? ").lower()
    if height == "да":
        tail = input("У собаки короткий хвост? ").lower()
        if tail == "да":
            print("английский бульдог")
        elif tail == "нет":
            ears = input("У собаки длинные уши? ").lower()
            if ears == "да":
                print("гончая")
            elif ears == "нет":
                body = input("У собаки короткое тело? ").lower()
                if body == "да":
                    print("мопс")
                elif body == "нет":
                    print("чихуахуа")
    elif height == "нет":
        weight = input("Собака весит более 50 кг? ").lower()
        if weight == "да":
            print("датский дог")
        elif weight == "нет":
            print("фоксхаунд")
elif wool == "нет":
    height = input("Рост собаки менее 50 см? ").lower()
    if height == "да":
        character = input("У собаки доброжелательный характер? ").lower()
        if character == "да":
           print("кокер-спаниэль")
        elif character == "нет":
            print("ирландский сеттер")
    elif height == "нет":
        height_70 = input("Рост собаки менее 70 см? ").lower()
        if height_70 == "нет":
            color = input("Окрас рыжий с белыми отметинами? ").lower()
            if color == "да":
                print("сенбернар")
            elif color == "нет":
                color_white = input("Белоснежный окрас? ").lower()
                if color_white == "да":
                    print("ирландский волкодав")
                elif color_white == "нет":
                    print("ньюфаундленд")
        elif height_70 == "да":
            ears = input("У собаки длинные уши? ").lower()
            if ears == "да":
                print("большой вандейский грифон")
            elif ears == "нет":
                print("колли")
