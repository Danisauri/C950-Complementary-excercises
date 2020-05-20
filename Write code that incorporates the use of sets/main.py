def sublists_of_length(full_list, length):
    # Your code here - implement sublists_of_length
    sublists = []
    for i in range(len(full_list)):
        result = full_list[i:(length+i)]
        if len(result) == length:
            sublists.append(result)
    return sublists

def all_sublists(full_list):
    # Your code here - implement all_sublists
    all_sublist = []
    modifier = 1
    range_list = []
    for element in range(len(full_list)):
        range_list.append(element)
    while len(range_list)>0:
        for i in range_list:
            all_sublist.append(full_list[i:modifier+i])
        modifier += 1
        range_list.pop()
    return all_sublist

def all_sublists_as_tuples(full_list):
    # Your code here - implement all_sublists_as_tuples
    tuples_sublist = []
    all_sublist = all_sublists(full_list)
    for element in all_sublist:
        tuples_sublist += (tuple(element), )
    return tuples_sublist

def distinct_sublists(full_list):
    # Your code here - implement distinct_sublists
    all_sublist = []
    for i in range(len(full_list)):
        for j in range(len(full_list)+1):
            generated_tuples = tuple(full_list[i:j])
            if len(generated_tuples) >0 and (generated_tuples not in all_sublist):
                all_sublist.append(generated_tuples)
    frozen = frozenset(all_sublist)
    return frozen



# No output is required for this lab. Unit tests are used to grade your submission.
# The code below shows a few samples to help you check your work before submitting.
# if __name__ == "__main__":
#     test_lists = [[4, 7, 1, 7], ["red", "green", "blue"], [1, 2, 1, 2]]
#     for test_list in test_lists:
#         print("Sublists of length 2 from " + str(test_list) + ":")
#         print("  " + str(sublists_of_length(test_list, 2)))
#         print("All sublists from " + str(test_list) + ":")
#         print("  " + str(all_sublists(test_list)))
#         print("All sublists as tuples from " + str(test_list) + ":")
#         print("  " + str(all_sublists_as_tuples(test_list)))
#         print("Distinct sublists from " + str(test_list) + ":")
#         print("  " + str(distinct_sublists(test_list)))
#         print()

print(distinct_sublists(['red', 'green', 'blue']))