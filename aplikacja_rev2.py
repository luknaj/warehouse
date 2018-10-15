print("Witaj Złodupcu, jak Ci na imię?")
name: str=input()
print("cześć,"+name)
print("A więc, "+name+", ile masz lat?") # Czy musimy uzywac operatora +?
# Co się stanie jak zrobisz print("abc", "123", "def"), a  print("abc", 123, "def")?
age=input()
print("Ty stary zgredzie! Masz aż "+age+" lat?!")
print("Nie wiem czy o tym wiesz, ale Twoje imię posiada aż")
z=len(name)
print(z)
print("liter.")
liter_w_imieniu=int(z)*int(age)
print("iloczyn ilośći liter w Twoim imieniu oraz Twojego wieku wynosi:")
print(int(liter_w_imieniu))
print("ale to tylko ciekawostka")
print("Gdybyś chciał zapisać swoje imie od tyłu, tak będzie wyglądać:")
odwrocone=name [::-1]
print(odwrocone)
print("a jeżeli wypiszemmy Twoje imię tyle razy ile masz lat, będzie to wyglądało tak:")
print(name * int(age)) # Dwukrotnie wolasz int(y) - mozesz to przypisac do zmiennej.
input() # Czy to jest potrzebne?