# Data Classes Exercise

from dataclasses import dataclass, field
from datetime import date

@dataclass
class Orders:
    orderId: int
    customerId: int
    salespersonId: int
    orderDate: date
    expectedDelivery: date
    purchaseOrderNum: str

    def __gt__(self,other):
        return self.expectedDelivery > other.expectedDelivery

    def __ge__(self,other):
        return self.expectedDelivery >= other.expectedDelivery

@dataclass
class Invoices:
    invoiceId: int
    customerId: int
    orderId: int
    invoiceDate: date
    totalDryItems: int
    totalChillerItems: int

    def __gt__(self,other):
        return (self.totalChillerItems + self.totalDryItems) > (other.totalChillerItems + other.totalDryItems)

    def __ge__(self,other):
        return (self.totalChillerItems + self.totalDryItems) >= (other.totalChillerItems + other.totalDryItems)

@dataclass
class Customers:
    customerId: int
    customerName: str
    deliveryCityId: int
    creditLimit: float
    standardDiscountPct: float
    addressLine1: str
    addressLine2: str
    postalCode: str
