def check_the_number(N):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        list_of_numbers.append(i)

        if N in list_of_numbers:
            result = "True"
        else:
            result = "False"
    return result

N = 7
assert check_the_number(N) == "False"

N = 2
result = check_the_number(N)
print(result)
# đáp án : câu a