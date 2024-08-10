first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(x) for x in first_strings if 5 <= len(x)]
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}
print(first_result)
print(second_result)
print(third_result)