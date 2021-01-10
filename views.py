from models import *


def create_parking_lot(args):
    """Takes in input param and and initialize the lot"""
    total_slots = int(args[1])
    status = ParkingLot.initialize(total_slots)
    if status == 'SUCCESS':
        print(f'Created parking of {total_slots} slots')


def park_vehicle(args):
    """Checks availability and parks the vehicle"""
    registration_no, driver_age = args[1], int(args[3])
    if not ParkingLot.check_availability():
        print('Parking Lot Full')
    else:
        vehicle = Vehicle(registration_no, driver_age)
        ParkingLot.add_vehicle(vehicle)
        print(f'Car with vehicle registration number "{vehicle.registration_no}" '
              f'has been parked at slot number {vehicle.slot_occupied}')


def vacate_slot(args):
    """Vacate slot"""
    slot = int(args[1])
    if slot in ParkingLot.heap:
        print('Slot already vacant')
    else:
        vehicle = ParkingLot.release_slot(slot)
        ParkingLot.remove_vehicle(vehicle)
        print(
            f'Slot number {slot} vacated, the car with vehicle registration number "{vehicle.registration_no}" left the space'
            f', the driver of the car was of age {vehicle.driver.age}')


def get_slot_number_of_a_vehicle(args):
    """Given a registration number of a vehicle, prints the slot occupied"""
    registration_no = args[1]
    found_flag = False
    for item in ParkingLot.vehicles:
        if item.registration_no == registration_no:
            print(item.slot_occupied)
            found_flag = True

    if not found_flag:
        print('Vehicle Not Found')


def get_list_of_vehicles_with_age(age):
    """Returns a list of all vehicle objects with same age"""
    arr = []
    for vehicle in ParkingLot.vehicles:
        if vehicle.driver.age == age:
            arr.append(vehicle)
    return arr


def get_slot_numbers(args):
    """Shows slot numbers of all drivers with the given age"""
    age = int(args[1])
    arr = get_list_of_vehicles_with_age(age)
    s = ''
    for item in arr:
        s = s + str(item.slot_occupied) + ','
    s = s[:-1]
    print(s)


def get_vehicle_numbers(args):
    """Shows vehicle registration numbers of all drivers with the given age"""
    age = int(args[1])
    arr = get_list_of_vehicles_with_age(age)
    s = ''
    for item in arr:
        s = s + '"' + item.registration_no + '"' + ','
    s = s[:-1]
    print(s)
