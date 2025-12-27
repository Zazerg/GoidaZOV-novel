label mp:
    "Выбор куда пойти"
    menu:
        "Комната для массажа" if island_avail["massage"]:
            jump massage_room
        "Главный выход":
            jump main_exit
        "Пожарный выход":
            jump fire_exit
        "Комната, помеченная как Z":
            jump Z_room
        "Зал для вечеринок" if island_avail["party_room"]:
            jump party_room
