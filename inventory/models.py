from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class InventoryItem(models.Model):
    """Inventory Items - Will contain data about inventory item and create a log
    upon any change (for keeping track of changes)"""
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=False, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    #Run everytime the InventoryItem is Saved to create a log of previous items
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        InventoryItemLog.objects.create(
            change_date=self.date_created,
            item=self,
            quantity=self.quantity,
            user=self.user
        )

    
class Category(models.Model):
    """Category for Inventory Items"""
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class InventoryItemLog(models.Model):
    """Used to keep track of changes in InventoryItems. It's information
    including change_date are generated by the InventoryItem save"""
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    change_date = models.DateTimeField(auto_now_add=False, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} - {self.quantity} - {self.change_date}"