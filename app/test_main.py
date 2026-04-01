import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (25, 25, [2, 2]),
    (29, 29, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_returns_list() -> None:
    assert isinstance(get_human_age(0, 0), list)


def test_returns_two_elements() -> None:
    assert len(get_human_age(10, 10)) == 2


def test_cat_first_15_years_equals_1_human_year() -> None:
    assert get_human_age(15, 0)[0] == 1


def test_dog_first_15_years_equals_1_human_year() -> None:
    assert get_human_age(0, 15)[1] == 1


def test_cat_next_9_years_give_1_more_human_year() -> None:
    assert get_human_age(24, 0)[0] == 2


def test_dog_next_9_years_give_1_more_human_year() -> None:
    assert get_human_age(0, 24)[1] == 2


def test_cat_every_4_years_after_24_give_1_extra_human_year() -> None:
    assert get_human_age(28, 0)[0] == 3


def test_dog_every_5_years_after_24_give_1_extra_human_year() -> None:
    assert get_human_age(0, 29)[1] == 3


def test_remainder_is_discarded_for_cat() -> None:
    assert get_human_age(27, 0)[0] == 2


def test_remainder_is_discarded_for_dog() -> None:
    assert get_human_age(0, 28)[1] == 2


def test_ages_are_independent() -> None:
    cat_only = get_human_age(28, 0)
    dog_only = get_human_age(0, 29)
    combined = get_human_age(28, 29)
    assert combined[0] == cat_only[0]
    assert combined[1] == dog_only[1]
