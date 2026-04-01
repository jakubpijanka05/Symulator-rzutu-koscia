import pytest
from app.main import DiceSimulator

def test_roll_dice_standard():
    sim = DiceSimulator()
    rolls = sim.roll_dice(sides=6, num_dice=3)
    assert len(rolls) == 3
    assert all(1 <= r <= 6 for r in rolls)

def test_roll_dice_d20():
    sim = DiceSimulator()
    rolls = sim.roll_dice(sides=20, num_dice=1)
    assert len(rolls) == 1
    assert 1 <= rolls[0] <= 20

def test_invalid_parameters():
    sim = DiceSimulator()
    with pytest.raises(ValueError):
        sim.roll_dice(sides=1) # Kość musi mieć min. 2 ścianki
    with pytest.raises(ValueError):
        sim.roll_dice(sides=6, num_dice=0)

def test_statistics():
    sim = DiceSimulator()
    sim.roll_dice(sides=10, num_dice=5)
    stats = sim.get_statistics()
    assert stats["total_rolls"] == 5
    assert stats["min"] >= 1
    assert stats["max"] <= 10

def test_empty_statistics():
    sim = DiceSimulator()
    stats = sim.get_statistics()
    assert stats["total_rolls"] == 0
