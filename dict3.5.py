
mans = {
 'shvarz': 120,
 'RAMBO': 100,
'VANDAMM': 75

}

print (mans)

woman = {

    'pamela':60,
    'britney': 65,
    'naomi':50
}

print (woman)
avengers = {
    'ironman':200,
    'halk': 1000,
    'spiderman': 45
}
print (avengers)

# 3.5 python way
heroes = {**mans, **woman, **avengers}
print(heroes, sep="/n")

#classic python way
superheroues = mans.copy()
superheroues.update(woman)
superheroues.update(heroes)

print(superheroues)

