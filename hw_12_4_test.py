import logging
import rt_with_exceptions
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r1 = rt_with_exceptions.Runner('Mini-Me', -5)
            for i in range(10):
                r1.walk()
            logging.info(f'"test_walk" выполнен успешно')
            self.assertEqual(r1.distance, 50)
        except ValueError as ve:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            r2 = rt_with_exceptions.Runner(22, 10)
            for i in range(10):
                r2.run()
            logging.info(f'"test_run" выполнен успешно')
            self.assertEqual(r2.distance, 100)
        except TypeError as te:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        r1 = rt_with_exceptions.Runner('Mini-Me')
        r2 = rt_with_exceptions.Runner('Tirion')
        for i in range(10):
            r1.walk()
        for i in range(10):
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)

    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()

