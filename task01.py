# The Exam Resuults

# Данная программа обрабатывает результаты экзамена

def count_mark(ls, mark):
    count = 0
    for index in range(len(ls)):
        if ls[index] == mark:
            count += 1
    return count


def calculate(ls, start, end):
    capacity = []

    for mark in range(start, end + 1):
        cap = count_mark(ls, mark)
        capacity.append(cap)

    return capacity


def main():
    ls = [5, 4, 5, 0, 1, 3, 4, 2, 4, 0, 2, 5, 4, 2, 3, 3, 5, 5, 4, 5]
    print("Исходные оценки:", *ls)
    print("Результаты экзамена:")
    count = count_mark(ls, 5)
    print(f"пятерок - {count / len(ls) * 100} % ({count})")
    count = count_mark(ls, 4)
    print(f"четверок - {count / len(ls) * 100} % ({count})")
    count = count_mark(ls, 3)
    print(f"троек - {count / len(ls) * 100} % ({count})")
    count = count_mark(ls, 2)
    print(f"двоек - {count / len(ls) * 100} % ({count})")
    count = count_mark(ls, 1)
    print(f"единиц - {count / len(ls) * 100} % ({count})")
    count = count_mark(ls, 0)
    print(f"нулей - {count / len(ls) * 100} % ({count})")


if __name__ == "__main__":
    main()
