def count_items(items_list):
    freq = {}
    for item in items_list:
      freq[item] = freq.get(item, 0) + 1
    return freq 

#['apple','banana','apple','cherry','banana','apple']

print(count_items(['apple','banana','apple','cherry','banana','apple']))
