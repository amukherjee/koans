#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

import random

class DiceSet(object):
    def __init__(self):
        self._values = []

    @property
    def values(self):
        return self._values

    def roll(self, n):
        # Needs implementing!
        # Tip: random.randint(min, max) can be used to generate random numbers
        for roll in range(0, n):
            self._values.append(random.randint(1, 6))

        return self._values

class AboutDiceProject(Koan):
    def test_can_create_a_dice_set(self):
        dice = DiceSet()
        self.assertTrue(dice)

    def test_rolling_the_dice_returns_a_set_of_integers_between_1_and_6(self):
        dice = DiceSet()

        dice.roll(5)
        self.assertTrue(isinstance(dice.values, list), "should be a list")
        self.assertEqual(5, len(dice.values))
        for value in dice.values:
            self.assertTrue(value >= 1 and value <= 6, "value " + str(value) + " must be between 1 and 6")

    def test_dice_values_do_not_change_unless_explicitly_rolled(self):
        dice = DiceSet()
        dice.roll(5)
        first_time = dice.values
        second_time = dice.values
        self.assertEqual(first_time, second_time)

    def test_dice_values_should_change_between_rolls(self):
        dice1 = DiceSet()
        dice2 = DiceSet()

        dice1.roll(5)
        first_time = dice1.values

        dice2.roll(5)
        second_time = dice2.values

        self.assertNotEqual(first_time , second_time, \
            "Two rolls should not be equal")

        # THINK ABOUT IT:
        #
        # If the rolls are random, then it is possible (although not
        # likely) that two consecutive rolls are equal.  What would be a
        # better way to test this?

    def test_you_can_roll_different_numbers_of_dice(self):
        dice1 = DiceSet()
        dice2 = DiceSet()

        dice1.roll(3)
        self.assertEqual(3, len(dice1.values))

        dice2.roll(1)
        self.assertEqual(1, len(dice2.values))
