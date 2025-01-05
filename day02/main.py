def helper(report):
    """Check the Problem conditions"""
    safe = False
    if report == sorted(report) or report == sorted(report, reverse=True):
        safe = True
        for i in range(1, len(report)):
            if (abs(int(report[i]) - int(report[i - 1])) < 1) or (
                abs(int(report[i]) - int(report[i - 1])) > 3
            ):
                safe = False
                break
    return safe


def solve2():
    """Solution of part-2"""
    ans = 0
    for report in data:
        for i in range(len(report)):
            updated_report = report[:i] + report[i + 1 :]
            if helper(updated_report):
                ans += 1
                break
    return ans


def solve1():
    """Solution of part-1"""
    ans = 0
    for report in data:
        if helper(report):
            ans += 1
    return ans


data = []

with open("./inputs.txt", "r", encoding="utf-8") as file:
    for line in file:
        data.append(list(map(int, line.strip().split())))

print(f"Solution of part-1: {solve1()}")
print(f"Solution of part-2: {solve2()}")
