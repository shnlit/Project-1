from enum import unique

shopping_list = ['carrot', 'apple', 'banana', 'melon']
shopping_list.append('peach')
print(shopping_list)
unique_items = set(shopping_list)
print(unique_items) # оно отличается от списка уникальными именами без четкого порядка
