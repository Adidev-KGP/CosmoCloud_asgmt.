list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
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

def merge_lists(list_1, list_2):
    merged_list = []
    for student_1 in list_1:
        merged_student = student_1.copy()
        for student_2 in list_2:
            if student_2["id"] == student_1["id"]:
                merged_student.update(student_2)
                break
        merged_list.append(merged_student)
    for student_2 in list_2:
        for student_1 in list_1:
            if student_1["id"] == student_2["id"]:
                break
        else:
            merged_list.append(student_2.copy())
    return merged_list

list_3 = merge_lists(list_1, list_2)

def print_merged_data():
	for var in list_3:
		print(var)

print_merged_data()
