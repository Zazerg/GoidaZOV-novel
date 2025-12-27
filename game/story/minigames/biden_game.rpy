init python:
    import random

    def biden_choose(total, target=67, max_add=10):
        need = target - total
        if 1 <= need <= max_add:
            return need

        mod = max_add + 1
        desired = target % mod  # для 67 и 10 это 1

        for x in range(1, max_add + 1):
            nt = total + x
            if nt < target and (nt % mod) == desired:
                return x

        safe = [x for x in range(1, max_add + 1) if total + x <= target]
        if safe:
            weights = [x for x in safe]
            return random.choices(safe, weights=weights, k=1)[0]

        return random.randint(1, max_add)


screen biden_67_game(target=67, max_add=10):

    modal True

    default total = 0
    default turn = "player"      # "player" | "biden"
    default last_move = ""
    default info = "Твой ход: выбери число 1..10."

    # Байден ходит автоматически, когда его очередь
    if turn == "biden":
        $ b = biden_choose(total, target, max_add)
        # Маленькая пауза для ощущения хода (можно убрать)
        timer 0.3 action [
            SetScreenVariable("total", total + b),
            SetScreenVariable("last_move", "Байден добавил [b]."),
            # Проверка исходов после хода Байдена
            If(total + b == target,
                Return({"win": False, "reason": "biden_hit_67", "total": total + b}),
                If(total + b > target,
                    Return({"win": True, "reason": "biden_over_67", "total": total + b}),
                    [
                        SetScreenVariable("turn", "player"),
                        SetScreenVariable("info", "Твой ход: выбери число 1..10."),
                    ]
                )
            )
        ]

    add Solid("#0008")

    frame:
        xalign 0.5
        yalign 0.15
        padding (20, 15)
        vbox:
            spacing 8
            text "Игра в 67" size 42
            text "Сумма: [total] / [target]" size 30
            text "[last_move]" size 22
            text "[info]" size 22

    frame:
        xalign 0.5
        yalign 0.55
        padding (20, 20)

        vbox:
            spacing 10
            text "Выбери число:" size 26

            grid 5 2:
                spacing 10
                for x in range(1, max_add + 1):
                    textbutton "[x]":
                        sensitive (turn == "player")
                        action [
                            # ход игрока
                            SetScreenVariable("total", total + x),
                            SetScreenVariable("last_move", "Ты добавил [x]."),
                            # проверка исходов после хода игрока
                            If(total + x == target,
                                Return({"win": True, "reason": "player_hit_67", "total": total + x}),
                                If(total + x > target,
                                    Return({"win": False, "reason": "player_over_67", "total": total + x}),
                                    [
                                        SetScreenVariable("turn", "biden"),
                                        SetScreenVariable("info", "Ход Байдена..."),
                                    ]
                                )
                            )
                        ]

    textbutton "Сдаться":
        xalign 0.98
        yalign 0.95
        action Return({"win": False, "reason": "give_up", "total": total})
