import Bil

looping = True
Bmw_svart = Bil.Bil("Bmw", "svart", 3 )
Mercedes_gul = Bil.Bil("Mercedes", "Gul", 6)
Ferrari_röd = Bil.Bil("Ferrari", "Röd", 20)
Toyota_grön = Bil.Bil("Toyota", "Grön", 1)

billista = [Bmw_svart, Mercedes_gul, Ferrari_röd, Toyota_grön]

print(Bmw_svart.getFabrikat())


while looping:

    i = 0

    for Bil in billista:
        print(str(i+1) + "Fabrikat: " + Bil.getFabrikat() + ", Färg: " + Bil.getColor() )
        i += 1


    bil_nr = input("\n Mata In Bil Nummer För Vald Bil: ")

    print("\n Din " + billista[int(bil_nr) -1].fabrikat + ", Färg:" + billista[int(bil_nr) -1].color)

    svar_anvandare = input( " \nVill Du Avsluta Programmet? j/n : ")

    if (svar_anvandare == "j"):
        break

