

#первый способ создания словария
city = {

    'moskva': 77,
    'Kiev': 44,
    'donetsk': 62,

}
print(city)

#второй способ создания словария
cityusa = (['denver',100], ['newyork', 300], ['birminghan', 200])
print(cityusa)

#третий способ создания словария

citychina = {
'beyjin': 500,
    'hanoy': 505,
    'honkong': 507,
}
print (citychina)

#создаем переменную м в которую копируем обьединиям словари
m = city.copy()
m.update(cityusa)
m.update(citychina)
print(m)

#переменная новая мерджсити = берем слварь и апдейтим его другими словарями
mergecity = dict(city)
mergecity.update(cityusa)
mergecity.update(citychina)

print (mergecity)
