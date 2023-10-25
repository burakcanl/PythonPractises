#Kullanıcıdan dairenin yarıçap değerini alarak dairenin alanını ve çevresini hesaplayan program
#Program that calculates the area and circumference of a circle by taking the radius value of the circle from the user

# Kullanıcıdan yarıçap bilgisini alıyoruz.
# We get the radius of the circle from the user
radius = float(input("Dairenin yarıçapını girin (Enter the radius of the circle): "))

# Pi sayısını tanımlıyoruz
# We define the value of pi
pi = 3.14

# Dairenin alanını hesaplıyoruz
# We calculate the area of the circle
area = pi * radius ** 2

# Dairenin çevresini hesaplıyoruz
# We calculate the circumference of the circle
circumference = 2 * pi * radius

# Sonuçları yazdırıyoruz.
# Print the results
print(f"Dairenin alanı (Area of the circle): {area}")
print(f"Dairenin çevresi (Circumference of the circle): {circumference}")

'''
Program çalıştırıldığında(When the program is run);

PS C:\\Users\\CAN\\Desktop\\PythonPractises> python Example4.py
Dairenin yarıçapını girin (Enter the radius of the circle): 5
Dairenin alanı (Area of the circle): 78.5
Dairenin çevresi (Circumference of the circle): 31.400000000000002
'''