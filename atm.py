class atm(object):
    def __init__(self,cardnumber,pin,cvv,expirydetailsofcard):
        self.cardnumber=cardnumber
        self.pin=pin
        self.cvv=cvv
        self.expirydetailsofcard=expirydetailsofcard

    def toPay(self):
        print("Your Payment Is Done By A Secured Method ")

    def toGet(self):
        print("You won a reward of 5000")

    def expiry():
        print("Your Card Is expired")
        