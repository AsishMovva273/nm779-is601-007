from enum import Enum
import sys

# Import custom exceptions from the PumpkinMachineExceptions module
from PumpkinMachineExceptions import (
    ExceededRemainingChoicesException,
    InvalidChoiceException,
    InvalidStageException,
    NeedsCleaningException,
    OutOfStockException,
    InvalidPaymentException,
)

class Usable:
    def _init_(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if self.quantity < 0:
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def _repr_(self):
        return self.name

class Pumpkin(Usable):
    pass

class FaceStencil(Usable):
    pass

class Extra(Usable):
    pass

class STAGE(Enum):
    Pumpkin = 1
    FaceStencil = 2
    Extra = 3
    Pay = 4

class PumpkinMachine:
    USES_UNTIL_CLEANING = 15
    MAX_STENCILS = 3
    MAX_EXTRAS = 3

    def _init_(self):
        # Initialize pumpkins, face stencils, and extras
        self.pumpkins = [
            Pumpkin(name="Mini Pumpkin", cost=1),
            Pumpkin(name="Small Pumpkin", cost=2),
            Pumpkin(name="Medium Pumpkin", cost=2.5),
            Pumpkin(name="Large Pumpkin", cost=3),
        ]
        self.face_stencils = [
            FaceStencil(name="Happy Face", quantity=10, cost=1),
            FaceStencil(name="Scream Face", quantity=10, cost=1),
            FaceStencil(name="Toothy Face", quantity=10, cost=1),
            FaceStencil(name="Spooky Face", quantity=10, cost=1),
        ]
        self.extras = [
            Extra(name="Small Candle", quantity=10, cost=0.25),
            Extra(name="LED Candle", quantity=10, cost=0.25),
            Extra(name="Spooky Sound Effects", quantity=10, cost=1.25),
            Extra(name="Sticker Pack", quantity=10, cost=1.00),
            Extra(name="Paint Kit", quantity=10, cost=3),
            Extra(name="Dry Ice", quantity=10, cost=0.25),
            Extra(name="Googly Eyes", quantity=10, cost=0.25),
            Extra(name="Glitter", quantity=10, cost=0.25),
        ]

        # Initialize machine parameters and variables
        self.remaining_uses = self.USES_UNTIL_CLEANING
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.total_sales = 0
        self.total_products = 0
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def pick_pumpkin(self, choice):
        if self.currently_selecting != STAGE.Pumpkin:
            raise InvalidStageException
        for c in self.pumpkins:
            if c.name.lower() == choice.lower() and c.in_stock():
                c.use()
                self.inprogress_pumpkin.append(c)
                return
        raise InvalidChoiceException

    def pick_face_stencil(self, choice):
        if self.currently_selecting != STAGE.FaceStencil:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_stencils <= 0:
            raise ExceededRemainingChoicesException
        for f in self.face_stencils:
            if f.name.lower() == choice.lower() and f.in_stock():
                f.use()
                self.inprogress_pumpkin.append(f)
                self.remaining_stencils -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_extras(self, choice):
        if self.currently_selecting != STAGE.Extra:
            raise InvalidStageException
        if self.remaining_extras <= 0:
            raise ExceededRemainingChoicesException
        for t in self.extras:
            if t.name.lower() == choice.lower() and t.in_stock():
                t.use()
                self.inprogress_pumpkin.append(t)
                self.remaining_extras -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        # Reset the machine for a new pumpkin
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def clean_machine(self):
        # Clean the machine
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_pumpkin_choice(self, pumpkin):
        # Handle pumpkin choice
        self.pick_pumpkin(pumpkin)
        self.currently_selecting = STAGE.FaceStencil

    def handle_face_stencil_choice(self, face_stencil):
        if face_stencil == "next":
            self.currently_selecting = STAGE.Extra
        else:
            self.pick_face_stencil(face_stencil)

    def handle_extra_choice(self, extra):
        if extra == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_extras(extra)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your Pumpkin and Happy Halloween!")
            self.total_products += 1
            self.total_sales += expected
            self.reset()
        else:
            raise InvalidPaymentException

    def print_current_pumpkin(self):
        # Print the current pumpkin in progress
        print(f"Current Pumpkin: {', '.join([x.name for x in self.inprogress_pumpkin])}")


    def calculate_cost(self):
        # Calculate the cost of the current pumpkin
        total_cost = sum(item.cost for item in self.inprogress_pumpkin)
        return total_cost
# UCID:nm779 DATE:11/21/2023
# This code sums up the values in the "inprogress_pumpkin" variable and stores the result in the "total_cost" variable.
# The entire function gives you the overall cost.
    def run(self):
        try:
            if self.currently_selecting == STAGE.Pumpkin:
                pumpkin = input(
                    f"What type of pumpkin would you like {', '.join([c.name.lower() for c in self.pumpkins if c.in_stock()])}?\n")
                self.handle_pumpkin_choice(pumpkin)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.FaceStencil:
                stencil = input(
                    f"What type of face stencil would you like {', '.join([f.name.lower() for f in self.face_stencils if f.in_stock()])}? Or type next.\n")
                self.handle_face_stencil_choice(stencil)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Extra:
                extra = input(
                    f"What extras would you like {', '.join([t.name.lower() for t in self.extras if t.in_stock()])}? Or type done.\n")
                self.handle_extra_choice(extra)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                total = input(f"Your total is {expected}, please enter the exact value.\n")
                self.handle_pay(expected, total)

                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    print("Quitting the pumpkin machine")
                    return 1
        except KeyboardInterrupt:
            print("Quitting the pumpkin machine")
            sys.exit()
# UCID:nm779 DATE:11/21/2023
# handle OutOfStockException: 
            # show an appropriate message of what stage/category was out of stock
        except OutOfStockException as e:
            print(f"{self.currently_selecting} is out of stock.")
         # The prints a message informing the user that the item is out of stock.
        #UCID:nm779 DATE:11/21/2023
        # handle NeedsCleaningException
            # prompt user to type "clean" to trigger clean_machine()
            # any other input is ignored
            # print a message whether or not the machine was cleaned
        except NeedsCleaningException as e:
            while True:
                user_input = input("Type clean to clear the machine before using")
                if user_input.lower() == "clean":
                    self.clean_machine()
                    print("Machine has been cleaned.")
                    break
                else:
                    continue
                 # This displays the user to type "clean" to clean the machine before use, and then cleans the machine.

        #UCID:nm779 DATE:11/21/2023
        # handle InvalidChoiceException
        # show an appropriate message of what stage/category was the invalid choice was in
        except InvalidChoiceException as e:
            print(f"{self.currently_selecting} has an invalid choice.")
         # This prints a message to the user indicating that the selected item is invalid.

        #UCID:nm779 DATE:11/21/2023
        # handle ExceededRemainingChoicesException
            # show an appropriate message of which stage/category was exceeded.
            # move to the next stage/category
        except ExceededRemainingChoicesException as e:
            print(f"{self.currently_selecting} has exceeded remaining choices.")
         # This prints a message to the user indicating that the choices have been exceeded and can tgo beyond this number.

        #UCID:nm779 DATE:11/21/2023
        #  handle InvalidPaymentException
            # show an appropriate message
        except InvalidPaymentException as e:
            print("Invalid payment.")
            # The user receives a message stating that the payment method is not valid.

        # This except indicates a closure for try in run function
        except Exception as e:
            print(f"Something went wrong and I didn't handle it: {e}")

        self.run()

    def start(self):
        self.run()

if _name_ == "_main_":
    pm = PumpkinMachine()
    pm.start()
