
print("dictionaries ")
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
print (" 3.5 new  method way pythone")
heroes = {**mans, **woman, **avengers}
print(heroes, sep="/n")

#classic python way
print ("classic  way pythone")
superheroues = mans.copy()
superheroues.update(woman)
superheroues.update(heroes)

print(superheroues)

print ("for method way pythone")
# for
m1 ={}
for i in mans:
    m1[i]=mans[i]
for i in woman:
     m1[i] = woman[i]
for i in avengers:
    m1[i]=avengers[i]
print(m1)

