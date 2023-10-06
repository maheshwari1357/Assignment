from VehicleNumberNotFoundException import VehicleNumberNotFoundException
class ParkingLot:
	parkingMap={}  #vehicleNumber as a Key and parkingSpot will be corresponding value 
	spotOccupied=[] #List of Spots already occupied.

	def retrieveParkingSpot(self,vehicleNumber):
		if vehicleNumber in self.parkingMap:
			self.spotOccupied.remove(self.parkingMap[vehicleNumber])
			tmp = self.parkingMap[vehicleNumber]
			del self.parkingMap[vehicleNumber]
			return tmp
		else:
			raise VehicleNumberNotFoundException

	def assignParkingSpot(self,vehicleNumber):
		if vehicleNumber in self.parkingMap:
			print("Vehicle number already exists!!!....with below parking details")
			return self.parkingMap[vehicleNumber]
		for i in range(1,41):
			if i not in self.spotOccupied:
				self.parkingMap[vehicleNumber] = i
				self.spotOccupied.append(i)
				break
		return self.parkingMap[vehicleNumber]

	def getParkingMap(self,password):
		if password == "admin":
			return self.parkingMap
		else:
			return ("Incorrect Password")
	
	def getLevel(self,spotNumber):
		return ("A" if spotNumber<21 else "B")