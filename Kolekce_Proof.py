my_tuple = (1, 2, 3, 3, None, 4, 5)
#1, 2, 4, 5
print(my_tuple)
#3
print(f"3: {my_tuple[2]}")
#6
tuple2 = (1, 2, "Hello", [3, 4], {"a": 7, "b": 8}, {9, 7})
print(f"6: {tuple2}")
#7, 11
#my_tuple[2] = 10 #Vyhodi chybu
#8
length_tuple = len(my_tuple) 
print(f"8: {length_tuple}")
#9
newTuple = (20, 30)
twoTuples = my_tuple + newTuple
print(f"9: {twoTuples}")
#10 - Nelze odebrat prvek z tuple
#12
exists = 2 in my_tuple  
print(f"Exists: {exists}")
count = my_tuple.count(3)
print(f"12(count): {count}")
#13
print(f"13: {my_tuple[2]}") 


print("----")


my_list = [10, 10, 20, 30, None, 40, 50]
#1, 2, 4, 5
print(my_list)
#3
print(f"3: {my_list[2]}")
#6
list2 = [1, 2, "Hello", (3, 4), {"a": 7, "b": 8}, {9, 7}]
print(f"6: {list2}")
#7
my_list.append(11)
print(f"7: {my_list}")
#8
length_list = len(my_list) 
print(f"8: {length_list}")
#9
my_list.append(100)
my_list.insert(0, 200)
newList = [500, 600]
my_list.extend(newList)
print(f"9: {my_list}")
#10
my_list.pop()
del my_list[0]
my_list.remove(10)
print(f"10: {my_list}")
#11
my_list[0] = 5 #11
print(f"11: {my_list}")
#12
exists2 = 40 in my_list
print(f"Exists: {exists2}")
count = my_list.count(40)
print(f"12(count): {count}")
#13
print(f"13: {my_list[2]}")


print("----")


my_set = {3, 6, 6, 9, 12, None, 17}
#1, 2, 4, 5
print(my_set)
#3
#print(f"3: {my_set[1]}") #vyhodi chybu 
#6
set2 = {1, 2, (3, 4)}
print(f"6: {set2}")
#7
my_set.add(19)
print(f"7: {my_set}")
#8
length_set = len(my_set) 
print(f"8: {length_set}")
#9
my_set.add(50)
newSet = {100, 200}
my_set.update(newSet)
newSet2 = {500}
newSet3 = my_set.union(newSet2)
print(f"9.1: {my_set}")
print(f"9.2: {newSet3}")
#10
my_set.remove(17)
my_set.discard(12)
my_set.pop()
print(f"10: {my_set}")
#11 - Nelze upravit hodnotu prvku
#12
exists3 = 9 in my_set 
print(f"Exists: {exists3}")
#13 - Nelze vyhledat v poradi treti prvek v poradi


print("----")


my_dict = {"name": "John", None : None, "city": "New York", "surname" : "Karel", "surname" : "John", }
#1, 2, 4, 5
print(my_dict)
#3
print(my_dict["city"])
#6
dict2 = {"list": [1, 2, 3], "tuple": (4, 5, 6), "set": {7, 8, 9}, "dict": {"a": 10, "b": 11}, "string": "Hello World"}
print(f"6: {dict2}")
#7
my_dict["city"] = "Prague"
print(f"7: {my_dict}")
#8
length_dict = len(my_dict) 
print(f"8: {length_dict}")
#9
my_dict["sex"] = "male"
newInfo = {"age" : 20}
my_dict.update(newInfo)
my_dict.setdefault("birth_year", 2004)
print(f"9: {my_dict}")
#10
del my_dict["city"]
my_dict.pop("sex")
my_dict.popitem()
print(f"10: {my_dict}")
#11 
my_dict["name"] = "Dominik"
my_dict.update({"surname": "Petr"})
print(f"11: {my_dict}")
#12
exists4 = "age" in my_dict 
print(f"Exists: {exists4}")
valueDict = my_dict.get("name")
print(f"12(get): {valueDict}")
#13
key = list(my_dict.keys()) 
thirdKey = key[2]  
print(f"13: {my_dict[thirdKey]}")  


print("----")


my_string = "Hello World" 
#1, 2, 4, 5
print(my_string)
#3 
print(f"3: {my_string[2]}")
#6
testList = [1, 2, 3]
testString = f"List: {my_list}"
print(f"6: {testString}")  
#7
my_string += " Happy"
print(f"7: {my_string}")
#8
length_string = len(my_string) 
print(f"8: {length_string}")
#9
newString = "New".join(my_string)
newString2 = "House"
my_string = my_string + newString2
print(f"9.1: {newString}")
print(f"9.2: {my_string}")
#10 - Nelze smazat prvek z stringu
#11
my_string.replace("World", "Home") 
print(f"11: {my_string}")
#12
exists5 = "Hello" in my_string 
print(f"Exists: {exists5}")
count = my_list.count("l")
print(f"12(count): {count}")
subString = "World"
pisitionString = my_string.find(subString)
print(f"12(position): {pisitionString}")
print(my_string[7])
#13
print(f"13: {my_string[2]}")







