# id132838372
"""Служба доставки."""


def minimum_platforms(robots: list[int], limit: int) -> int:
    """Вычисляет минимальное количество платформ для перевозки грузов."""
    count_platforms = 0
    first_robot = 0
    last_robot = len(robots) - 1
    while first_robot <= last_robot:
        if robots[first_robot] + robots[last_robot] <= limit:
            first_robot += 1
        last_robot -= 1
        count_platforms += 1
    return count_platforms


if __name__ == '__main__':
    robots = sorted(list(map(int, input().split())))
    limit = int(input())
    print(minimum_platforms(robots, limit))
