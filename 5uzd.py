def ierakstit_vardu_faila(vards, fails):
    with open(fails, 'w') as f:
        f.write(vards)

def main():
    vards = input("Lūdzu, ievadiet savu vārdu: ")
    fails = "lietotajs.txt"  # Faila nosaukums, kurā saglabāt vārdu
    try:
        ierakstit_vardu_faila(vards, fails)
        print(f"Jūsu vārds '{vards}' ir ierakstīts failā '{fails}'.")
    except Exception as e:
        print("Kļūda ierakstot vārdu failā:", e)

if __name__ == "__main__":
    main()