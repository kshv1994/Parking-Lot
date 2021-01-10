from heapq import heapify, heappush, heappop


class Actor:
    """Actors in the system"""
    def __init__(self, name=None, age=0, phone_number=None, is_admin=False):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.is_admin = is_admin


class Admin(Actor):
    """Admin demographics"""
    def __init__(self, name=None, age=0, phone_number=None):
        super().__init__(name, age, phone_number, True)


class Driver(Actor):
    """Driver demographics"""
    def __init__(self, name=None, age=0, phone_number=None):
        super().__init__(name, age, phone_number, False)


class Slot:
    """Stores the vehicle object parked in slot"""

    def __init__(self, slot_id=0, vehicle=None):
        """Initializes the instance variables"""
        self.id = slot_id
        self.vehicle = vehicle

    def get_vehicle(self):
        """Returns the vehicle object stored at the slot"""
        return self.vehicle


class ParkingLot:
    """Class that stores the meta-data as well as state of all the slots"""
    total_slots = 0
    heap = []
    slots = []
    vehicles = []

    @staticmethod
    def initialize(total_slots=0):
        """Initializes the data store with the total slots taken as input"""
        ParkingLot.total_slots = total_slots
        ParkingLot.slots = [None for i in range(total_slots)]
        ParkingLot.heap = [i+1 for i in range(total_slots)]
        heapify(ParkingLot.heap)
        return 'SUCCESS'

    @staticmethod
    def check_availability():
        """Checks and returns whether the lot is full or not"""
        if len(ParkingLot.heap):
            return True
        return False

    @staticmethod
    def occupy_slot(vehicle):
        """Returns the closest slot available to entry gate"""
        vacant_slot = heappop(ParkingLot.heap)
        slot = Slot(vacant_slot, vehicle)
        ParkingLot.slots[vacant_slot-1] = slot
        return vacant_slot

    @staticmethod
    def release_slot(slot):
        """Takes the slot which is vacated and adds it to the available slot data structure"""
        vehicle = ParkingLot.slots[slot - 1].get_vehicle()
        ParkingLot.slots[slot - 1] = None
        heappush(ParkingLot.heap, slot)
        return vehicle

    @staticmethod
    def add_vehicle(vehicle):
        """Add vehicle to the list of vehicles parked"""
        ParkingLot.vehicles.append(vehicle)

    @staticmethod
    def remove_vehicle(vehicle):
        """Remove vehicle to the list of vehicles parked assuming numbers are unique"""
        ParkingLot.vehicles.remove(vehicle)


class Vehicle:
    """stores metadata of the vehicle which came for parking"""

    def __init__(self, registration_no='', driver_age=None):
        """Registers the vehicle and assigns a slot to it"""
        self.registration_no = registration_no
        self.driver = Driver('Unknown', driver_age, None)
        self.slot_occupied = ParkingLot.occupy_slot(self)
