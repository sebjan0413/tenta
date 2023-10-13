# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Prov.py: Skriv ett Pythonprogram som beräknar serieresistans och parallellresistans för de värden som användaren 
#          matar in. Användaren kan mata in 0, 1 eller flera värden följt av enter. Programmet beräknar sedan 
#          serieresistans och parallellresistans för de värden som matats in. Efter att resultatet skrivs ut 
#          avslutas programmet. Programmet använder inga externa bibliotek och behöver inte hantera exceptions.
#   
#          Author: Sebastian Jansson
#          Date:   2023-10-13
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Programmets hälsningsfras när det startas:
print('Ei22 - praktiskt prov ht23')

# Skapar en lista och en variabel för att lagra de inmatade värdena:
resistor_list = []
resistance = 0
r_tot_ser = 0
r_tot_par = 0

resistance = input('Ange resistorer: ')

if (resistance == ''):
    print('Serieresistans: 0')
    print('Parallellresistans: 0')

else:

    resistor_list = (resistance.split(' '))

    # Iterar igenom listan och omvandlar till ints:
    for i in range(0, len(resistor_list)):   
        (resistor_list[i]) = int(resistor_list[i])

    # Sätter seriekopplad resistans till summan av listans innehåll:
    r_tot_ser = sum(resistor_list)

    # Iterator för uträkning parallellresistans:
    for j in range(0, len(resistor_list)):
        r_tot_par += 1 / resistor_list[j]

    r_tot_par = 1 / r_tot_par

    # Utskrift innan programmet avslutas:

    print(f'Serieresistans: {r_tot_ser}')
    print(f'Parallellresistans: {r_tot_par}')
