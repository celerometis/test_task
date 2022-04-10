from django.db import models
from django.core.validators import RegexValidator


# Create your models here.


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(validators=[phone_regex], max_length=17,
                             null=True, unique=True)
    email = models.EmailField(unique=True)
    # owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
