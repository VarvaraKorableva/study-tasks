
"""
first = 'Hello World'
"This is a comment."
print(first)

print("i am a computer")

if 1 < 2 and 4 > 2:
    print('math is fun')    

length_of_string = 'what is my length?'
print(len(length_of_string))

print(length_of_string.upper())

print(length_of_string.lower())

print(length_of_string.title())

#From str to number
number_str = '1000' 
print(int(number_str))


number_four = 4
string_toconc = 'real'

print(str(number_four) + string_toconc)


print ('cool' * 3)

print(type([]))





##dont work???
name = input("What is your name?: ")
print ('Hi' + user_name)



apple = 'apple'
print(apple.index('e'))



small_list = [1,2,3,4]

for val in small_list:
    print(val * 20)


names = ['Mary', 'Sveta', 'Vlad']
letters = []

for word in names:
    letters.append(word[0])
    print (letters)

numbers_list = [1,2,3,4,5,6]
even_values = []

for num in numbers_list:
    if num % 2 == 0:
        even_values.append(num)
        print(even_values)
 

list1 = [2,3,5,7,5,0,1,6,'',9]
list2 = [2,5,6,'','',3,'e',7]

set1 = set(list1)
set2 = set(list2)

find_intersection = set1.intersection(set2)
result = list(find_intersection)

print (result)



names = ["Sveta", "Varvara", "Tom", "Ilia"]
newnames = []

for name in names:
    newnames.append(name.lower()[::-1])

    
    print (newnames)


first_str = 'first'
second_str = 'third'

set1 = set(first_str)
set2 = set(second_str)

general = set1.intersection(set2)

print(list(general))


array = []
for num in range(1,101):
    if num % 12 == 0:
        array.append(num)

print (array)


small_str = 'amazing'
vowels = 'aeiou'
result = []

for letter in small_str:
    if  letter not in vowels:
        result.append(letter)
print(result)


result_list = [[0, 1, 2] for _ in range(3)]

second_part_of_task = [[0,1,2,3,4,5,6,7,8,9] for _ in range(10)]

print(second_part_of_task)


data = [('name','Ema'), ('job','lawer')]

result = {key: value for key, value in data}

print(result)


first_list = ["CA", "NJ", "RI"]
second_list = ['California','New Jersey', 'Rhode Island']

my_list = {first_list[i] : second_list[i] for i in range(0,len(first_list))}

print(my_list)


first_list = ["a", "e", "i", "o", "u"]
second_list = [0, 0, 0, 0, 0]

my_list = {first_list[i] : second_list[i] for i in range(0,len(first_list))}

print(my_list)


list_1 = {char:0 for char in ["a", "e", "i", "o", "u"]}
print(list_1)


souse_str = 'awesome sause'
vowels = ["a", "e", "i", "o", "u"]

result = {item: souse_str.count(item) for item in vowels }

print(result)



print({i: chr(64 + i) for i in range(1, 27)})


def difference(a,b):
    return a - b

def print_day(num):
    days = {
        1: 'sunday', 2: 'monday', 3: 'tuesday', 
        4: 'wednesday', 5: 'thursday', 6:'friday', 7: 'saturday'
    }
    return days.get(num)

print(print_day(2))    


def print_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError:
        return None

print(print_day(-10))         


def last_element(list_l):
    if not list_l:
        return None

    return list_l[-1]

print(last_element([1,2,3]))

def last_element(list_l):
    try:
        return list_l[-1]
    except Exception:
        return None

print(last_element(6))   

def number_compare(a,b):

    if a == b: 
        return 'numbers are equal'    
    else:
        return 'second is greater' if b > a else 'first is greater'

print(number_compare(90,90))        


def single_letter_count(word,letter):
    if not letter.lower() in word.lower():
        return 0
    else: 
        return word.lower().count(letter.lower())

print(single_letter_count('aphbnAhkjhk','A'))


def single_letter_count(word,letter):
    return word.lower().count(letter.lower())

print(single_letter_count('aphbnAhkjhk','B'))


def multiple_letter_count(word):
    
    return {item: word.count(item) for item in word}

print(multiple_letter_count('momo'))


def list_manipulation( list_l, command, location, value = 0):
    if command == 'remove' and location == 'end':
        return list_l.pop() 
    elif command == 'remove' and location == 'beginning':
        return list_l.pop(0)
    elif command == 'add' and location == 'beginning':
        list_l.insert(0, value)
        return list_l
    elif command == 'add' and location == 'end':
        list_l.append(value) 
        return list_l 

print(list_manipulation([1,2,3], "remove", "beginning"))



def is_palindrome(word):
   return word.lower().replace(" ",'') == word.lower().replace(" ",'')[::-1]
               
print(is_palindrome('a man a plan a canal Panama'))



def frequency(l, count_in_list):
    return l.count(count_in_list)

print(frequency([1,2,3,4,4,4,4,5], 4)) 



def flip_case(sentence, letter):

    new_string = ''
    for item in sentence:
        if item.lower() == letter.lower():
            new_string += item.swapcase()
        else:
            new_string += item
            
    return new_string   
  
print(flip_case("bardy Bar bar", "b"))
    
 

def flip_case(sentence, letter):

    return '1'.join([item.swapcase() if item.lower() == letter.lower() else item for item in sentence])  
  
print(flip_case("bardy Bar bAr", "a"))
 

def multiply_even_numbers(array):
    new_arr = 1
    for item in array:
        if item % 2 == 0:
            new_arr = new_arr * item
    return new_arr 


def mode(l_of_numbers):
    numbers_dic = {l_of_numbers.count(key):key for key in l_of_numbers}
    max_num = max(numbers_dic.keys())
    return numbers_dic.get(max_num)

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))


def multiply_even_numbers(array):
    newArr = 1
    return prod([newArr * item if item % 2 == 0 else 1 for item in array])

print(multiply_even_numbers([2,3,4,5,6,5,2,6]))    

import math
def capitalize(some_string):
    return some_string.capitalize()

print (capitalize('fgjhjk'))

def compact(l):
    new_list = []
    for item in l:
        if item:
            new_list.append(item)
    return new_list


def compact(l):
    #return [item if item else 0 for item in l]
    return [item for item in l if item]


print(compact([0,1,2,"",[], False, {}, None, "All done"]))

def partition(l,func):
    true_l = []
    false_l = []

    result = [true_l, false_l]

    for item in l:
        if is_even(item):
            true_l.append(item)
        else:
            false_l.append(item)
    return result       
                

def is_even(num):
    return num % 2 == 0

print(partition([1,2,3,4], is_even)) # [[2,4],[1,3]]    

"""