'''
IA = marks * 0.476 (max = 42, passing = 20)
P1 = marks * 0.667 (max = 45, passing = 22)
P2 = marks * 0.769 (max = 65, passing = 25)
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

def essfinalgrade(ia, p1, p2):
    grade = int(round(ia * 0.476 + p1 * 0.667 + p2 * 0.769))
    for e in boundary:
        if grade in boundary[e]:
            return '{} {} {}{}{}{}{}'.format('Final grade:', e, '(', grade, '/', 100, ')')

def desiredgradeia(ia, desired_grade):
    lst = []
    for e in range(22, 46):
        p2 = int(round((boundary[desired_grade][0] - ia * 0.476 - e * 0.667)/0.769))
        lst.append([e, p2])
    return '{}{}'.format('Your Paper 1 and Paper 2 scores should be one of these combinations of score: ', lst)

def desiredgradepapers(p1, p2, desired_grade):
    ia = int(float(((boundary[desired_grade][0] - p1 * 0.667 - p2 * 0.769) / 0.476)))
    return '{} {} {} {} {}'.format('Your IA score should be a minimum of', ia, 'out of', 42, 'marks') if ia < 42 else 'Not possible'

while True:
    ans = raw_input('Final grade calculation (0), desired grade with IA calculation (1)'
                    ', or desired grade with papers calculation (2?)')
    if ans == '0':
        ia = int(raw_input('IA score? (max 42 marks) '))
        p1 = int(raw_input('Paper 1 score? (max 45 marks) '))
        p2 = int(raw_input('Paper 2 score? (max 65 marks) '))
        print essfinalgrade(ia, p1, p2)
    elif ans == '1':
        ia = int(raw_input('IA score? (max 42 marks) '))
        desired_grade = int(raw_input('Desired grade? (1-7) '))
        print desiredgradeia(ia, desired_grade)
    elif ans == '2':
        p1 = int(raw_input('Paper 1 score? (max 45 marks) '))
        p2 = int(raw_input('Paper 2 score? (max 65 marks) '))
        desired_grade = int(raw_input('Desired grade? (1-7) '))
        print desiredgradepapers(p1, p2, desired_grade)
    if raw_input('Retry?') == 'n': break