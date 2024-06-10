import datetime
import People

class HotelBookingSystem:
    def __init__(self):
        self.rooms = []
        self.bookings = []
        self.available_rooms = []
        self.customers = [] 

    def add_room(self, room_number, room_type, price):
        for room in self.rooms:
            if room["room_number"] == room_number:
                raise Exception("Room already exists")
        room = {"room_number": room_number, "room_type": room_type, "price": price}
        self.rooms.append(room)
        self.available_rooms.append(room)
        return "Room added successfully"
        
    def display_rooms(self):
        output = ""
        for room in self.rooms:
            output += f"Room Number: {room['room_number']}, Room Type: {room['room_type']}, Price: {room['price']}\n"
        return output
    
    def display_available_rooms(self):
        output = ""
        for room in self.available_rooms:
            output += f"Room Number: {room['room_number']}, Room Type: {room['room_type']}, Price: {room['price']}\n"
        return output
    
    def add_customer(self, name, age, cpf):
        customer = People.People(name, age, cpf)
        self.customers.append(customer)
        return "Customer added successfully"
        
    def display_customers(self):
        output = ""
        for customer in self.customers:
            output += customer.display() + "\n"
        return output
    
    def book_room(self, customer, room_number, checkin_date, checkout_date):
        if not customer.is_adult():
            raise Exception("Customer is not an adult")
        for room in self.available_rooms:
            if room["room_number"] == room_number:
                booking = {"customer_name": customer, "room_number": room_number, "checkin_date": checkin_date, "checkout_date": checkout_date}
                self.bookings.append(booking)
                self.available_rooms.remove(room)
                return f"Room {room_number} booked successfully"
        raise Exception("Room not available")

    def cancel_booking(self, room_number):
        if len(self.bookings) == 0:
            raise Exception("No bookings found")
        for booking in self.bookings:
            if booking["room_number"] == room_number:
                self.bookings.remove(booking)
                self.available_rooms.append({"room_number": room_number, "room_type": "", "price": 0})
                return f"Booking for room {room_number} cancelled successfully"
        raise Exception(f"Booking for room {room_number} not found")

    def display_bookings(self):
        output = ""
        for booking in self.bookings:
            output += f"Customer Name: {booking['customer_name'].name}, Room Number: {booking['room_number']}, Checkin Date: {booking['checkin_date']}, Checkout Date: {booking['checkout_date']}\n"
        return output
    