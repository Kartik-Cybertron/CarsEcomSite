from django.db import models

# Create your models here.

class CarBrand(models.Model):
    brand_id=models.AutoField(primary_key=True)
    logo=models.ImageField(upload_to='images/logo')
    brand_name=models.CharField(max_length=100)
    model_year=models.CharField(max_length=10)

    def __str__(self):
        return self.brand_id

class CarModel(models.Model):
    model_id=models.AutoField(primary_key=True)
    brand_id=models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    model_name=models.CharField(max_length=100)

    def __str__(self):
        return self.model_id

class Login(models.Model):
    f_name=models.CharField(max_length=200)
    l_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    passwd=models.CharField(max_length=200)

    def __str__(self):
        return self.f_name
        
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    brand_id=models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    model_id=models.ForeignKey(CarModel,on_delete=models.CASCADE)
    model_year=models.CharField(max_length=100)
    Specifications=models.CharField(max_length=1000)
    Car_Type=models.CharField(max_length=100)

    def __str__(self):
        return self.car_id

class CarImages(models.Model):
    car_id=models.ForeignKey(Car,on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='cars/')
    image2 = models.ImageField(upload_to='cars/')
    image3 = models.ImageField(upload_to='cars/')
    image4 = models.ImageField(upload_to='cars/')
    image5 = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.car_id





# class Log(models.Model):
#     f_name=models.CharField(max_length=200)
#     l_name=models.CharField(max_length=200)
#     email=models.CharField(max_length=200)
#     images = models.FileField(blank=True)

#     def __str__(self):
#         return self.f_name

# class PostImage(models.Model):
#     log=models.ForeignKey(Log,default=None,on_delete=models.CASCADE)
#     images=models.FileField(upload_to='images/')

#     def __str__(self):
#         return self.log.f_name