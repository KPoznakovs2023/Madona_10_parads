def lasit_treto_rindu(fails):
    with open(fails, 'r') as f:
        rindas = f.readlines()
        if len(rindas) >= 3:
            return rindas[2]  # Trešā rinda (indeksā 2)
        else:
            return "Failā nav pietiekami daudz rindu"

def main():
    fails = input("aka.txt")
    try:
        saturs = lasit_treto_rindu(fails)
        print("Trešās rindas saturs:")
        print(saturs)
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")

if __name__ == "__main__":
    main()