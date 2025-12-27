label trump_on_island:
    "Танк и эпштейн идут в комнату откуда шел звонок"
    "В комнате они действительно встречают трампа"
    "А с трампом в комнате эйнштейн"
    if ein_score >= 1:
        jump ending_trump_island_good
    jump ending_trump_island_bad


label ending_trump_island_good:
    "Эйнштейн говорит что знает танка"
    "Эпштейн ахуел что энштейн не хуесос и умер"
    "Хорошая концовка с трампом и эйнштейном"
    return

label ending_trump_island_bad:
    "Трамп улетает с острова и кидает ядерку"
    "Все взорвались"
    "Бля(("
    return


label ending_island_ban:
    "Эпштейн забанил танка нахуй с острова"
    "Танк утопился"
    "Ретурн("
    return