from django.db import models
from api_overview.models import Profile
from books.models import BooksModel
import uuid


class CartItems(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item_id = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
    ordered_when = models.DateTimeField(auto_now_add=True, null=False)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2) 
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    delivered = models.BooleanField(default=False)


    def __str__(self):
        return self.delivered



    

