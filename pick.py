import json
import os
import random

def get_pick_data(file_path):
    """
    Chuyển đổi dữ liệu từ tệp JSON thành một danh sách các đối tượng Python.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_pick_data(data, file_path):
    """
    Lưu dữ liệu vào tệp JSON.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def pick_5(choices, queue):
    """
    Chọn 5 phần tử ngẫu nhiên từ danh sách choices 
    """
    # Lọc các lựa chọn không có trong hàng chờ
    available_choices = [choice for choice in choices if choice not in queue]

    # Chọn ra 5 lựa chọn ngẫu nhiên từ danh sách có sẵn
    selected_choices = random.sample(available_choices, min(5, len(available_choices)))


    return selected_choices

def pick_1(choices):
    """
    Chọn 1 phần tử ngẫu nhiên từ danh sách selected_choices 
    """
    idx = random.randint(0, len(choices) - 1)
    picked_choice = choices[idx]
    concept = random.random() < 0.5 
    print(f"Concept : {'正经' if concept == 1 else '不正经'}")
    return picked_choice

def update_queue(queue, picked_choice):
    """
    Cập nhật hàng chờ với lựa chọn được chọn.
    """
    queue.append(picked_choice)  # Thêm lựa chọn được chọn vào hàng chờ
    queue.pop(0)  # Xóa phần tử đầu tiên trong hàng chờ
    return queue

if __name__ == "__main__":
    # toàn bộ cái tên được lưu
    pool = get_pick_data('choices.json')
    choices = []
    for i in pool:
        choices.append(i['id'])

    # hàng chờ (những cái tên không đươc chọn)
    queue = get_pick_data('history.json')

    selected_choices = pick_5(choices, queue)
    picked_choice = pick_1(selected_choices)
    queue = update_queue(queue, picked_choice)
    save_pick_data(queue, 'history.json')
    
    print("\nSelected Choices:")
    for i in pool:
        if i['id'] in selected_choices:
            print(i['name'])
    
    for i in pool:
        if i['id'] == picked_choice:
            print(f"\nPicked Choice: {i['name']}")
    #print(queue)
        #for i in pool:
     #   if i['id'] not in queue:
      #      print(i['name'])
            