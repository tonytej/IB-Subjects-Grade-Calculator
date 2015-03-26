'''
IA = marks * 0.476 (max = 42, passing = 20)
P1 = marks * 0.667 (max = 45, passing = 22)
P2 = marks * 0.769 (max = 65, passing = 25) 22 - 45  44 - 64
Final Grade:
1(0-15)
2(16-30)
3(31-41)
4(42-53)
5(54-64)
6(65-76)
7(77-100)
'''
boundary = {1: range(16), 2: range(16,31), 3: range(31,42),
                4: range(42,54), 5: range(54,65), 6: range(65,77),
                7: range(77,101)}

def essfinalgrade(ia, p1, p2,grade):
    grade = int(round(ia * 0.476 + p1 * 0.667 + p2 * 0.769))
    for e in boundary:
        if grade in boundary[e]:
            return '{} {}{}{}{}{}'.format(e, '(', grade, '/', 100, ')')

print essfinalgrade(28,23,44,0)

def desiredgradeia(ia, desired_grade):
    pass

def desiredgradepapers(p1, p2, desired_grade):
    ia = int(float(((boundary[desired_grade][0] - p1 * 0.667 - p2 * 0.769) / 0.476)))
    return '{}{}{}'.format(ia, '/', 42) if ia < 42 else 'Not possible'

print desiredgradepapers(23, 44, 7)

