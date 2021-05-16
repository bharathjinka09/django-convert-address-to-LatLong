from django.db import models
from django.contrib.auth.models import User
# from users.models import Profile
from django_countries.fields import CountryField
import requests
api_response_dict = ''

class Address(models.Model):
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    country = CountryField(blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')

    def __str__(self):
        return f'Address {self.address_1}'

    class Meta:
        verbose_name_plural = "addresses"

    def save(self, **kwargs):

        address = " ".join(
            [self.address_1, self.address_2, str(self.zip_code), self.city])
        # api_key = "REPLACE_YOUR_PROJECT_API_KEY_HERE"
        # api_response = requests.get(
        #     'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response = requests.get("http://api.positionstack.com/v1/forward?access_key=1df0f214727eddb3e6c9dac2bbe9524f&query={0}".format(address))

        api_response_dict = api_response.json()
        # print(api_response_dict, "aIPscd")
        print(api_response_dict['data'],"7777777777777777")
        # print(api_response_dict['data'][0]['longitude'])
        
        if api_response_dict:
            # self.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            # self.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            try:
                self.latitude = api_response_dict['data'][0]['latitude']
                self.longitude = api_response_dict['data'][0]['longitude']
                self.save()
            except Exception as e:
                print(e,"ERRor")
        super().save(**kwargs)