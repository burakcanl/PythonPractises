# Kullanıcıdan boy ve ağırlık bilgilerini alarak Vücut Kitle Endeksini yazdıran program
# A program that takes height and weight information from the user and calculates the Body Mass Index (BMI).

# Kullanıcıdan boy ve ağırlık bilgisini alıyoruz.
# We are getting height and weight information from the user
bodyHeight = float(input("Boyunuzu metre cinsinden girin (Enter your height in meters): "))
bodyWeight = float(input("Kilonuzu kilogram cinsinden girin (Enter your weight in kilograms): "))

# Vücut Kitle İndeksini hesaplıyoruz.
# We are calculating Body Mass Index.
BMI = bodyWeight / (bodyHeight ** 2)

# Sonucu ekrana yazdırıyoruz.
# We are displaying the result.
print("Vücut Kitle İndeksi (Body Mass Index):", BMI)



'''
Program çalıştırıldığında(When the program is run);

PS C:\\Users\\CAN\\Desktop\\PythonPractises> python Example1.py
Boyunuzu metre cinsinden girin (Enter your height in meters): 1.80
Kilonuzu kilogram cinsinden girin (Enter your weight in kilograms): 65
Vücut Kitle İndeksi (Body Mass Index): 20.061728395061728

'''