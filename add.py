
def add_numbers(a, b):
    return a + b


def process_numbers(numbers):
    result = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            result.append(numbers[i] + numbers[j])

    return result