import stripe
stripe.api_key = "sk_test_51MllwGBUJKiCM3GCX0umGaryJz29LzLGJd0GJgOI1bNmSm1XnqDpfI5yGGi9TXu8D63a1i7uU2mNGzEsXSwqVKUr00Bdyepwqp"

# get customers
# customer_list = stripe.Customer.list()

# get prices
# price_list = stripe.Price.list(limit=3)

# create customer
# stripe.Customer.create(
#   name="hammad ali shah",
#   email="skilletjordan@gmail.com",
#   payment_method="pm_card_visa",
#   invoice_settings={"default_payment_method": "pm_card_visa"},
# )

#create source
# stripe.Subscription.create(
#   customer="cus_NZTIKzGcimagOi",
#   items=[{"price": "price_1MoKFiBUJKiCM3GC2M9ElcvG"}],
#   billing_cycle_anchor=1679477295,
# )

#list all payment methods of customer
# list_payment_methods = stripe.Customer.list_payment_methods(
#   "cus_NZTIKzGcimagOi",
#   type="card",
# )

#retrieve payment mathod:
retrieve = stripe.PaymentMethod.retrieve(
  "pm_1MoODEBUJKiCM3GCPBNZFzbL",
)

print(retrieve)

