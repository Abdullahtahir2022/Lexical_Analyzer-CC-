#Content Table
Table=[]

NFA_Keyword = {0:{'i':1, 'f':4, 's':9, 'w':14, 'e':18},
        1:{'f':3,'n':2},2:{'t':3},3:{'':3},4:{'o':8,'l':5},
        5:{'o':6},6:{'a':7},7:{'t':3},8:{'r':3},9:{'t':10},
        10:{'r':11},11:{'i':12},12:{'n':13},13:{'g':3},14:{'h':15},
        15:{'i':16},16:{'l':17},17:{'e':3},18:{'l':19},19:{'s':20},
        20:{'e':3}  }

NFA_Delimiter = {0:{' ':1, '+':1, '{':1, '}':1, '-':1 ,'*':1, '/':1,
                    ',':1, ';':1, '>':1, '<':1, '=':1,'==':1, '(':1,
                    ')':1, '[':1,']':1, '<=':1, '>=':1, '&':1,
                    '!':1, '|':1},
                1:{'':1}    }

NFA_A_Operator =  {0:{'+':1, '-':1, '/':1, '*':1},
                 1:{'+':1}}
NFA_R_Operator =  {0:{'=':1, '<':1, '>':1},
                    1:{'=':1}}


NFA_Integer = {0:{'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'0':1},
                    1:{'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'0':1}}

NFA_RealNumbers = {0:{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'0':0,'.':1},
                    1:{'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'0':1}}


NFA_ValidIdentifier = {0:{'a':2,'b':2,'c':2,'d':2,'e':2,'f':2,'g':2,'h':2,'i':2,'j':2,'k':2,'l':2,
                          'm':2,'n':2,'o':2,'p':2,'q':2,'r':2,'s':2,'t':2,'u':2,'v':2,'w':2,'x':2,
                          'y':2,'z':2,'A':2,'B':2,'C':2,'D':2,'E':2,'F':2,'G':2,'H':2,'I':2,'J':2,
                          'K':2,'L':2,'M':2,'N':2,'O':2,'P':2,'Q':2,'R':2,'S':2,'T':2,'U':2,'V':2,
                          'W':2,'X':2,'Y':2,'Z':2},
                        1:{'':1},
                        2:{'a':2,'b':2,'c':2,'d':2,'e':2,'f':2,'g':2,'h':2,'i':2,'j':2,'k':2,'l':2,
                           'm':2,'n':2,'o':2,'p':2,'q':2,'r':2,'s':2,'t':2,'u':2,'v':2,'w':2,'x':2,
                           'y':2,'z':2,'A':2,'B':2,'C':2,'D':2,'E':2,'F':2,'G':2,'H':2,'I':2,'J':2,
                           'K':2,'L':2,'M':2,'N':2,'O':2,'P':2,'Q':2,'R':2,'S':2,'T':2,'U':2,'V':2,
                           'W':2,'X':2,'Y':2,'Z':2,'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,
                           '9':2,'0':2}}

NFA_string={0:{'"':1},
            1:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,
            'm':1,'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,
            'y':1,'z':1,'A':1,'B':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,
            'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,'Q':1,'R':1,'S':1,'T':1,'U':1,'V':1,
            'W':1,'X':1,'Y':1,'Z':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,
            '9':1,'0':1, '+':1, '{':1, '}':1, '-':1 ,'*':1, '/':1,',':1, ';':1, '>':1,
            '<':1, '=':1,'==':1, '(':1,')':1, '[':1,']':1, '.':1, '<=':1, '>=':1, '&':1,
            '!':1, '|':1,'"':2},
            2:{'':2}}





#Subpart of lexical Analyzer--------Runs Strings on NFA's
def Accept(transitions,initial,accepting,s):
    state = initial
    for c in s:
        if c in list(transitions[state].keys()):
            state = transitions[state][c]
        else:
            return False
    return state in accepting


#Output the valid Token
def Lexical_Analyzer(string):
    if Accept(NFA_A_Operator,0,{1},string)==True:
        print("<", "Arithmetic Operator",", ",string, ">")
    elif Accept(NFA_R_Operator,0,{1},string)==True:
        print("<", "Relational Operator",", ",string,">")
    elif Accept(NFA_Keyword,0,{3},string)==True:
        print("<", string,",>")
    elif Accept(NFA_ValidIdentifier,0,{2},string)==True and Accept(NFA_Keyword,0,{3},string)==False:
        if string not in Table:
            Table.append([string,"Null"])
        print("< id, ",len(Table)-1,">")
    elif Accept(NFA_Integer,0,{1},string)==True:
        if Table[len(Table)-1][1]=='Null':
            Table[len(Table)-1][1]=string
        print("< Interger , ",len(Table)-1,">")
    elif Accept(NFA_string,0,{2},string)==True:
        if Table[len(Table)-1][1]=='Null':
            Table[len(Table)-1][1]=string
        print("< String , ",len(Table)-1,">")
    elif Accept(NFA_RealNumbers,0,{1},string)==True:
        if Table[len(Table)-1][1]=='Null':
            Table[len(Table)-1][1]=string
        print("< Real Number , ",len(Table)-1,">")
    elif Accept(NFA_Delimiter,0,{1},string)==True and string!=' ':
        print("< Symbol, ",string,">")
    elif string!=' ' and string!='':
        print(string,"<---","Not Recongnized!")

 





    










#For File Read
f = open("C_file", "r")
start=0
end=0
data=f.read()
#For extracting Sub strings and passing them to Lexical Analyzer
print("<======================= Tokens ==========================>")
for x in range(len(data)):
    if (Accept(NFA_Delimiter,0,{1},data[x])==True):
        subst=data[start:end]
        if(Accept(NFA_R_Operator,0,{1},data[end-1])==True and Accept(NFA_R_Operator,0,{1},data[end])==True):
            subst1=data[end-1:end+1]
        elif (Accept(NFA_Delimiter,0,{1},data[x])==True):
            subst1=data[end:end+1] 
        Lexical_Analyzer(subst)
        Lexical_Analyzer(subst1)
        start=end+1
    end+=1
print("<================== Table Contents + Values ===============>")
print(Table)
print("<==========================================================>")
