"""Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
Result:
243"""

import numpy as np
l = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
rounded_l = [round(x) for x in l]
np_rl = np.array(rounded_l)
print(np.sum(np_rl) * len(l))