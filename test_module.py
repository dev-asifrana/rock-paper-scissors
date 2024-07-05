import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class TestRPSPlayer(unittest.TestCase):

    def test_quincy(self):
        results = play(player, quincy, 1000)
        print("Results against Quincy:", results)
        win_rate = results  # Directly use results if it's a float representing the win rate
        self.assertGreaterEqual(win_rate, 0.6, "Win rate against Quincy is less than 60%")

    def test_abbey(self):
        results = play(player, abbey, 1000)
        print("Results against Abbey:", results)
        win_rate = results
        self.assertGreaterEqual(win_rate, 0.6, "Win rate against Abbey is less than 60%")

    def test_kris(self):
        results = play(player, kris, 1000)
        print("Results against Kris:", results)
        win_rate = results
        self.assertGreaterEqual(win_rate, 0.6, "Win rate against Kris is less than 60%")

    def test_mrugesh(self):
        results = play(player, mrugesh, 1000)
        print("Results against Mrugesh:", results)
        win_rate = results
        self.assertGreaterEqual(win_rate, 0.6, "Win rate against Mrugesh is less than 60%")

if __name__ == "__main__":
    unittest.main()
