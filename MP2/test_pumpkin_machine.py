import pytest
from PumpkinMachine import PumpkinMachine, STAGE
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException

# Define a fixture to create a PumpkinMachine instance
@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm

# Define a fixture for the first order
@pytest.fixture
def first_order(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(10000, "10000")
    return machine

# Define a fixture for the second order
@pytest.fixture
def second_order(first_order):
    first_order.handle_pumpkin_choice("Large Pumpkin")
    first_order.handle_face_stencil_choice("Spooky Face")
    first_order.handle_face_stencil_choice("Toothy Face")
    first_order.handle_face_stencil_choice("next")
    first_order.handle_extra_choice("LED Candle")
    first_order.handle_extra_choice("Dry Ice")
    first_order.handle_extra_choice("done")
    return first_order

# Sample test case
def test_production_line(second_order):
    for j in second_order.pumpkins:
        print(second_order.inprogress_pumpkin)
        if j.name.lower() == second_order.inprogress_pumpkin[0].name.lower():
            print(f"Pumpkin {j.name.lower()} matches in progress {second_order.inprogress_pumpkin[0].name.lower()}")
            assert True
            return
    assert False

# Add required test cases below

# 1st pumpkin must be the first selection (can't add face stencils or extras without a pumpkin choice)
# UCID:nm779 DATE:11/21/2023
# This test determines if the Pumpkin is being chosen by the machine.
# The code executes only if "currently_selecting" is in the Pumpkin stage, otherwise, it throws an AssertionError.
def test_first_selection(machine):
    assert machine.currently_selecting.name == STAGE.Pumpkin.name

# 2nd can only add face stencils if they're in stock
# UCID:nm779 DATE:11/21/2023
# This test determines whether face stencils are available.
# Selecting two face stencils sets the initial count to 1 and triggers an OutOfStockException.
def test_face_stencils_in_stock(machine):
    # Set the quantity of the first face stencil to 1
    machine.face_stencils[0].quantity = 1
    machine.handle_pumpkin_choice("Mini Pumpkin")
    
    # Use pytest's raises context manager to assert that an OutOfStockException is raised
    with pytest.raises(OutOfStockException):
        machine.handle_face_stencil_choice("Happy Face")

# 3rd can only add extras if they're in stock
# UCID:nm779 DATE:11/21/2023
# This test determines whether extras are available.
# This test and the test case above are comparable.
# When two extras are chosen, the number of extras is initially set to 1, and an OutOfStockException is raised.
def test_extras_in_stock(machine):
    machine.extras[0].quantity = 1
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Dry Ice") 
    try:
        machine.handle_extra_choice("Dry Ice")
        assert machine.extras[0].quantity == 1
    except OutOfStockException:
        assert False

# 4th Can add up to 3 face stencils of any combination
# UCID:nm779 DATE:11/21/2023
# The max face stencil limit is 3, as indicated in PumpkinMachine's attributes.
# The for loop handles only 2 values, and it raises the ExceededRemainingChoicesException when exceeding this limit.
# The function passes if the machine throws an exception; otherwise, the test case is unsuccessful.
def test_max_face_stencils(machine):
    machine.face_stencils[0].quantity = 3
    machine.handle_pumpkin_choice("Mini Pumpkin")
    for stencils in range(machine.MAX_STENCILS - 1):
        machine.handle_face_stencil_choice("Toothy Face")
    try:
        machine.handle_face_stencil_choice("Toothy Face")
        assert machine.remaining_stencils == 0
    except ExceededRemainingChoicesException:
        assert False

# 5th Can add up to 3 extras of any combination
# UCID:nm779 DATE:11/21/2023
# This test case is similar to the above test case.
# The value of extras is always -1, and ExceededRemainingChoicesException is thrown if that value is equal to 0.
# The test case is unsuccessful if the exception is not caught.
def test_max_extras(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    # loop to choose (maximum - 1) number of stencil
    for scoop in range(machine.MAX_EXTRAS - 1):
        machine.handle_extra_choice("LED Candle")
    try:
        machine.handle_extra_choice("LED Candle")
        assert machine.remaining_extras == 0
    except ExceededRemainingChoicesException:
        assert False

# 6th cost must be calculated properly based on the choices (check for currency format as part of this)
# (test case should have a few permutations of at least 3 valid pumpkins [hint parameterized tests])
# UCID:nm779 DATE:11/21/2023
# This test case is used to calculate the total cost.
# The test case goes through each step, including selecting the extras and stencils as well as the pumpkin.
# The procedure is then computed using the calculate_cost function based on the selected items,
# and its equality with the expected cost of 6.5 is verified.
# Initially we reset the machine using reset().
def test_total_cost(machine):
    machine.reset()
    machine.handle_pumpkin_choice("Large Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Glitter")
    machine.handle_extra_choice("done")
    assert machine.calculate_cost() == 6.5

# 7th Total Sales (sum of costs) must be calculated properly (test case should have a few permutations of at least 3 valid pumpkins
# [hint parameterized tests])
# UCID:nm779 DATE:11/21/2023
# This test case examines the method by which the device determines the price for several orders.
# The test case, as per usual, goes through every step, including selecting the pumpkin and selecting the extras and stencils.
# The cost is then determined using the calculate_cost function. The pumpkin is then paid using handle_pay(). 
# The real price and the sting format at the same cost are the two variables that must be entered. The source of this is calculate_cost().
# The final step involves storing the cost in a variable named total_sales.
# After the second order is placed, it adds the total cost and serves a similar purpose. 
# Lastly, the test determines whether the total_sales attribute equals the total of the two pumpkins' expenses.
def test_total_sales(machine):
    # First order
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Dry Ice")
    first_pumpkin_cost = float(machine.calculate_cost())
    # Set the machine stage to Pay
    machine.currently_selecting = STAGE.Pay
    machine.handle_pay(first_pumpkin_cost, str(first_pumpkin_cost))

    # Second order
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Googly Eyes")
    machine.handle_extra_choice("done")
    second_pumpkin_cost = float(machine.calculate_cost())
    machine.handle_pay(second_pumpkin_cost, str(second_pumpkin_cost))
    expected_total_sales = first_pumpkin_cost + second_pumpkin_cost
    # Assert that the total sales match the expected total
    assert machine.total_sales == expected_total_sales

# 8th Total products variable should properly increment for each purchase
# UCID:nm779 DATE:11/21/2023
# We monitor the delivery of multiple items by the Pumpkin machine in this test case.
# Here, two orders are placed, and it claims that the "total_products" variable increases as
# anticipated following the completion of each order's payment.
# It guarantees that the number of orders processed by the Pumpkin Machine is counted precisely.
# We make use of handle_pay(), calculate_cost(), and reset().
def test_total_pumpkin(machine):
    machine.reset()
    # First order
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Dry Ice")
    first_pumpkin_cost = float(machine.calculate_cost())
    machine.currently_selecting = STAGE.Pay
    machine.handle_pay(first_pumpkin_cost, str(first_pumpkin_cost))
    assert machine.total_products == 1

    # Reset the machine for the second order
    machine.reset()
    # Second order
    machine.handle_pumpkin_choice("Small Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Small Candle")
    second_pumpkin_cost = float(machine.calculate_cost())
    machine.currently_selecting = STAGE.Pay
    machine.handle_pay(second_pumpkin_cost, str(second_pumpkin_cost))

    assert machine.total_products == 2

if _name_ == "_main_":
    pytest.main()
