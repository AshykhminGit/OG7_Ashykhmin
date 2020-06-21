

my_dict = {
    'a': 645,
    'b': 3987,
    'c': 93,
    'd': 111,
    'e': 646,
    'f': 20
}
#самое большое число
print(max(zip(my_dict.values(),my_dict.keys())))
#три самых больших числа с функцией get reverse =True  -  от большего к меньшему  [ количество ключей значений]
print (sorted(my_dict, key=my_dict.get, reverse=True)[:3])
#три самых  маленьких числа с функцией get reverse = false  -  от  меньшего к большему  [ количество ключей значений]
print (sorted(my_dict, key=my_dict.get, reverse=False)[:3])