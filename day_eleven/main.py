from os import path
import math

print("enter total rounds")
total_rounds = int(input())
print("enter level of monkey worry")
worry_level = int(input())

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    input_monkeys = f.read().splitlines()

arr_monkeys = []

def calc_lcm(monkeys: list) -> int:
    getLCM = math.lcm(
        * map(
            lambda m: m['test'], monkeys
        )
    )
    return getLCM

def run_rounds(monkeys: list, rounds: int, worry_amount: int) -> int:
    inspected = [0] * len(monkeys)
    lcm_answer = calc_lcm(monkeys)
    monkey_business = [monkey['items'][:] for monkey in monkeys]
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            while monkey_business[i]:
                item = monkey_business[i].pop(0)
                operation = monkey['operation'] \
                    .replace('old', str(item))
                value_oper = eval(operation) // worry_amount
                target_monkey = monkey['true'] if value_oper % monkey['test'] == 0 else monkey['false']
                monkey_business[target_monkey] \
                    .append(value_oper if worry_amount != 1 else value_oper % lcm_answer)
                inspected[i] += 1
    inspected.sort()
    return inspected[-1] * inspected[-2]

for value in range(0, len(input_monkeys), 7):
    starting_items = input_monkeys[value+1].split(':')[1]
    arr_monkeys.append({
            'items': list(map(int, starting_items.split(','))),
            'operation': input_monkeys[value+2].split('=')[1].strip(),
            'test': int(input_monkeys[value+3].split()[-1]),
            'true': int(input_monkeys[value+4].split()[-1]),
            'false': int(input_monkeys[value+5].split()[-1])
    })

print("Answer",
      run_rounds(
        monkeys=arr_monkeys,
        rounds=total_rounds,
        worry_amount=worry_level
    )
)


