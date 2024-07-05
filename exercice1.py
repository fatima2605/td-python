note =float (input("entrez votre note (entre 0 et 20) : "))
if note >= 18:
    print("Exellent")
elif 16<=note<18:
    print("tres bien")
elif 14<=note< 16:
    print("bien")
elif 12<=note < 14:
    print("satisfaisant")
elif 10<=note < 12:
    print("passable")
else :
    print("echec cest pas bon")