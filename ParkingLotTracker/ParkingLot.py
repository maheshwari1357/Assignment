from VehicleNumberNotFoundException import VehicleNumberNotFoundException
parkingMap={}  #vehicleNumber as a Key and parkingSpot will be corresponding value 
spotOccupied=[] #List of Spots already occupied.

class ParkingLot:
	def retrieveParkingSpot(vehicleNumber):
		if vehicleNumber in parkingMap:
			spotOccupied.remove(parkingMap[vehicleNumber])
			tmp = parkingMap[vehicleNumber]
			del parkingMap[vehicleNumber]
			return tmp
		else:
			raise VehicleNumberNotFoundException

	def assignParkingSpot(vehicleNumber):
		if vehicleNumber in parkingMap:
			print("Vehicle number already exists!!!....with below parking details")
			return parkingMap[vehicleNumber]
		for i in range(1,41):
			if i not in spotOccupied:
				parkingMap[vehicleNumber] = i
				spotOccupied.append(i)
				break
		return parkingMap[vehicleNumber]

	def getParkingMap(password):
		if password == "admin":
			return parkingMap
		else:
			return ("Incorrect Password")
	
	def getLevel(spotNumber):
		return ("A" if spotNumber<21 else "B")