lang = ""

def madlibs_uk():
    adjective1 = str(input("Enter an Adjective: "))
    noun2 = str(input("Enter a noun: "))
    verb_past_tense3 = str(input("Enter a Verb, past tense: "))
    adverb4 = str(input("Enter an adverb: "))
    adjective5 = str(input("Enter an Adjective: "))
    noun6 = str(input("Enter a noun: "))
    noun7 = str(input("Enter a noun: "))
    adjective8 = str(input("Enter an Adjective: "))
    verb9 = str(input("Enter a Verb: "))
    adverb10 = str(input("Enter an adverb: "))
    verb_past_tense11 = str(input("Enter a Verb, past tense: "))
    adjective12 = str(input("Enter an Adjective: "))
    print("""
    Today I went to the zoo. I saw a(n) {} {} jumping up and down in 
    its tree. He {} {} through the large tunnel that led to its
    {} {}. I got some peanuts and passed them through the
    cage to a gigantic gray {} towering above my head. Feeding
    that animal made me hungry. I went to get a {} scoop of ice cream.
    It filled my stomach. Afterwards I had to {} {}
    to catch our bus. When I got home I {} my mom for 
    a {} day at the zoo. 
        """.format(adjective1, noun2, verb_past_tense3, adverb4, adjective5,
            noun6, noun7, adjective8, verb9, adverb10, verb_past_tense11,
            adjective12)
        .format(adjective1))

def madlibs_pl():
    adjective1 = str(input("Wpisz Przymiotnik: "))
    noun2 = str(input("Wpisz Rzeczownik: "))
    verb_past_tense3 = str(input("Wpisz Czasownik, czas przeszły: "))
    adverb4 = str(input("Wpisz Przysłówek: "))
    adjective5 = str(input("Wpisz Przymiotnik: "))
    noun6 = str(input("Wpisz Rzeczownik: "))
    noun7 = str(input("Wpisz Rzeczownik: "))
    adjective8 = str(input("Wpisz Przymiotnik: "))
    verb9 = str(input("Wpisz Czasownik: "))
    adverb10 = str(input("Wpisz Przysłówek: "))
    verb_past_tense11 = str(input("Wpisz Czasownik, czas przeszły: "))
    adjective12 = str(input("Wpisz Przymiotnik: "))
    print("""
    Dzisiaj poszedłem do zoo. widziałem {} {} skaczącego w górę i w dół na 
    swoim drzewie. On {} {} przez duży tunel, który prowadził do jego
    {} {}. Wziąłem trochę orzeszków ziemnych i przepuściłem je przez
    klatkę do gigantycznej szarej {} górującej nad moją głową. Karmienie
    tego zwierzęcia sprawiło, że poczułem głód. Poszedłem po {} gałkę lodów.
    Wypełniło mój żołądek. Potem musiałem {} {} aby złapać nasz autobus.
    Kiedy wróciłem do domu {} mamie za {} dzień w zoo. 
        """.format(adjective1, noun2, verb_past_tense3, adverb4, adjective5,
            noun6, noun7, adjective8, verb9, adverb10, verb_past_tense11,
            adjective12)
        .format(adjective1))

while lang.lower() != "english" or "polish":
    lang = str(input("Choose Language: English or Polish: "))
    if lang.lower() == "english":
        madlibs_uk()
        break
    elif lang.lower() == "polish":
        madlibs_pl()
        break
    else:
        print("Error. Please try again.")