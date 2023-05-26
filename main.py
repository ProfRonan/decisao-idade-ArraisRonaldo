abc = int(input("digite sua idade: "))

if abc < 0:
    print("Impossível!")
elif abc < 18:
        print("Não precisa se alistar.")
elif abc > 18 and abc < 65:
            print("Não esqueça de votar na próxima eleição.")
elif abc > 65:
                print("Vá descansar.")
else:
                print("Eita!")
