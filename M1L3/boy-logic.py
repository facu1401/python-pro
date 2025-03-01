import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)



    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def gen_titan_name(): #defino funcón
    titanes = [
        "titan Godzilla", "titan King Kong", "titan Mothra", "titan Rodan", "titan Ghidorah", 
        "Mechagodzilla", "titan Biollante", "titan Destoroyah", "titan Hedorah", 
        "titan Anguirus", "titan Kumonga", "titan Baragon", "titan Titanosaurus", "titan Kamacuras"
        "titan Silla", "titan Zilla", "titan Quetzalcoalt", "Mechagidora", "titan M.U.T.Os"
    ] #array
    return random.choice(titanes)

print(gen_titan_name())