import unittest
import navsys


class TestNavigationSystem(unittest.TestCase):

	def test_space_ship_class_north(self):
		for facing in (0, 1, 2, 3):	
			test_ship = navsys.Spaceship(4, 4, facing)

			self.assertEquals(test_ship.x, 4)
			self.assertEquals(test_ship.y, 4)

			self.assertEquals(test_ship.facingq[0], facing)

	def test_space_ship_move_left(self):
		test_ship = navsys.Spaceship(4, 4, 0)
		val = test_ship.move("LEFT")

		self.assertTrue(val)
		self.assertEquals(test_ship.facingq[0], 3)
		self.assertEquals(test_ship.x, 4)
		self.assertEquals(test_ship.y, 4)

	def test_space_ship_move_forward(self):
		test_ship = navsys.Spaceship(3, 7, 0)
		val = test_ship.move("FORWARD")

		self.assertTrue(val)
		self.assertEquals(test_ship.facingq[0], 0)
		self.assertEquals(test_ship.x, 3)
		self.assertEquals(test_ship.y, 8)

	def test_space_ship_edge_case_y(self):
		# Ship at edge of universe and shouldn't be allowed to make move, move() should return false
		test_ship = navsys.Spaceship(0, 9, 0)
		val = test_ship.move("FORWARD")

		self.assertFalse(val)
		self.assertEquals(test_ship.facingq[0], 0)
		self.assertEquals(test_ship.x, 0)
		self.assertEquals(test_ship.y, 9)

	def test_space_ship_edge_case_x(self):
		# Ship at edge of universe and shouldn't be allowed to make move, move() should return false
		test_ship = navsys.Spaceship(9, 9, 1)
		val = test_ship.move("FORWARD")

		self.assertFalse(val)
		self.assertEquals(test_ship.facingq[0], 1)
		self.assertEquals(test_ship.x, 9)
		self.assertEquals(test_ship.y, 9)

	def test_generate_possible_positions_return_type(self):
		test_data = ["FORWARD","FORWARD"]
		poss_positions = navsys.generate_possible_positions(test_data, 0, 1)

		self.assertEquals(type(poss_positions), list) # Should return a list of pairs
		self.assertEquals(type(poss_positions[0]), tuple) # This case should return 1 item in the list, which is a pair
		self.assertEquals(type(poss_positions[0][0]), int) # Checks the x value of the pair, should be an int
		self.assertEquals(type(poss_positions[0][1]), int) # Checks the y value of the pair, should be an int

	def test_generate_possible_positions_return_values_1(self):
		test_data = ["FORWARD","FORWARD"]
		poss_positions = navsys.generate_possible_positions(test_data, 0, 1)
		
		self.assertEquals(len(poss_positions), 3)

		north_cords = poss_positions[0]
		self.assertEquals(north_cords[0], 0)
		self.assertEquals(north_cords[1], 2)

		east_cords = poss_positions[1]
		self.assertEquals(east_cords[0], 1)
		self.assertEquals(east_cords[1], 1)

		south_cords = poss_positions[2]
		self.assertEquals(south_cords[0], 0)
		self.assertEquals(south_cords[1], 0)

	def test_generate_possible_positions_return_values_2(self):
		test_data = ["RIGHT","RIGHT", "RIGHT", "RIGHT", "FORWARD"] # Checks the ship rotates 270 degrees and moves one 
		poss_positions = navsys.generate_possible_positions(test_data, 2, 2)

		self.assertEquals(len(poss_positions), 4)

		north_cords = poss_positions[0]
		self.assertEquals(north_cords[0], 1)
		self.assertEquals(north_cords[1], 2)

		east_cords = poss_positions[1]
		self.assertEquals(east_cords[0], 2)
		self.assertEquals(east_cords[1], 3)

		south_cords = poss_positions[2]
		self.assertEquals(south_cords[0], 3)
		self.assertEquals(south_cords[1], 2)

		west_cords = poss_positions[3]
		self.assertEquals(west_cords[0], 2)
		self.assertEquals(west_cords[1], 1)


if __name__ == '__main__':
    unittest.main()