from datetime import datetime
class Account:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.balance = 0        

    def welcome(self):
        return "Hello {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)


    def deposit(self,d):
        deposit = d
        time = datetime.now()
        object = {"time":time,"d":d}
        self.deposits.append(object)



        
        # self.deposits.append(y)
        
        self.balance = self.balance + d

        dps = "Dear {} {} deposit of kes {} was successful current balance is {}".format(self.first_name,self.last_name,d,self.balance)
        return dps


    def show_deposits(self):

        for d in self.deposits:
            time = d["time"]
            formatted_time = time.strftime("%c")
            d= d["d"]
            print("On {} you deposited {}".format(formatted_time,amount))
        

    def withdraw(self,w):
        withdraw = w
        time = datetime.now()
        object = {"time":time,"amount":w}
        self.withdrawals.append(object)

         


        if w>self.balance:
            return "cant withdraw"
        else:
            self.balance = self.balance - w



            


            msg = "Dear {} {} withdrawal of kes {} was successful current balance is {}".format(self.first_name,self.last_name,w,self.balance)
            return msg


    def show_withdrawals(self):
        for w in self.withdrawals:

            time = w["time"]
            formatted_time = time.strftime("%c")
            amount= w["amount"]
            print("On {} you withdrew {}".format(formatted_time,amount))
            
    

    def show_balance(self):
        show_balance = self.balance
        text = "Dear {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
        return text

    def give_loan(self,l):
         loan = l
         total = 0
         for d in self.deposits:
            d = d["d"]
            total+=d

         if len(self.deposits)>=5 and l<total/3 and self.loan==0:
            self.loan = self.loan + l
            print("Dear customer your loan of {} has been approved".format(l))



    def repay_loan(self,p):
        
        payment = p

        self.loan.extend(p)

        self.loan = self.loan-p
        excess_payment = self.deposit.append(deposit)

        loanp = "Dear customer you have paid kes {} your remaining loan balance is now {}".format(p,self.loan)
        print(loanp)













































































































































# class Account:
# 	def __init__(self,firstname,secondname,balance):
# 		self.firstname=firstname
# 		self.secondname=secondname
# 		self.balance=0
# 		self.deposits=[]
# 		self.withdraws=[]
# 		self.loan=0
# 		# self.loans=[]


		

# 	def user(self):
# 		return "Hello {} {} your balance is {}".format(self.firstname,self.secondname,self.balance)
	
# 	def deposit(self,amount):
# 		time = datetime.now()
# 		object={"time":time,"amount":amount}
# 		self.deposits.append(object)
# 		self.balance = self.balance + amount
# 		return "Hello {} {} your deposits are {}".format(self.firstname,self.secondname,self.deposits)

# 	def show_deposits(self):
# 		for deposit in self.deposits:
# 			time=deposit["time"]
# 			formated_time=time.strftime("%c")
# 			amount= deposit["amount"]

# 			print ("on {} you deposited {}".format(formated_time , amount))
			

# 	def withdraw(self,amount):
# 		# time = datetime.now()
# 		# object={"time":time,"amount":amount}
# 		if amount <= self.balance:
# 			time = datetime.now()
# 			object={"time":time,"amount":amount}
# 			return "Hello {} {} , your Account balance is insufficient to withdrawn {}".format(self.firstname, self.secondname,self.withdraws)

# 	def show_withdraws(self):
# 		for withdraws in self.withdraws:
# 			time= withdraws ["time"]
# 			formated_time=time.strftime("%c")
# 			amount= withdraw["amount"]

# 			print ("on {}  you withdrew {}".format(formated_time,amount) )

	

# 			self.withdraws.append(object)
# 			self.balance=self.balance-amount
# 			return "Hello {} {} you have succesfully withdrawn {}".format(self.firstname,self.secondname,self.withdraws)

# 		else:

# 	# def show_deposits(self):
# 	# 	for amount in self.deposits:
# 	# 		print(amount)

# 	# def show_withdraws(self):
# 	# 	for amount in self.withdraws:
# 	# 		print (amount)
		
# 	def give_loan(self,amount):
# 		formated_time=time.strftime("%c")
# 		if len(self.deposits) >=5 and amount <= (1/3*sum(self.deposits)) and self.loan==0:

# 		return ("sorry,you have succecfully borrowed, loan")















































	# def pay_loan(self,amount):
	# 	if self.loan==0:
	# 		print("you do not have a loan debt")
	# 	elif amount<self.loan:
	# 		self.loan=self.loan-amount
	# 		print("Hi {} you have paid {} as part of your loan repayment. Your remaining balance is {}".format(self.name, amount, self.loan))
	# 	elif amount==self.loan:
	# 		self.loan=self.loan-amount
	# 		print("You have completed the payment of your loan")
	# 	elif amount>self.loan
	# 		more=amount-self.loan
	# 		self.balance=more+self.balance
	# 		self.loan=amount-self.loan-more
	# 		print("Hello {} you have paid more than what is needed, your new balance is {}".format(self.name,self.balance))

			





	

