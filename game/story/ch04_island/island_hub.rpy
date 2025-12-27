label mp:
    "Выбор куда пойти"
    menu:
        "Комната для массажа" if map_avail_massage:
            jump massage_room
        "Главный выход":
            jump main_exit
        "Пожарный выход":
            jump fire_exit
        "Комната, помеченная как Z":
            jump Z_room
        "Зал для вечеринок":
            jump party_room
