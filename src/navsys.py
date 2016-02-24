import urllib2
import json
from collections import deque

EMAIL_ADDRESS = 'domsmith94@gmail.com'
API_URL = None # Removed URL to hide company.

X_MAX = 10
Y_MAX = 10


class Spaceship:
	
	def __init__(self, x, y, facing):
		self.x = x 
		self.y = y 
		self.facingq = deque([0, 1, 2, 3]) 
		self.facingq.rotate(-facing) 

		# Note that X and Y values in this example relate to the co-ordinates after one move. 
		# Double ended queue used represents the 4 possible directions the ship can be facing.
		# Mapped as follows {North: 0, East: 1. South: 2, West: 3}. The first value, facingq[0]
		# indicates the direction the Ship is currently facing. Such that facingq[0] = 1 means
		# ship is facing North direction. 


	def move(self, direction):
		if direction == 'LEFT':
			self.facingq.rotate(1)
	
		elif direction == 'RIGHT':
			self.facingq.rotate(-1)
		
		elif direction == 'FORWARD':
			if self.facingq[0] == 0 and self.y < Y_MAX-1:
				self.y = self.y + 1
			
			elif self.facingq[0] == 1 and self.x < X_MAX-1:
				self.x = self.x + 1
			
			elif self.facingq[0] == 2 and self.y > 0:
				self.y = self.y - 1
		
			elif self.facingq[0] == 3 and self.x > 0:
				self.x = self.x - 1
	
			else:
				return False

		print("Direction was {}, ship now at {},{}".format(direction, self.x, self.y))
		return True

		# Returns True is move could be made, False if it could not such that ship is at end
		# of universe. Length of universe specified in Y_MAX and X_MAX constants. 

def generate_possible_positions(directions, x, y):
	possible_posistions = []
	directions.pop(0)

	for start_direction in (0, 1, 2, 3):
		out_of_bounds = False
		ship = Spaceship(x, y, start_direction)

		for direction in directions:
			if not ship.move(direction):
				out_of_bounds = True
				break

		if out_of_bounds:
			print("\nSpaceship went off the face of the universe for start direction {}".format(start_direction))
			print("=================================================================\n")
		else:
			possible_posistions.append((ship.x, ship.y))
			print('\n====== Spaceship starting at {} predicted to be at: ==='.format(start_direction))
			print "Final estimated direction is ROW: {}, COLUMN: {}".format(ship.y, ship.x)
			print("=================================================================\n")
			

	return possible_posistions

	# We remove the first direction from list as given co-ordinates are after ship has made it's first move.
	# There are up to 4 possible start positions (facing North, South, East, West) so we find
	# all the solutions. We iterate through each direction in directions and apply the direction
	# to Ships current position, keeping of track when/if a ship goes off the universe. 


if __name__ == '__main__':
	#url = API_URL + 'getdata/' + EMAIL_ADDRESS # Not functional due to removing URL to hide company.
	#response = urllib2.urlopen(url) Commented out as we are not using the HTTP API call.

	with open('../sample_data/1.json') as data_file:
		json_data = json.load(data_file)

	#json_data = json.load(response)

	directions = json_data["Directions"]
	possible_posistions = generate_possible_positions(directions, 0, 1)

	if len(possible_posistions) == 1:
		print('\n1 possible posistion was found.')
		user_response = raw_input('\nDo you wish to send off the results and stop this madness? (y/n)\n')

		# Used for submitting results of coding challenge. Not in use as URL has been removed
		if user_response.lower() == 'y':
			url = API_URL + 'submitdata/' + EMAIL_ADDRESS + '/{}/{}'.format(possible_posistions[0][0], possible_posistions[0][1])
			print url
			response = urllib2.urlopen(url)
			json_response = json.load(response)

			if json_response["StatusCode"] == 200:
				print "Success!"
				print json_response["Message"]
			else:
				print ("Not quite right!")
				print json_response["Message"]