import random

# Demande à l'utilisateur de saisir la longueur du mots de passe
lengthPassword = int(input('Donner la longeur du mots de passe souhaité: '))
# Ensemble des lettres, chiffres et symbole qui composera le mots de passe
s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
# Assemble les caractères en supprimant les mots de passe
password = "".join(random.sample(s, lengthPassword))
print(password)