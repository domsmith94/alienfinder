# alienfinder
This is my solution to a coding exercise I completed that was set by one the UK's leading Digital Studios. I completed it late 2015 during my final year of university whilst applying to their Software Engineering graduate scheme. The code will be modified to keep the company anonymous in case the exercise is used in future years. Basically if you've somehow found this, don't bother copying it! I'm sure there are more elegant solutions! 

<h3>Brief (summarised)</h3>
<li>Need to find the exact location of an alien spacecraft</li> 
<li>universe is exactly 10 units wide by 10 units long</li>
<li>Craft moves in increments of 1 unit</li>
<li>Craft can only move forwards and turn to the left and the right rotating 90 degrees each time</li>
<li>Although we have not managed to track the final position of the alien craft we have managed to track its movements</li>
<li>The last position we managed to track for the aliens is row 1 column 0, after it made it's first move</li>

An API was also provided that had two methods - getdata and submitdata. A GET request to getdata returned a JSON containing the directions the ship made.

<b>Example of what getdata returned:</b>

“Directions”: {[“FORWARD”, “FORWARD”, “RIGHT”, “FORWARD”, “FORWARD”, “FORWARD”, “FORWARD”, “RIGHT”, “FORWARD”, “FORWARD”, “LEFT”, “FORWARD”, “RIGHT”, “LEFT”, “LEFT”, “FORWARD”, “FORWARD”, “FORWARD”, “LEFT”, “RIGHT”]}

submitdata was used to submit the final x and y co-ordinates of the solution and returned a success or failure message. 

<h3>Instructions</h3>
Run navsys.py + tests.py for the unit tests

The real solution used the API over the network, but I've removed this from the code for obvious reasons. Instead I've inserted the data returned by the API into data.json so the script will still function. Just run navsys.py :) 

<h3>Comments</h3>

Company estimated it would take roughly 8 hours, I managed it in roughly 4. Print statements make the code a little messy in my opinion but I wanted the user running it to see what was happening. Overall a fun little exercise and I would welcome any comments on the structure of my code and design choices. 



