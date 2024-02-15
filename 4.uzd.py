def lasit_failu(fails):
    with open(fails, 'r') as f:
        saturs = f.read()
    return saturs

def main():
    fails = input("Lūdzu, ievadiet faila nosaukumu: ")
    paplasinajums = input("fails" un "txt")
    try:
        faila_nosaukums = f"{fails}.{paplasinajums}"
        teksts = lasit_failu(faila_nosaukums)
        print("Faila saturs:")
        print(teksts)
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")

if __name__ == "__main__":
    main()