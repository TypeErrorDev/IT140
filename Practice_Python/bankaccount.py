# Create a BankAccount class where each account has:
# - An account holder's name and balance
# - A method to deposit money
# - A method to withdraw money
# - A method to check balance
# The balance should never go below 0!

# Example usage:
my_account = BankAccount("Alex", 100)
my_account.deposit(50)      # Should add 50 to balance
my_account.withdraw(30)     # Should subtract 30 from balance
my_account.check_balance()  # Should print current balance
my_account.withdraw(200)    # Should print "Not enough funds!"