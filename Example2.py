#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren program
#A program that takes input from the user for the salary and raise percentage, converts the raise percentage to its decimal form (dividing by 100), calculates the new salary with the raise, and displays the result on the screen in USD.

# Kullanıcıdan maaş ve zam oranın bilgilerini alıyoruz.
# We get the input for salary and the raise percentage information from the user
salary = float(input("Maaşınızı girin (Enter the salary): "))
raise_percentage = float(input("Zam oranını girin (Enter the raise percentage(%)): "))

# Zam yüzdesi yüzde şeklinde olduğu için 100'e bölüyoruz.
# Since the raise percentage is in percentage form, we divide it by 100.
raise_percentage /= 100

# Zamlanmış yeni maaşı hesaplıyoruz.
# We calculate the new salary with the raise
new_salary = salary * (1 + raise_percentage)

# Sonucu ekrana yazdırıyoruz.
# We display the result on the screen
print(f"Zamlı yeni maaşınız (Your new salary): {new_salary:.2f} TL")


'''
Program çalıştırıldığında(When the program is run);

PS C:\\Users\\CAN\\Desktop\\PythonPractises> python Example2.py
Maaşınızı girin (Enter the salary): 20000
Zam oranını girin (Enter the raise percentage(%)): 50
Zamlı yeni maaşınız (Your new salary): 30000.00 TL
'''