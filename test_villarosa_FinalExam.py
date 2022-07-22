import unittest
from villarosa_FinalExam import Restaurant_Reservation_System


class TestReservation(unittest.TestCase):
    def test_reserve1(self):
        #arrange
        #act
        #assert
        self.assertEqual(obj.name, "jasper")

    def test_reserve2(self):
        self.assertNotEqual(obj.time, "3:00 pm")

    def test_reserve3(self):
        self.assertTrue(obj.no_child, "3")

obj = Restaurant_Reservation_System("jasper", "03/12/12", "4:45 pm", "5", "3")

if __name__ == '__main__':
    unittest.main()