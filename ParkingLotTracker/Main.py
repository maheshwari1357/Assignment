from ParkingLot import ParkingLot
from VehicleNumberNotFoundException import VehicleNumberNotFoundException
parkingLot=ParkingLot()
while True:
		print("Welcome to Parking Lot Tracker!!")
		print("********************************")
		print("Press 1 to retrieve parking spot number of your vehicle")
		print("Press 2 to get you a parking spot assigned")
		print("Press 3 to get all vehicles parked (For Admin use only)")
		print("Press 4 to Exit the system")
		choice = int(input())
		if choice == 1:
			try:
				vehicleNumber = input("Please enter the vehicle number: ")
				spotNumber = parkingLot.retrieveParkingSpot(vehicleNumber)
				level = parkingLot.getLevel(spotNumber)
				print("Spot No: ",spotNumber, " Level: ", level)
				print(" ")
			except VehicleNumberNotFoundException:
				print("Exception Occured: Vehicle Number Invalid!!")
		elif choice == 2:
			vehicleNumber = input("Please enter the vehicle number: ")
			spotNumber = parkingLot.assignParkingSpot(vehicleNumber)
			level = parkingLot.getLevel(spotNumber)
			print("Spot Assigned: " ,spotNumber," Level: ", level)
			print(" ")
		elif choice == 3:
			password = input("Enter the admin password: ")
			print(parkingLot.getParkingMap(password))
		elif choice == 4:
			break
		else:
			print("Oops!...Invalid Choice!!")
			print(" ")