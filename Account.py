class Account:
	def __init__(self,firstname,secondname,balance):
		self.firstname=firstname
		self.secondname=secondname
		self.balance=balance
		

	def user(self):
		return "Hello {} {} your balance is {}".format(self.firstname,self.secondname,self.balance)
	
	def deposite(self,cash_deposited):
		self.balance=self.balance + cash_deposited
		return "Hello {} {} you have deposited {}".format(self.firstname,self.secondname,cash_deposited)

	def withdraw(self,cash_withdrawn):
		if cash_withdrawn <= self.balance:
			self.balance=self.balance-cash_withdrawn
			return "Hello {} {} you have succesfully withdrawn {}".format(self.firstname,self.secondname,cash_withdrawn)

		else:
			return "Hello {} {} , your Account balance is insufficient to withdrawn {}".format(self.firstname, self.secondname,cash_withdrawn)
				

	def show_balance(self):
		show_balance = self.balance
		return "Hello {} {}, your current balance is {}".format(self.firstname,self.secondname,self.balance)
