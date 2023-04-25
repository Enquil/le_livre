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
class Product(models.Model):
    '''
    Base model for single-payment products with common basic features.
    Abstract used since the Product model should not need a table on its own.
    '''
    class Meta:
        abstract = True

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


# Sourced from Code Institute https://codeinstitute.net/global/
class BookGenre(models.Model):

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

    parent = models.ForeignKey('Category', on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Inherits the 'Product' class
class Book(Product):
    '''
    Inherits Product Class and adds relevant fields specific to books.
    '''
    genre = models.ForeignKey('BookGenre',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL)
    authors = models.CharField(max_length=254)
    isbn_thirteen = models.CharField(max_length=254,
                                     null=True,
                                     blank=True)
    isbn_ten = models.CharField(max_length=254,
                                null=True,
                                blank=True)


# Inherits the 'Product' class
class Electronics(Product):
    '''
    Inherits Product class and adds relevant fields specific to electronics.
    '''
    class Meta:
        abstract = True

    electronics_category = models.ForeignKey('ElectronicCategory',
                                             null=True,
                                             blank=True,
                                             on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254)
    manufacturer_sku = models.CharField(max_length=254)
    additional_features = models.TextField(max_length=1024)


class Computer(Electronics):

    class Meta:
        abstract = True

    parent_category = models.ForeignKey('Category',
                                        null=True,
                                        blank=True,
                                        on_delete=models.SET_NULL)
    cpu = models.CharField(max_length=254,
                           null=True,
                           blank=True)
    gpu = models.CharField(max_length=254,
                           null=True,
                           blank=True)
    ram = models.CharField(max_length=254,
                           null=True,
                           blank=True)
    hard_drive = models.CharField(max_length=254,
                                  null=True,
                                  blank=True)


class HasScreen():

    class Meta:
        abstract = True

    screen_size = screen_size = models.CharField(null=True,
                                                 blank=True)
    refresh_rate = models.IntegerField(null=True,
                                       blank=True)


class Laptop(Computer, HasScreen):
    '''
    Inherits Computer and HasScreen
    '''
    has_camera = models.BooleanField()


class Tablet(Laptop):
    has_sim = 


class Phone(Computer, HasScreen):
    '''
    Inherits Computer and HasScreen, add camera options
    '''
    back_camera = models.CharfieldField(null=True,
                                        blank=True)
    front_camera = models.CharfieldField(null=True,
                                         blank=True)


class HeadPhones(Electronics):
    '''
    Inherits Electronics class and adds relevant fields specific to audio.
    '''
    IN_EAR = "In Ear"
    OVER_EAR = "Over Ear"
    HEADPHONE_TYPE_CHOICES = [
        (IN_EAR, "In Ear"),
        (OVER_EAR, "Over Ear"),
    ]
    type = models.CharField(max_length=15,
                            choices=HEADPHONE_TYPE_CHOICES,
                            default=IN_EAR)
    wireless = models.BooleanField(default=False)
