# task 1
def string_filter(arr):
    return [i for i in arr if type(i) != str]
    

#task 2
def first_non_repeating_letter(word):
    for letter in word:
        num = word.lower().count(letter.lower())
        if num == 1:
            return letter
    return ''

#task 3
def digital_root(num):
    def lowering(num):
        if num < 10:
            return num
        x = num % 10
        return x + lowering((num-x)//10)
    while num >= 10:
        num = lowering(num)
    return num

#task 4
def pairs_in_array(arr, target):
    count = 0
    seen = set()

    for num in arr:
        comp = target - num
    if comp in seen:
        count +=1
    seen.add(num)
    return count    


#task 5
def sort(list):
    arr = list.upper().split(';')
    split = []
    for name in arr:
        pair = name.split(':')
        name = pair[0]
        surname = pair[1]
        split.append(f"{surname}, {name}")
    split.sort()
    result = ''.join(split)
    return result


#main
print(string_filter([4,3,5,2,'f','d','q',7,9]))
print(first_non_repeating_letter("stress"))
print(digital_root(345))
print(pairs_in_array([2,4,2,6,7,2,5,1,5], 4))
list = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(sort(list))