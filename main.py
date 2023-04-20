list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "2", "name": "World", "age": 24},
    {"id": "3", "age": 10, "name": "Hello"},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    final_dict = {}   #Key = id , Value = Dictionary storing info like name,age,marks
    merged_list = []
    
    for student_1 in list_1:
        student_id = student_1["id"]
        merged_student = student_1
        
        for student_2 in list_2:
            if student_2.get("id") == student_id:
                merged_student.update(student_2)
                break
        
        id = merged_student['id']
        del merged_student['id']
        final_dict[id] = merged_student
    
    for student in list_2:
        id = student.get("id")
        if final_dict.get(id)==None:
            del student['id']
            final_dict[id] = student

    merged_list.append(final_dict)
    
    return merged_list




list_3 = merge_lists(list_1, list_2)
print (list_3)


# Access all info about student_id = 1
print(list_3[0]['1'])

#Access particular info like name of student_id = 1
print(list_3[0]['1']['name'])