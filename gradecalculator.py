#ESS:
#IA = marks * 0.476 (max 42, passing 20)
#P1 = marks * 0.667 (max 45, passing 22)
#P2 = marks * 0.769 (max 65, passing 25)

#Physics HL:
#IA = marks * 0.5 (max 48, passing 23)
#P1 = marks * 0.5 (max 40, passing 21)
#P2 = marks * 0.378 (max 95, passing 33)
#P3 = marks * 0.333 (max 60, passing 26)

#Math HL:
#IA = marks * 1 (max 20, passing 9)
#P1 = marks * 0.25(max 120, passing 42)
#P2 = marks * 0.25 (max 120, passing 52)
#P3 = marks * 0.33 (max 60, passing 27)

class Grade():
    ess_boundary = {1: range(16), 2: range(16,31), 3: range(31,42),
                4: range(42,54), 5: range(54,65), 6: range(65,77),
                7: range(77,101)}

    physics_hl_boundary = {1: range(17), 2: range(17,30), 3: range(30,42),
                4: range(42,52), 5: range(52,63), 6: range(63,72),
                7: range(72,101)}

    math_hl_boundary = {1: range(14), 2: range(14,28), 3: range(28,41),
                4: range(41,53), 5: range(53,66), 6: range(66,77),
                7: range(77,101)}

    def __init__(self, subject):
        self.subject = subject

    def three_papers(self):
        "check whether the subject's exam includes paper 3"
        three_papers = ['physics', 'math']
        return True if self.subject.lower() in three_papers else False
 
    def boundary(self):
        "defining the subject's boundary to its corresponding boundary"
        if self.subject.lower() == 'ess':
            return Grade.ess_boundary
        elif self.subject.lower() == 'physics':
            return Grade.physics_hl_boundary
        elif self.subject.lower() == 'math':
            return Grade.math_hl_boundary

    def ranges(self, comp):
        "return the range of min and max marks of the subject's requested paper, comp 0,1,2,3 means ia,p1,p2,p3"
        if self.subject == 'ess':
            if comp == 0:
                return range(20, 43)
            return range(22, 46) if comp == 1 else range(25, 66)
        elif self.subject == 'physics':
            if comp == 0:
                return range(23, 49)
            elif comp == 1:
                return range (21, 41)
            return range(33, 96) if comp == 2 else range(26, 61)
        elif self.subject == 'math':
            if comp == 0:
                return range(9, 21)
            elif comp == 1:
                return range (42, 121)
            return range(52, 121) if comp == 2 else range(27, 61)

    def overall_weighting(self):
        "provide the ratio / number / proportion that needs to be multiplied to corresponding compositions of subjects"
        if self.subject.lower() == 'ess':
            #[ia, p1, p2, p3]
            return [0.476, 0.667, 0.769, 0]
        if self.subject.lower() == 'physics':
            return [0.5, 0.5, 0.378, 0.333]
        if self.subject.lower() == 'math':
            return [1, 0.25, 0.25, 0.333]

    def final_grade(self, ia, p1, p2, p3 = 0):
        "calculation of final grade with all composition provided"
        grade = int(round(ia * self.overall_weighting()[0] + p1 * self.overall_weighting()[1]
                          + p2 * self.overall_weighting()[2] + p3 * self.overall_weighting()[3]))
        #after the grade is found, the boundary is iterated in order to find the key that contains the grade value
        for e in self.boundary():
            if grade in Grade.ess_boundary[e]:
                return '{} {} {}{}{}{}{}'.format('Final grade:', e, '(', grade, '/', 100, ')')

    def desired_grade_ia(self, ia, desired_grade):
        "calculation of paper 1, paper 2 and paper 3 (opt) required to achieve the desired_grade with the ia score provided"
        lst = []
        if self.three_papers():
            #for subjects with three papers, paper 1 and paper 2 score ranges were iterated one by one to be utilized in the calculation of the correct p1, p2 and p3 scores
            for e, f in zip(self.ranges(1), self.ranges(2)):
                p3 = int(round((self.boundary()[desired_grade][0] - ia * self.overall_weighting()[0]
                                - e * self.overall_weighting()[1] - f * self.overall_weighting()[2]) / self.overall_weighting()[3]))
                #if statement to eliminate the score that is out of the minimum boundary (passing)
                if e in self.ranges(1) and f in self.ranges(2) and p3 in self.ranges(3):
                    lst.append([e, f, p3])
            return '{}{}'.format('Your Paper 1, Paper 2 and Paper 3 scores should be one of these combinations of score: ', lst)
        else:
            for p1 in self.ranges(1):
                #for subjects with two papers, paper 1 score ranges were iterated one by one to do the calculation of correct p1 and p2 scores
                p2 = int(round((self.boundary()[desired_grade][0] - ia * self.overall_weighting()[0]
                                - p1 * self.overall_weighting()[1]) / self.overall_weighting()[2]))
                #if statement to eliminate not passing scores
                if p1 in self.ranges(1) and p2 in self.ranges(2):
                    lst.append([p1, p2])
            return '{}{}'.format('Your Paper 1 and Paper 2 scores should be one of these combinations of score: ', lst)

    def desired_grade_papers(self, desired_grade, p1, p2, p3 = 0):
        ia = int(float(((self.boundary()[desired_grade][0] - p1 * self.overall_weighting()[1] - p2
                         * self.overall_weighting()[2]) - p3 * self.overall_weighting()[3] / self.overall_weighting()[0])))
        if self.three_papers():
            #the output distinction between subjects with two papers and three papers
            return '{} {} {} {} {}'.format('Your IA score should be a minimum of', ia,
                                            'out of', 48 if self.subject.lower() == 'physics' else 20, 'marks') if ia < 48 else 'Not possible'
        return '{} {} {} {} {}'.format('Your IA score should be a minimum of', ia,
                                            'out of', 42, 'marks') if ia < 42 else 'Not possible'
        

while True:
    session = Grade(raw_input('Subject?'))
    ans = raw_input('Final grade calculation (0), desired grade with IA calculation (1)'
                    ', or desired grade with papers calculation (2?)')
    if ans == '0':
        ia = int(raw_input('IA score? '))
        p1 = int(raw_input('Paper 1 score? '))
        p2 = int(raw_input('Paper 2 score? '))
        p3 = int(raw_input('Paper 3 score?'))
        grade = session.final_grade(ia, p1, p2, p3)
        print grade
    elif ans == '1':
        ia = int(raw_input('IA score? '))
        desired_grade = int(raw_input('Desired grade? (1-7) '))
        grade = session.desired_grade_ia(ia, desired_grade)
        print grade
    elif ans == '2':
        p1 = int(raw_input('Paper 1 score? '))
        p2 = int(raw_input('Paper 2 score? '))
        p3 = int(raw_input('Paper 3 score? '))
        desired_grade = int(raw_input('Desired grade? (1-7) '))
        grade = session.desired_grade_papers(desired_grade, p1, p2, p3)
        print grade
    if raw_input('Retry?') == 'n':
        break