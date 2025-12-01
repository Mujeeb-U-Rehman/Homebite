from django.db import models
from django.utils import timezone
from accounts.models import CustomerProfile, CookProfile
from meals.models import Meal


class Order(models.Model):
    """Model representing a customer order."""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('ready', 'Ready for Pickup'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    DELIVERY_TYPE_CHOICES = [
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash on Delivery/Pickup'),
    ]
    
    customer = models.ForeignKey(
        CustomerProfile, on_delete=models.CASCADE, related_name='orders'
    )
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='orders'
    )
    cook = models.ForeignKey(
        CookProfile, on_delete=models.CASCADE, related_name='received_orders'
    )
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending'
    )
    delivery_type = models.CharField(
        max_length=20, choices=DELIVERY_TYPE_CHOICES, default='pickup'
    )
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash'
    )
    customer_phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True, help_text='Special instructions or notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order #{self.pk} - {self.meal.name} by {self.customer.user.username}"
    
    @property
    def order_id(self):
        """Generate a formatted order ID."""
        return f"HB{self.pk:06d}"
    
    def calculate_total(self):
        """Calculate total price based on meal price and quantity."""
        self.total_price = self.meal.price * self.quantity
        return self.total_price
    
    def mark_as_ready(self):
        """Mark order as ready for pickup."""
        self.status = 'ready'
        self.save()
    
    def mark_as_completed(self):
        """Mark order as completed."""
        self.status = 'completed'
        self.cook.total_orders += 1
        self.cook.save()
        self.save()
    
    def cancel(self):
        """Cancel the order and restore meal quantity."""
        if self.status in ['pending', 'confirmed']:
            self.status = 'cancelled'
            self.meal.quantity_available += self.quantity
            self.meal.save()
            self.save()
            return True
        return False
