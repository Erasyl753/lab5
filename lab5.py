
import re

# 1. 
print("1) a followed by zero or more b's:")
pattern1 = r'ab*'
test1 = ["a", "ab", "abb", "ac", "a123"]
for s in test1:
    print(f"{s} → {bool(re.fullmatch(pattern1, s))}")
print()

# 2. 
print("2) a followed by 2-3 b's:")
pattern2 = r'ab{2,3}'
test2 = ["abb", "abbb", "abbbb", "ab", "a"]
for s in test2:
    print(f"{s} → {bool(re.fullmatch(pattern2, s))}")
print()

# 3. 
print("3) lowercase joined by underscore:")
pattern3 = r'[a-z]+_[a-z]+'
test3 = ["abc_def", "a_b", "A_b", "abcDef"]
for s in test3:
    print(f"{s} → {bool(re.fullmatch(pattern3, s))}")
print()

# 4. 
print("4) Uppercase followed by lowercase letters:")
pattern4 = r'[A-Z][a-z]+'
test4 = ["Hello", "Python", "java", "A"]
for s in test4:
    print(f"{s} → {bool(re.fullmatch(pattern4, s))}")
print()

# 5. 
print("5) a ... b:")
pattern5 = r'a.*b$'
test5 = ["acb", "a123b", "ab", "abc", "a_b"]
for s in test5:
    print(f"{s} → {bool(re.match(pattern5, s))}")
print()

# 6. 
print("6) Replace space/comma/dot with colon:")
text6 = "Hello, world. How are you today"
result6 = re.sub(r'[ ,.]+', ':', text6)
print(result6)
print()

# 7. 
print("7) snake_case → camelCase:")
def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)

print(snake_to_camel("my_variable_name"))
print()

# 8. 
print("8) Split at uppercase letters:")
text8 = "SplitAtUpperCaseLetters"
result8 = re.findall('[A-Z][^A-Z]*', text8)
print(result8)
print()

# 9. 
print("9) Add spaces between capitalized words:")
text9 = "HelloWorldFromPython"
result9 = re.sub(r'([a-z])([A-Z])', r'\1 \2', text9)
print(result9)
print()

# 10. 
print("10) CamelCase → snake_case:")
def camel_to_snake(text):
    return re.sub(r'([A-Z])', r'_\1', text).lower().strip('_')

print(camel_to_snake("CamelCaseString"))
