from django.db import models

# Create your models here.
class Expense(models.Model):
    date = models.Field.unique_for_date
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.CharField(max_length = 10)
    category = models.Field.choices
        