from django.db import models

# Create your models here.

choices_fields=(
    ("starters","starters"),
    ("main_dishes","main_dishes"),
    ("deserts","deserts"),
    ("drinks","drinks")
)

class Menu(models.Model):
    title=models.CharField(max_length=500,blank=False,null=False)
    description=models.TextField(max_length=1000,blank=False,null=False)

    price=models.DecimalField(max_digits = 8,
                         decimal_places = 2,default=0.0)
    image=models.ImageField(upload_to="menu/",blank=False,null=False) 
    type=models.CharField(choices=choices_fields,max_length=20,default="starters")
    special=models.BooleanField(default=False)
    special_image=models.ImageField(upload_to="menu/",blank=True,null=True) 

    def __str__(self):
        return self.title
    

    

