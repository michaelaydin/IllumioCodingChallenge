Illumio Coding Challenge

a.  I tested my solution by creating a csv with the given rules, passing that in to an instatiated firewall, and checking the results    
of the given test cases.  I also added some edge cases, but if I had more time I would've thought of more and fancier edge cases.  
b. I used a dictionary of dictionary of dictionaries to group the direction, protocol, port, and ip because dictionaries have an average 
lookup time of O(1).  
c. The dictionary system I used uses a lot of space so maye think of a different data strucutre to use that sacrifices some lookup time  
for less space.  I also need to test more edge cases.  A bug I'm pretty sure is in my code but I didn't have time to test for is if
multiple rules are given for the same port involving different IP address ranges.  In the for loop in my accept_packet function I do
not think this would be accounted for.
d. The instructions are good.

I am particularly interested in the policy team. 
