def calculate_structure_sum(data_):
    sum_= 0
    data_change = []
    if len(data_) == 1:
        return data_[0]
    else:
        for i in data_:
            if type(i) == str:
                data_change.append(len(i))
                continue
            if type(i) == list or type(i) == tuple or type(i) == set:
                for j in i:
                    data_change.append(j)
                continue
            if type(i) == dict:
                data_change.append(list(i.keys()))
                data_change.append(list(i.values()))
            else:
                sum_+=i
        data_change.append(sum_)
    return calculate_structure_sum(data_change)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)