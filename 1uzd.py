def lasit_failu(fails):
    with open(fails, 'r') as f:
        saturs = f.read()
    return saturs

def main():
    fails = input("aka.txt")
    try:
        teksts = lasit_failu(fails)
        print("Faila saturs:")
        print(teksts)
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")

if __name__ == "__main__":
    main()