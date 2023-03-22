from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import stripe

import stripe
stripe.api_key = "sk_test_51MllwGBUJKiCM3GCX0umGaryJz29LzLGJd0GJgOI1bNmSm1XnqDpfI5yGGi9TXu8D63a1i7uU2mNGzEsXSwqVKUr00Bdyepwqp"


app = FastAPI()

class Customer(BaseModel):
    name: str
    email: str
    address: str

class Charge(BaseModel):
    customer_id: str
    product_id: str
    price: int

class PaymentMethod(BaseModel):
    type: str
    number: str
    exp_month: int
    exp_year: int
    cvc: str

@app.post("/charges")
def charge_product(charge: Charge):
    stripe.Charge.create(
        customer=charge.customer_id,
        amount=charge.price,
        currency="usd",
        description="Charge for product {}".format(charge.product_id)
    )
    return {"message": "Charge processed successfully"}

# Creatae customer
@app.post("/customers")
def create_customer(customer: Customer):
    stripe_customer = stripe.Customer.create(
        name=customer.name,
        email=customer.email,
        address={
            "line1": customer.address
        }
    )
    return stripe_customer  

# Create payment method
@app.post("/crate-payment-method")
def create_customer(payment: PaymentMethod):
    stripe_customer = stripe.PaymentMethod.create(
        type=payment.type,
        card={
            "number":payment.number,
            "exp_month":payment.exp_month,
            "exp_year":payment.exp_year,
            "cvc":payment.cvc
        }
    )
    return stripe_customer  


# Create Payment Method for Customer
@app.post("/payment_methods_request")
async def create_payment_method(payment_method_request: PaymentMethod):
    try:
        # Create Payment Method
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": payment_method_request.number,
                "exp_month": payment_method_request.exp_month,
                "exp_year": payment_method_request.exp_year,
                "cvc": payment_method_request.cvc
            }
        )
        # Attach Payment Method to Customer
        payment_method.attach(customer='cus_NZaGvh6IKeGmtU')
        return {"message": "Payment method created successfully", "data": payment_method}
    except stripe.error.CardError as e:
        # Error Handling for Card Errors
        error = e.json_body.get("error", {})
        raise HTTPException(status_code=400, detail=error.get("message", "Unknown Error"))
    except stripe.error.StripeError as e:
        # Error Handling for Generic Stripe Errors
        raise HTTPException(status_code=400, detail=str(e))
    