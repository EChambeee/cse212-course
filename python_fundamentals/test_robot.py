import unittest
from robot import Robot

class TestRobot(unittest.TestCase):
    def test_move_forward_changes_position(self):
        robot = Robot()
        start_position = robot.get_position()  # Adjust if needed
        robot.move_forward()
        end_position = robot.get_position()
        self.assertNotEqual(start_position, end_position)

if __name__ == '__main__':
    unittest.main()
