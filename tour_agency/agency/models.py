from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name='Nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Company(models.Model):
    name = models.CharField(max_length=70,verbose_name='Nomi')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Kompaniya'
        verbose_name_plural = 'Kompaniyalar'



class Ticket(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Kategoriya')
    company = models.ForeignKey(Company,on_delete=models.CASCADE,verbose_name='Kompaniya')
    name = models.CharField(max_length=255,verbose_name='Nomi')
    image = models.ImageField(upload_to='media',null=True,blank=True)
    comfort = models.TextField(verbose_name='qulaylik')
    about = models.TextField(verbose_name='haqida')
    time = models.DateTimeField(verbose_name='Uchish vaqti')
    price = models.IntegerField(verbose_name='Narxi',default=0)


    def __str__(self):
       return self.name

    class Meta:
        verbose_name = 'Bilet'
        verbose_name_plural = 'Biletlar'





