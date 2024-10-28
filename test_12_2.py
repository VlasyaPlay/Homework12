from runner_and_tournament import Tournament, Runner
import unittest


class TournamentTest(unittest.TestCase):
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner('Усейн',10)
        self.runner_andrey = Runner('Андрей', 9)
        self.runner_nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_num, result in cls.all_results.items():
            print(f'Test {test_num}: {result}')

    def test_usain_and_nik(self):
        tournament = Tournament(90, [self.runner_usain, self.runner_nik])
        results = tournament.start()

        TournamentTest.all_results[1] = {k: v.name for k, v in results.items()}

        last_position = max(results.keys())
        self.assertTrue(results[last_position].name == 'Ник')

    def test_andrey_and_nik(self):
        tournament = Tournament(90, [self.runner_andrey, self.runner_nik])
        results = tournament.start()

        TournamentTest.all_results[2] = {k: v.name for k, v in results.items()}

        last_position = max(results.keys())
        self.assertTrue(results[last_position].name == 'Ник')

    def test_usain_andrey_and_nik(self):
        tournament = Tournament(90, [self.runner_usain, self.runner_andrey, self.runner_nik])
        results = tournament.start()

        TournamentTest.all_results[3] = {k: v.name for k, v in results.items()}

        last_position = max(results.keys())
        self.assertTrue(results[last_position].name == 'Ник')


if __name__ == "__main__":
    unittest.main()




