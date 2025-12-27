screen shooting_gallery(time_limit=10.0, target_goal=5):

    modal True

    default score = 0
    default shots = 0
    default t_left = time_limit
    default target_x = 500
    default target_y = 300
    default target_visible = True

    add "mariupol"

    # Ловим "выстрел мимо" кликом по фону
    button:
        xfill True
        yfill True
        background None
        action SetScreenVariable("shots", shots + 1)

    # Мишень поверх фона
    if target_visible:
        imagebutton:
            idle "target_h"
            hover "target_h"
            xpos target_x
            ypos target_y
            action [
                SetScreenVariable("shots", shots + 1),  # если хочешь считать выстрел и при попадании
                SetScreenVariable("score", score + 1),
                SetScreenVariable("target_visible", False),
            ]

    frame:
        xalign 0.02 yalign 0.02
        vbox:
            text "Очки: [score]/[target_goal]"
            text "Выстрелы: [shots]"
            text "Время: [t_left:.1f]"

    timer 0.05 repeat True action [
        SetScreenVariable("t_left", max(0.0, t_left - 0.05)),
        If(not target_visible,
            [
                SetScreenVariable("target_x", renpy.random.randint(100, 1100)),
                SetScreenVariable("target_y", renpy.random.randint(120, 600)),
                SetScreenVariable("target_visible", True),
            ],
            []
        ),
        If(score >= target_goal,
            Return({"win": True, "score": score, "shots": shots, "time_left": t_left}),
            None
        ),
        If(t_left <= 0.0,
            Return({"win": False, "score": score, "shots": shots, "time_left": 0.0}),
            None
        ),
    ]
