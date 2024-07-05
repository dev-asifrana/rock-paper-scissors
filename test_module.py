import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_quincy(self):
        print("Testing against quincy...")
        actual = play(player, quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected defeat percentage for quincy 60% of the time.')

    def test_player_vs_abbey(self):
        print("Testing against abbey...")
        actual = play(player, abbey, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected defeat percentage for abbey 60% of the time.')

    def test_player_vs_kris(self):
        print("Testing against kris...")
        actual = play(player, kris, 1000) >= 60
        self.assertTrue(
            actual, 'Expected defeat percentage for kris 60% of the time.')

    def test_player_vs_mrugesh(self):
        print("Testing against mrugesh...")
        actual = play(player, mrugesh, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected defeat percentage for mrugesh 60% of the time.')


if __name__ == "__main__":
    unittest.main()