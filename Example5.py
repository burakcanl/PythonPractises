#Kullanıcı tarafından girilen bir sayının palindrom olup olmadığını kontrol eden program
#Program to check whether a number entered by the user is a palindrome

#Kullanıcıdan bir sayı alıyoruz
#We get the input from user.
number = input("Bir sayı girin (Enter a number): ")

#Girilen sayıyı string veri tipine çeviriyoruz ve bunu başka bir değişkene atıyoruz
#We convert the number to a string and store it.
number_str = str(number)

# Sayıyı ters çevirdiğimizde sayının kendisine eşit yani palindrom olduğunu kontrol ediyoruz. Palindrom olup olmadığı bu kontrole göre ekrana yazdırılıyor.
# We check if the number is equal to its reverse (a palindrome check). Whether it is a palindrome or not is printed on the screen according to this check.
if number_str == number_str[::-1]:
    print("Bu sayı bir palindromdur(This number is a palindrome).")
else:
    print("Bu sayı bir palindrom değildir(This number is not a palindrome).")


'''
Program çalıştırıldığında(When the program is run);

PS C:\\Users\\CAN\\Desktop\\PythonPractises> python Example5.py
Bir sayı girin (Enter a number): 3003
Bu sayı bir palindromdur(This number is a palindrome).
PS C:\\Users\\CAN\\Desktop\\PythonPractises> python Example5.py
Bir sayı girin (Enter a number): 4545
Bu sayı bir palindrom değildir(This number is not a palindrome).
'''