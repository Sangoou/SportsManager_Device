#!/usr/bin/env python
GAME_START = 0
GAME_END = 1
GAME_PAUSE = 2
GAME_SET_END = 3


# Game Class
class Game:
    __team_id = {"A": "", "B": ""}
    __team_score = {"A": 0, "B": 0}
    __team_set_score = {'A': 0, "B": 0}

    __win_score = 5
    __win_set_score = 2
    __state = 0

    @staticmethod
    def set_team_id(team, id):
        Game.__team_id[team] = id

    @staticmethod
    def set_win_score(score):
        Game.__win_score = score

    @staticmethod
    def set_win_set_score(score):
        Game.__win_set_score = score

    @staticmethod
    def game_init():
        Game.__team_score = {"A": 0, "B": 0}
        Game.__team_set_score = {'A': 0, "B": 0}

    @staticmethod
    def score_increase(team) -> bool:
        if Game.__team_score[team] >= Game.__win_score:
            return False
        Game.__team_score[team] += 1
        if Game.__team_score[team] < Game.__win_score:
            return False
        Game.__team_set_score[team] += 1

        if not Game.is_end():
            Game.__team_score = {"A": 0, "B": 0}
        return True

    @staticmethod
    def score_decrease(team) -> bool:
        if Game.__team_score[team] > 0:
            Game.__team_score[team] -= 1
            return True
        return False

    @staticmethod
    def is_end() -> bool:
        return max(Game.__team_set_score.values()) >= Game.__win_set_score

    @staticmethod
    def get_winner() -> str:
        if Game.is_end():
            return 'A' if Game.__team_set_score["A"] > Game.__team_set_score["B"] else 'B'
        return False

    @staticmethod
    def get_team() -> dict:
        return Game.__team_id

    @staticmethod
    def get_score() -> dict:
        return Game.__team_score

    @staticmethod
    def get_set_score() -> dict:
        return Game.__team_set_score

    @staticmethod
    def get_win_score() -> int:
        return Game.__win_score

    @staticmethod
    def get_win_set_score() -> int:
        return Game.__win_set_score
