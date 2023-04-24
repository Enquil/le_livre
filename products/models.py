from django.db import models


# Sourced from Code Institute https://codeinstitute.net/global/
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Sourced from Code Institute https://codeinstitute.net/global/
class Genre(models.Model):

    class Meta:
        verbose_name_plural = 'Genres'

    parent = models.ForeignKey('Category', on_delete)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Sourced from Code Institute https://codeinstitute.net/global/
class ElectronicCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Electronics'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Sourced from Code Institute https://codeinstitute.net/global/
class Product(models.Model):
    '''
    - Base model for single-payment products with common basic features
    - Abstract used since the Product model should not need a table on its own
    '''
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


# Inherits the 'Product' class
class Book(Product):
    '''
    Inherits Product Class and adds relevant fields for books
    '''
    genre = models.ForeignKey('BookGenre',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL)
    authors = models.CharField(max_length=254)
    isbn_thirteen = models.CharField(max_length=254, null=True, blank=True)
    isbn_ten = models.CharField(max_length=254, null=True, blank=True)


# Inherits the 'Product' class
class Electronics(Product):
    '''
    Inherits Product class and adds relevant fields for electronics
    '''
    electronics_category = models.ForeignKey('ElectronicCategory',
                                             null=True,
                                             blank=True,
                                             on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254)

    class Meta:
        abstract = True


class Laptop(Electronics):
    '''
    Inherits Electronics class and adds relevant fields for electronics
    '''
    parent = models.ForeignKey('Category',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    screen_size = models.DecimalField(null=True,
                                      blank=True)
    processor = models.TextField(null=True,
                                 blank=True)
    graphics = models.CharField(max_length=254)
    manufacturer_sku = models.CharField(max_length=254)
