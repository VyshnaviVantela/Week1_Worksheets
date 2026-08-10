def convert_case(text, case_type):
    if case_type == 'upper':
       return text.upper()
    elif case_type == 'lower':
       return text.lower()
    elif case_type == 'title':
      return text.title()
    else:
      return "Invalid case_type"

"""'hello world', 'upper' -> 'HELLO WORLD' 
'HELLO WORLD', 'lower' -> 'hello world' 
'hello world', 'title' -> 'Hello World'
'hello', 'caps' -> 'Invalid case_type...'"""

print(convert_case('hello world', 'upper'))
print(convert_case('HELLO WORLD', 'lower'))
print(convert_case('hello world', 'title'))
print(convert_case('hello', 'caps'))
