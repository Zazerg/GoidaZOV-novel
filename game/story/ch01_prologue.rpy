label ch01_moscow:

    play music "diddy-blud-no-voc.wav"
    scene moscow with pixellate

    "В один солнечный день обычный танк ехал по самому обычному городу"

    show tank at right with moveinright

    t "Я ебучий танк хуярю по Москве"

    t "О нихуя это че за объявление"

    window hide
    show svo_ad at truecenter with zoomin

    pause
    window auto True

    t "Денежные выплаты! " with vpunch
    extend "От 5200000 денег! " with vpunch
    extend "И это только за год?!! " with vpunch
    extend "Я так даже смогу купить еды!" with vpunch

    menu:
        "Упускать такую возможность никак нельзя!":
            jump dep
        "Это явно не так просто как кажется...":
            jump bad_ending_1


label bad_ending_1:
    scene black with dissolve
    "Танк так и не решился поехать на СВО..."
    "Всю свою оставшуюся жизнь он прожил в нищете и умер в канализации."
    return
