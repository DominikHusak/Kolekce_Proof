#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12:
my_tuple = (1, 2, 3, 3, None, 4, 5)
v_tuple = ((1, 2), (3, 4), (5, 6))
print(my_tuple[0]) #3
print(my_tuple[2])
# my_tuple[0] = 7 #7 Vyhodí chybu
print(my_tuple) #1, 2
print(v_tuple) #6
length_tuple = len(my_tuple) #8
print(length_tuple)#8
new_element = 4 #9
new_tuple = my_tuple + (new_element,)#9
print(new_tuple)
exists = 2 in my_tuple #12, vypíše true nebo false podle zoho jestli je prvek v kolekci 
print(f"Exists: {exists}")

my_list = [10, 10, 20, 30, None, 40, 50]
v_list = [[1, 2], [3, 4], [5, 6]]
print(my_list[0])   #3
print(my_list[3])
print(my_list) #1, 2
my_list.append(11) #7, 9
print(my_list)
print(v_list)#6
length_list = len(my_list) #8
print(length_list)#8
new_element2 = 4 #9
my_list.insert(1, new_element2)#9
#new_elements = [4, 5, 6]#9
#my_list.extend(new_elements)#9
print(my_list)
my_list.pop(0)#10, odebere a přidá prvek na základě indexu
my_list.remove(50)#10odebere prvek dle zadané hodnoty
del my_list[2]#10odebre prvek na základě indexu
print(my_list)
my_list[0] = 5 #11
exists2 = 40 in my_list #12, vypíše true nebo false podle toho jestli je prvek v kolekci 
print(f"Exists: {exists2}")
count = my_list.count(40)#12, vrací počet výskytů 40
print(count)

my_set = {3, 6, 9, 12, None, 17}
v_set = {frozenset({1, 2}), frozenset({3, 4}), frozenset({5, 6})}
#print(my_set[3]) #3 Vyhodí chybu
print(my_set) #1, 2
print(v_set) #6
my_set.add(19) #7, 9
print(my_set)
length_set = len(my_set) #8
print(length_set)#8
my_set.remove(3) #10, odebere prvek dle zadané hodnoty, dojde k chybě pokud zadaná hodnota není v kolekci
my_set.discard(6)#10, odebere prvek dle zadané hodnoty, nedojde k chybě pokud zadaná hodnota není v kolekci
print(my_set)
exists3 = 9 in my_set #12, vypíše true nebo false podle toho jestli je prvek v kolekci 
print(f"Exists: {exists3}")

my_dict = {"name": "John", "age": None, "city": "New York"}
v_dict = {"data1": {"value1": 10, "value2": 20}, "data2": {"value1": 30, "value2": 40}}
print(my_dict["city"]) #3
print(my_dict) #1, 2
my_dict["job"] = "teacher" #7
print(v_dict) #6
print(my_dict)
length_dict = len(my_dict) #8
print(length_dict)#8
new_key = "sex"#9
new_value = "male"#9
my_dict[new_key] = new_value#9
print(my_dict)
removed_value = my_dict.pop("name")#10, odebre klíč a hodnotu dle zadaného klíče
removed_item = my_dict.popitem()#10, odebere a vrátí poslední klíč a hodnotu 
del my_dict["age"]#10, odebere klíč a hodnotu dle zadaného klíče
my_dict["age"] = 31 #11
exists4 = "age" in my_dict #12, vypíše true nebo false podle toho jestli je klíč v kolekci 
print(f"Exists: {exists4}")

my_string = "Hello World, [Hi]"   
print(my_string[0]) #3
print(my_string[7])
print(my_string) #1, 2, 6
length_string = len(my_string) #8
print(length_string)#8
exists5 = "Hello" in my_string #12, vypíše true nebo false podle toho jestli je klíč v kolekci 
print(f"Exists: {exists5}")
my_string = my_string.replace("World", "House") #11
position = my_string.find("Hello")  #12 vrací pozici World, -1 pokud nenalezen
print(f"Position: {position}")






