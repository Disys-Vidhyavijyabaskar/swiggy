class swiggy:

    def __init__(self,h,sd,m,s,a,tp,c,t,p):

        self.hotelslist=h
        self.sidedish=sd
        self.maincourse=m
        self.starters=s
        self.address=a
        self.toppicks=tp
        self.cusines=c
        self.tiffenitems=t
        self.personaldetails=p

    def display(self):

        self.location="current location"
        print("location address")

        self.hotels="list of hotels "
        print("hotels you may like")

        self.personaldata="enter name","enter address","add favourites","add phone no","add debit/credit card details"
        print("add personal data")

        self.cart="add food in the list"
        print("your cart")

        self.edit="edit cart details"
        print("edit cart")

        self.order="press ok in cart"
        print("place your order")

        self.selectcusines=" select the cusines you like"
        print("select cusine")

        self.recent= "recent hotels you ordered" or "favourites"
        print("recent hotels")
        

    def promotions(self):

        self.coupons="enter coupon details"
        print("enter coupon")

        self.discounts= "avail any discounts"
        print("avail discount")

        self.offers="avail offers" or "free dish"
        print("avail offer/freedish")


    def payment(self):

        self.debitcard="enter debit card details"
        print("save debit card")

        self.creditcard="enter credit card details"
        print("save credit card")

        self.netbanking=" pay through net banking"
        print("add banks for net banking")

        self.mobiletransfers="add mobile banking details"
        print("add mobilebanking")

        self.cash="pay cash on delivery"
        print("cash on delivery")

        self.gpay= "pay through gpay" or "phonepe"
        print("g pay or phonepe")


    def instamart(self):

        self.groceries="add grocery list "
        print("add groceries")

        self.payement="make payment"
        print("make payment")

    def genie(self):

        self.pickup="enter the pickup location" and "giver name"
        print("pickup")

        self.drop="enter the drop location" and "receiver name"
        print("drop")

        self.item="mention the type of item"
        print("type of item")

        self.deliverytime="mention the time of delivery"
        print("EST of delivery")

        self.deliverycharge="payment for delivery"
        print("delivery charges")

        self.payement="make payment"
        print("make payment")

        
    def review(self):

        self.reviewondel="review on delivery partner"
        print("review for delivery partner")

        self.reviewforhotel=" review on hotel/food"
        print("review on food")

        self.deliverypartner="details of delivery partner" and "temperature"
        print("delivery partner details and temperature")

        
        
              
customer=swiggy("hotels","sidedish","maincourse","starter","address","toppicks","cuisines","tiffen","personaldata")
customer.display()
customer.promotions()
customer.payment()
customer.instamart()
customer.genie()
customer.review()

if ("otp!=bankotp"):
    raise ValueError ("error and try again later")
elif print("order placed, keep swiggying!"):

    if ("any help required"):
        print("options and help")
    
