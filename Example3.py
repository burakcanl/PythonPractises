# Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran program
# Program that finds the largest number among three numbers entered by the user and prints the result

# Kullanıcıdan üç sayı girmesini istiyoruz.
# We ask the user to input three numbers
number1 = int(input("İlk sayıyı girin (Enter the first number): "))
number2 = int(input("İkinci sayıyı girin (Enter the second number): "))
number3 = int(input("Üçüncü sayıyı girin (Enter the third number): "))

# En büyük sayıyı buluyoruz.
# We find the largest number
if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

# Sonucu ekrana yazdırıyoruz.
# Print the result
print("En büyük sayı (The largest number):", largest)

'''
Program çalıştırıldığında(When the program is run);


PS C:\\Users\\CAN\\Desktop\\PythonPractises> python Example3.py
İlk sayıyı girin (Enter the first number): 25
İkinci sayıyı girin (Enter the second number): 50
Üçüncü sayıyı girin (Enter the third number): 900
En büyük sayı (The largest number): 900

'''