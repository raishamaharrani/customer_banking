"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    account = Account(balance, 0)
    #print ("Account Balance:", account.get_balance())
    #print ("Interest Rate:", account.get_interest_rate())

    # Calculate interest earned
    cd_interest_earned = balance * (interest_rate/100* months/12)
    
    # Update the CD account balance by adding the interest earned
    updated_cd_balance = balance + cd_interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    account.set_balance(updated_cd_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    account.set_interest(cd_interest_earned)

    # Return the updated balance and interest earned.
    return  cd_interest_earned,updated_cd_balance