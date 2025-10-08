from faker import Faker
from faker.providers import internet
luis = Faker()


print("-----Primer Dato-----")
luis = Faker(['it_IT', 'en_US', 'ja_JP'])
for _ in range(5):
    print(luis.name())



print("-----Segundo Dato-----")
for _ in range(3):
    print (luis.address())

print ("-----Tercer Dato-----")
luis = Faker()
luis.add_provider(internet) 
for _ in range(4):   
    print(luis.ipv4_private())


print ("-----Cuarto Dato-----")
Faker.seed(0)
for _ in range(5):
   print(luis.emoji())

'🇸🇪'
'🧖🏽\u200d♂️'
'⏩'
'🏋🏼\u200d♀️'
'🤚🏽'

print ("-----Quinto Dato-----")
Faker.seed(0)
for _ in range(2):
    print(luis.country_calling_code())



print ("-----Sexto Dato-----")
Faker.seed(0)
for _ in range(3):
   print(luis.phone_number())



print ("-----Septimo Dato-----")
import faker
luis = faker.Faker()

numbers = set(luis.unique.random_int() for i in range(10))
assert len(numbers) == 10

print(numbers)

print ("-----Octavo Dato-----")
Faker.seed(0)
for _ in range(1):
    luis.android_platform_token()
print(luis.android_platform_token())


print ("-----Noveno Dato-----")
Faker.seed(0)
for _ in range(2):
    luis.passport_dob()
    print(luis.passport_dob())

print ("-----Decimo Dato-----")   
Faker.seed(0)
for _ in range(5):
    luis.passport_owner()
    print(luis.passport_owner())