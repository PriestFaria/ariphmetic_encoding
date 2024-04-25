from decimal import Decimal


class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Letter(Interval):
    def __init__(self, letter, left, right):
        super().__init__(left, right)
        self.letter = letter


message = input()
alphabet = []
for i in message:
    if not (i in alphabet):
        alphabet.append(i)

diction = {}
letter_intervals = {}
for i in alphabet:
    diction[i] = Decimal(str(message.count(i)))
diction = {k: v for k, v in sorted(diction.items(), key=lambda item: item[1])}
for i in diction.keys():
    diction[i] = diction[i] / Decimal(str(len(message)))
alphabet = []
for i in diction.keys():
    alphabet.append(i)
print(alphabet)
main_interval = Interval(Decimal('0'), Decimal('1'))
k = 0
for i in diction.keys():
    if k == 0:
        new_interval = Letter(i, main_interval.left, main_interval.left + diction[i])
        letter_intervals[i] = new_interval
        k += 1
    else:
        new_interval = Letter(i, letter_intervals[alphabet[k - 1]].right,
                              letter_intervals[alphabet[k - 1]].right + diction[i])
        letter_intervals[i] = new_interval
        k += 1

for i in letter_intervals.values():
    print(i.letter, i.left, i.right)

for char in message:
    main_interval.left = letter_intervals[char].left
    main_interval.right = letter_intervals[char].right
    k = 0
    for i in letter_intervals.keys():
        if k == 0:
            new_interval = Letter(i, main_interval.left,
                                  main_interval.left + (main_interval.right - main_interval.left) * diction[i])
            letter_intervals[i] = new_interval
            k += 1
        else:
            new_interval = Letter(i, letter_intervals[alphabet[k - 1]].right,
                                  letter_intervals[alphabet[k - 1]].right + (main_interval.right - main_interval.left) *
                                  diction[i])
            letter_intervals[i] = new_interval
            k += 1
    print("==========================")
    for i in letter_intervals.values():
        print(i.letter, i.left, i.right)
print('Average: ', (main_interval.right + main_interval.left) / Decimal('2'))
print(f'Final interval: [{main_interval.left};{main_interval.right})')

