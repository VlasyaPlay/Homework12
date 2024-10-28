import unittest
import test_12_1, test_12_3


runner_and_tournamentTS = unittest.TestSuite()
runner_and_tournamentTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
runner_and_tournamentTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_and_tournamentTS)
