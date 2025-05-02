from django.db import models

# Create your models here.


category = (('printtshirtm','Printtshirtm'),("shirtm","Shirtm"),("jeansm","Jeansm"),("cargom","Cargom"),
           ('baggym','Baggam'),('shortsm',"Shortsm"),('printtshirtw','Printtshirtw'),("shirtw","Shirtw"),("kurta","Kurtaw"),("cargow","Cargow"),
           ('cargow','Cargow'),('shortsw',"Shortsw"),("braclets","Braclets"),("necklace","Necklace"),("caps","Caps"),("rings","Rings"),("sunglasses","Sunglasses"),("bags","Bags"),("watchm","Watchm"),("watchw","Watchw"),('shoes','Shoes'))


class clothes(models.Model):
    clothname = models.CharField(max_length=100)
    clothprice = models.IntegerField()
    clothescat = models.CharField(choices=category,max_length=200)
    clothesdesc = models.TextField()
    clothimg = models.ImageField()

