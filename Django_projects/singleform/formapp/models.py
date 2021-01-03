from django.db import models

LOCATION=(('indore', 'Indore'), ('ujjain', 'Ujjain'), ('pune', 'Pune'), ('mumbai' , 'Mumbai'), ('banglore', 'Banglore'), ('other', 'Other'),)

SERVICE=(('wedding', 'Wedding'), ('birthday', 'BirthDay'), ('stage_decoration', 'Stage_Decoration'),)

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.fname

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(choices=SERVICE, default='birthday', max_length=50)
    Max_Guest = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False,)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField(blank=True)
    # profile=models.ImageField(upload_to = 'images', max_length=255,height_field=None, width_field=None , default="")
    

    def __str__(self):
        return self.service


class Address(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    city = models.CharField(choices=LOCATION, default='indore', max_length=50)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()
    

def image_path(instance, filename):
    instance_id = instance.event.id
    return 'images/{}/{}'.format(instance_id, filename)

class event_photo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_photos')
    photo = models.ImageField(upload_to=image_path, max_length=255)
    create_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)