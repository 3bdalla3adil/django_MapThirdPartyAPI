from nextbillion_directions import *
from nextbillion_distance_matrix import *
from nextbillion_geocoding import *

from serper_dev import *

import requests

def get_location_info(*args):#origin,destination,origins,destinations,q,gl,hl,autocorrect
	
	num1= get_directions("31.16394201,36.02416130" , "31.66304341,35.96562838")
	num2= get_distance_matrix("31.16394201,36.02416130" , "31.66304341,35.96562838")
	num3= get_geocoding("31.16394201,36.02416130" , "31.66304341,35.96562838")
	num4= get_location("apple inc","us","en",True)

	return  "{} | {} | {} | {} ".format(num1,num2,num3,num4)

if __name__ == '__main__':
	print(get_location_info())


#API VIEW Code