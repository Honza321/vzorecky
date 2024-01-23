#Přivítání uživatele
print("Vítejte v aplikaci pro výpočet obsahu obdélníku")

#deklarace (spíše inicializace) proměných, následně do nich ukládáme vstup
a = input ("Zadejte proměnou a: ")
b = input ("zadejte proměnou b: ")

a = int(a)
b = int(b)

#podmínka, kontrola zda v proměných není záporné číslo
if a>0 and b>0:
  #deklarace proměné výsledek
  vysledek = a*b
  #output pro výsledek
  print("výsledek je: ", vysledek)
  #pokud nebude platit první podmínka, provede se vždy else
else:
    #dáváme uživateli vědět , že něco zadal asi špatně
    print("Tak jsi nadrbaný?")

