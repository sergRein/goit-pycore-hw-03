import re

def normalize_phone(phone_number):
    #remove all except digits
    patter_to_replace = r"[^\d]" 
    temp_number = re.sub(patter_to_replace, '', phone_number)
    #leave last 9 numbers and add +380 to number (will remove all in start like 380|80|0)
    return "+380"+temp_number[-9:]

    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)