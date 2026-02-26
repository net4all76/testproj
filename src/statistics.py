def mean(numbers):
    if not numbers:
        raise ValueError("빈 리스트는 계산할 수 없습니다.")
    return sum(numbers) / len(numbers)


def maximum(numbers):
    if not numbers:
        raise ValueError("빈 리스트는 계산할 수 없습니다.")
    return max(numbers)


def minimum(numbers):
    if not numbers:
        raise ValueError("빈 리스트는 계산할 수 없습니다.")
    return min(numbers)
