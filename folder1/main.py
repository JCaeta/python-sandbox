# selected_fields = [
#     {'name': 'id', 'default': True},
#     {'name': 'age', 'default': True},
#     {'name': 'gender', 'default': True}
# ]

# included_fields = [
#     {'name': 'Employee code', 'default': False},
# ]

# # Extract the names from selected_fields for faster lookup
# selected_field_names = {field['name'] for field in selected_fields}

# # Use next with a generator expression to find the first field not in selected_fields
# not_included_field = next((field for field in included_fields if field['name'] not in selected_field_names), None)

# print('not_included_field: ', not_included_field)