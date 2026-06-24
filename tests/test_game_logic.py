from logic_utils import (
    check_guess,
    get_attempt_limit_for_difficulty,
    get_range_for_difficulty,
)


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_numeric_string_secret_is_compared_numerically():
    outcome, _ = check_guess(10, "2")
    assert outcome == "Too High"


def test_easy_range_is_1_to_20():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range_is_1_to_50():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_range_is_1_to_100():
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_attempt_limit_matches_difficulty():
    assert get_attempt_limit_for_difficulty("Easy") == 6
    assert get_attempt_limit_for_difficulty("Normal") == 8
    assert get_attempt_limit_for_difficulty("Hard") == 5
