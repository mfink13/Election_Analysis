print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]

>>> print(counties[-1])
Jefferson
>>> counties [-1]
'Jefferson'
>>> len(counties)
3
>>> counties[:2]
['Arapahoe', 'Denver']
>>> counties.append("El Paso")

>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2, "El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.remove("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2, "El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']

>>> counties.pop(3)
'Jefferson'
>>> counties.insert(3, "Jefferson")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.pop(2)
'El Paso'
>>> counties.pop(-1)
'El Paso'
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[2] = "El Paso"
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties[2] = "Denver"
>>> counties
['Arapahoe', 'Denver', 'Denver']
>>> counties.insert(1, "El Paso")
>>> counties
['Arapahoe', 'El Paso', 'Denver', 'Denver']
>>> counties[3] = "Jefferson"
>>> counties
['Arapahoe', 'El Paso', 'Denver', 'Jefferson']
>>> counties.remove("Arapahoe")
>>> counties
['El Paso', 'Denver', 'Jefferson']

>>> counties
['El Paso', 'Jefferson', 'Denver']
>>> counties.append("Arapahoe")
>>> counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
>>> my_tuple = ()
>>> counties_tuple = ("Arapahoe", "Denver", "Jefferson"
... )
>>> counties_tuple = ("Arapahoe", "Denver", "Jefferson")
>>> len(counties_tuple)
3
>>> counties_tuple[1]
'Denver'
>>> counties_tuple[:2]
('Arapahoe', 'Denver')
>>> counties_tuple[:-1]
('Arapahoe', 'Denver')

>>> counties_tuple[-2]
'Denver'
>>> counties_tuple[-1]
'Jefferson'
>>> my_dictionary = {}
>>> counties_dict = {}
>>> counties_dict["Arapahoe"] = 422829
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_dict["Denver"] = 463353
>>> counties_dict["Jefferson"] = 432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
3
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get("Denver")
463353

>>> counties_dict['Arapahoe']
422829
>>> voting_data = []

>>> voting_data.append({"county":"Arapahoe", "registered_voters":422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"country":"Jefferson", "registered_voters": 432438})

>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])

>>> print(voting_data)
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'country': 'Jefferson', 'registered_voters': 432438}]

>>> counties_dict[1] = ({"counties": "El Paso","registered_voters":461149})

>>> counties_dict[0] = ({"counties": "El Paso","registered_voters":461149})
>>> print(counties_dict
... )
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438, 1: {'counties': 'El Paso', 'registered_voters': 461149}, 0: {'counties': 'El Paso', 'registered_voters': 461149}}
>>> counties_dict.pop(0)
{'counties': 'El Paso', 'registered_voters': 461149}

>>> print(voting_data)
[{'county': 'Denver', 'registered_voters': 463353}, {'country': 'Jefferson', 'registered_voters': 432438}]
>>> counties_dict.pop(1)
{'counties': 'El Paso', 'registered_voters': 461149}
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> voting_data
[{'county': 'Denver', 'registered_voters': 463353}, {'country': 'Jefferson', 'registered_voters': 432438}]


>>> voting_data.append({"county": "El Paso", "registered_voters": 461149})
>>> voting.append

>>> voting_data
[{'county': 'Denver', 'registered_voters': 463353}, {'country': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}]
>>> voting_data[0], voting_data[2] = voting_data[2], voting_data[0]
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'country': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}]
>>> voting_data.append({"county": "Arapahoe", "resitered_voters": 422829})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'country': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'resitered_voters': 422829}]
>>> for county in counties_dict.keys():
...     print(county)
...
Arapahoe
Denver
Jefferson


counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
        print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)