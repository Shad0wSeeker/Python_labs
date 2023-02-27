def even_numbers(numbers: list):
    answer = []

    for i in numbers:
        if i % 2 == 0:
            answer.append(i)
    return answer
