class Account:
	def __init__(self, acctNum, acctPin, balance):
		self.acctNum = acctNum
		self.pin = acctPin
		self.balance = int(balance)
	#def checkPin(self, pin):
	#	if self.pin == pin:
	#		return True
	#	else:
	#		return False
	def deposit(self, amount):
		self.balance += amount
		return self.balance
	def withdraw(self, amount):
		if amount > self.balance:
			return self.balance
		else:
			self.balance -= amount
			return self.balance
		
accounts = ['1000|1234|10000', '1020|2222|0', '3000|3344|1000', '2020|1234|90000']
print(accounts)

transactions = ['add|1000|1000|1234', 'sub|1000|1020|2222', 'sub|1000|3000|3344']
#print(transactions)
greeting = "Hello"

def mainTransaction(transactions, accounts):
	for transaction in transactions:
		transactionList = transaction.split("|")
		tCommand = transactionList[0]
		tAmount = int(transactionList[1])
		tAccount = transactionList[2]
		tPin = transactionList[3]
		for account in accounts:
			index = accounts.index(account)
			customer = account.split("|")
			custObj = Account(customer[0],customer[1],customer[2])
			if custObj.acctNum == tAccount and custObj.pin == tPin:
				#print("commence transaction")
				makeTransaction(custObj, tCommand, tAmount)
				#print(custObj.balance)
				customer[2] = str(custObj.balance)
				#print(customer[2])
				account = "|".join(customer)
				#print(account)
				accounts[index] = account
			else:
				print("wrong account/pin")
	return accounts
				
def makeTransaction(cust, command, amount):
	if command == 'add':
		cust.deposit(amount)
	elif command == 'sub':
		cust.withdraw(amount)

newAccounts = mainTransaction(transactions,accounts[:])
print("new Accounts: ")
print(newAccounts)
print("old Accounts: ")
print(accounts)

#cust1 = Account(1000,1234,10000)		
#print(cust1.acctNum)
#print(cust1.checkPin(1235))
#cust1.deposit(100)		
#cust1.withdraw (120)

#print(cust1.balance)

#z = spins[:]     # Traditional way
#z = spins(spins) # Pragmatic way
#z = spins.copy() # My favorite way
#https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/
#https://www.python-course.eu/passing_arguments.php
