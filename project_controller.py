from views import *


def route(line):
    values = line.split()
    if values[0] == 'Create_parking_lot':
        create_parking_lot(values)
    elif values[0] == 'Park':
        park_vehicle(values)
    elif values[0] == 'Slot_numbers_for_driver_of_age':
        get_slot_numbers(values)
    elif values[0] == 'Slot_number_for_car_with_number':
        get_slot_number_of_a_vehicle(values)
    elif values[0] == 'Leave':
        vacate_slot(values)
    elif values[0] == 'Vehicle_registration_number_for_driver_of_age':
        get_vehicle_numbers(values)
