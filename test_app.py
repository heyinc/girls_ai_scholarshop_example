import pytest
from app import calc_rank


def test_calc_rank_red_velvet():
    track = {"artist": {"name": "Red Velvet"}}
    assert calc_rank(0, track, multiplier=100) == 100
    assert calc_rank(1, track, multiplier=100) == 200
    assert calc_rank(4, track, multiplier=100) == 500


def test_calc_rank_other_artist():
    track = {"artist": {"name": "BTS"}}
    assert calc_rank(0, track, multiplier=100) == 1
    assert calc_rank(1, track, multiplier=100) == 2
    assert calc_rank(4, track, multiplier=100) == 5


def test_calc_rank_case_insensitive():
    track = {"artist": {"name": "red velvet"}}
    assert calc_rank(2, track, multiplier=50) == 150
    track = {"artist": {"name": "RED VELVET"}}
    assert calc_rank(2, track, multiplier=50) == 150


def test_calc_rank_missing_artist():
    track = {"artist": {}}
    assert calc_rank(0, track, multiplier=100) == 1
    track = {}
    assert calc_rank(0, track, multiplier=100) == 1
