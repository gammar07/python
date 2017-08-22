'''
things to add: 
- change date string to datetime
- add calendar for bookables?
- 
'''

class Calendar(object):
    def __init__(self):
        self.entries = {}

    def add_entry(self, slot,record): #add record to parameters
        self.entries[slot] = record #should be qual to record once it's added.

    def __str__(self):
        return str(self.entries)
    
class Bookable(object):

    
    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def is_available(self, booking_class):
        return self.get_items(booking_class) > 0
    
    def make_reservation(self, customer, booking_class, reservation_date):
        if customer.wallet<=self.price[booking_class]: #square brackets to access dict
            return print('Reservation could not be made, not sufficient funds')
        elif self.is_available(booking_class):
            self.decrement_items(booking_class)
            customer.wallet -= self.price[booking_class]
            customer.make_reservation(reservation_date,booking_class)
            return print('Reservation made for ' + customer.full_name + ', funds left ' + str(customer.wallet))
        else:
            return print('No capacity, reservation not possible')
            
                
class Hotel(Bookable):
    
    def __init__(self,name):
        super().__init__(name) #pass the paremeter name
        
        self.rooms = {'Penthouse': 10,
                  'King Deluxe Bedroom': 20,
                  'Queen Deluxe Bedroom': 20,
                  'King Standard Bedroom': 30,
                  'Queen Standard Bedroom': 50}
    
        self.price = {'Penthouse'            : 1000,
                  'King Deluxe Bedroom'    : 700,
                  'Queen Deluxe Bedroom'   : 600,
                  'King Standard Bedroom' : 450,
                  'Queen Standard Bedroom': 350 }
    
    def get_items(self, booking_class):
        return self.rooms[booking_class]
        
    def decrement_items(self, booking_class):
        self.rooms[booking_class] -= 1
    
class Airline(Bookable):
    
    
    def __init__(self,name):
        super().__init__(name) #pass the paremeter name
        self.seats = {'Business Class' : 50,
                    'First Class'    : 50,
                    'Premium Economy': 100,
                    'Regular Economy': 150 }
    
        self.price = {'Business Class' : 2500,
                    'First Class'    : 2000,
                    'Premium Economy': 1800,
                    'Regular Economy': 1500 }
        
    def get_items(self, booking_class):
        return self.seats[booking_class]
        
    def decrement_items(self, booking_class):
        self.seats[booking_class] -= 1

class Customer(object):
    
    def __init__(self, f_name, l_name, id_no, wallet):
        self.f_name = f_name
        self.l_name = l_name
        self.id_no = id_no
        self.full_name = self.f_name + " " + self.l_name
        self.wallet = wallet
        self.calendar = Calendar()
          
    def get_record(self):
        return {
            'name': self.full_name,
            'funds': self.wallet
        }
    
    def make_reservation(self, slot, record):
        self.calendar.add_entry(slot, record)


h1 = Hotel('Sheraton')
a1 = Airline('RyanAir')
c1 = Customer('John','Doe',1,2000)
a1.make_reservation(c1, 'Regular Economy', '12-06-2017')
h1.make_reservation(c1, 'Penthouse', '12-06-2017')
h1.make_reservation(c1, 'King Standard Bedroom', '12-06-2017')