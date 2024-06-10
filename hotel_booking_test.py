import unittest
from hotel_booking import HotelBookingSystem
import People
import datetime

class TestHotelBookingSystem(unittest.TestCase):
    def setUp(self):
        self.hotel = HotelBookingSystem()
        self.customer1 = People.People("John Doe", 25, "123456789")
        self.customer2 = People.People("Jane Doe", 30, "987654321")

    def test_add_room(self):
        self.assertEqual(self.hotel.add_room(101, "Single", 100), "Room added successfully")
        self.assertRaises(Exception, self.hotel.add_room, 101, "Single", 100)

    def test_display_rooms(self):
        self.hotel.add_room(101, "Single", 100)
        self.hotel.add_room(102, "Double", 200)
        expected_output = "Room Number: 101, Room Type: Single, Price: 100\nRoom Number: 102, Room Type: Double, Price: 200\n"
        self.assertEqual(self.hotel.display_rooms(), expected_output)

    def test_display_available_rooms(self):
        self.hotel.add_room(101, "Single", 100)
        self.hotel.add_room(102, "Double", 200)
        expected_output = "Room Number: 101, Room Type: Single, Price: 100\nRoom Number: 102, Room Type: Double, Price: 200\n"
        self.assertEqual(self.hotel.display_available_rooms(), expected_output)

    def test_add_customer(self):
        self.assertEqual(self.hotel.add_customer("John Doe", 25, "123456789"), "Customer added successfully")

    def test_display_customers(self):
        self.hotel.add_customer("John Doe", 25, "123456789")
        self.hotel.add_customer("Jane Doe", 30, "987654321")
        expected_output = "Name: John Doe, Age: 25, CPF: 123456789\nName: Jane Doe, Age: 30, CPF: 987654321\n"
        self.assertEqual(self.hotel.display_customers(), expected_output)

    def test_book_room(self):
        self.hotel.add_room(101, "Single", 100)
        self.assertEqual(self.hotel.book_room(self.customer1, 101, datetime.date(2022, 1, 1), datetime.date(2022, 1, 3)), "Room 101 booked successfully")
        self.assertRaises(Exception, self.hotel.book_room, self.customer2, 101, datetime.date(2022, 1, 1), datetime.date(2022, 1, 3))

    def test_cancel_booking(self):
        self.hotel.add_room(101, "Single", 100)
        self.hotel.book_room(self.customer1, 101, datetime.date(2022, 1, 1), datetime.date(2022, 1, 3))
        self.assertEqual(self.hotel.cancel_booking(101), "Booking for room 101 cancelled successfully")
        # self.assertRaises(Exception, self.hotel.cancel_booking, 101)

    def test_display_bookings(self):
        self.hotel.add_room(101, "Single", 100)
        self.hotel.add_room(102, "Double", 200)
        self.hotel.book_room(self.customer1, 101, datetime.date(2022, 1, 1), datetime.date(2022, 1, 3))
        self.hotel.book_room(self.customer2, 102, datetime.date(2022, 1, 5), datetime.date(2022, 1, 7))
        expected_output = "Customer Name: John Doe, Room Number: 101, Checkin Date: 2022-01-01, Checkout Date: 2022-01-03\nCustomer Name: Jane Doe, Room Number: 102, Checkin Date: 2022-01-05, Checkout Date: 2022-01-07\n"
        self.assertEqual(self.hotel.display_bookings(), expected_output)

if __name__ == "__main__":
    unittest.main()