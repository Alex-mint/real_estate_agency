from  property.models import Flat
import phonenumbers
#from property.prueba2 import get_pure_number
#get_pure_number(1)


def get_pure_number(num):
    flat = Flat.objects.all()[num]
    phone = flat.owners_phonenumber
    parsed_phone = phonenumbers.parse(phone, "RU")
    pure_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
    flat.owner_pure_phone = pure_number
    flat.save()



