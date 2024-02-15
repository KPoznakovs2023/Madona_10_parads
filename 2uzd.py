import csv

def lasit_csv(fails):
    otrais_kolonnas_dati = []
    with open(fails, 'r', newline='') as csvfile:
        csvlasitajs = csv.reader(csvfile)
        for rinda in csvlasitajs:
            if len(rinda) > 1:  # Pārbauda, vai rindā ir vismaz divi elements
                otrais_kolonnas_dati.append(rinda[1])  # Saglabā otrās kolonnas datus
    return otrais_kolonnas_dati

def main():
    fails = input("aka.csv")
    try:
        otrais_kolonnas_dati = lasit_csv(fails)
        print("Otrais kolonnas dati:")
        for dati in otrais_kolonnas_dati:
            print(dati)
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")

if __name__ == "__main__":
    main()