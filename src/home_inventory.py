from cmath import e
import json 
from secrets import choice 

with open('home_inventory.json', 'r') as f:
    data = json.load(f)
     

items= data.get('items', [])

while True: 
    print('-'*40)
    print('My Home Inventory')
    print('1.Display list of Home Inventory')
    print('2.Search for items')
    print('3.Add new items')
    print('4.Exit inventory')
    print('-'*40)
    choice = int(input())

    if choice == 1:
      print('id\titem\t\t\tcount')
      print('-'*40)
      for item in items:
          print(f'{item.get("id")}\t{item.get("item")}\t\t{item.get("count")}')
      print('-'*40)
    elif choice == 2:
        search_items = map(int, input('please enter item id:').split(','))
        print('id\titem\t\t\tcount')
        print('-'*40)
        try:
          for search_item in search_items:
            for item in items:
              if item['id'] == search_item:
                print('-'* 4 + 'Showing for Searched items' + '-'*4 )
                print('-'*40)
                print(f'{item.get("id")}\t{item.get("item")}\t\t{item.get("count")}')
                break
        except:
         print('Wrong Item Selection search with ID number again')
    elif choice == 3:
        item_name = input('Enter the item name: ')
        item_count = int(input('Enter the count:'))
        items.append({
            'id':len(items)+1,
            'item' : item_name,
            'count':item_count
        })
        data['items'] = items
        with open('home_inventory.json', 'w') as f:
            json.dump(data, f)
        print('New item added successfully!')
    elif choice == 4:
      print('Exiting, Good bye!')
      break
