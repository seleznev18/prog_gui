class class_check(object):
    def __init__(self,word):
        self.word=word
    ok=['0','1','2','3','4','5','6','7','8','9','.','-']
    def do_check_calc(self):
        if (len(self.word)==0):
            return False
        for i in self.word:
            if not(i in self.ok):
                return False
        if (self.word.count('.')>1 or self.word=='.' or self.word[0]=='.' \
            or self.word[-1]=='.' or self.word.count('-')>1 or \
            (self.word.count('-')==1 and self.word[0]!='-') or self.word=='-'):
            return False
        return True
    def do_check_rect(self):
        if (len(self.word)==0):
            return False
        for i in self.word:
            if not(i in self.ok):
                return False
        if ('-' in self.word):
            return False
        if (self.word.count('.')>1 or self.word=='.' or self.word[0]=='.'or self.word[-1]=='.'):
            return False
        if (float(self.word)==0):
            return False
        return True
    




