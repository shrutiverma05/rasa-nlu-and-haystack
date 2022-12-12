import streamlit as st
import csv

st.title('Haystack Editor')

head1, head2 = st.columns([3,3])
if head1.button('Load'):
    head1.write('File Loaded')
    indata = []
    index = set()
    with open('../Hosted Data/faq_data.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            indata.append(lines)
    indata.pop(0)
    question = []
    ans = []
    for i in range(len(indata)):
        index.add(indata[i][2])
    index = list(index)
    for i in range(len(index)):
        index[i] = int(index[i])
    for i in range(int(max(index))):
        question.append([])
        ans.append('')
    for i in indata:
        question[int(i[2])-1].append(i[0])
        ans[int(i[2])-1] = i[1]
    st.session_state.numberq = len(ans)
    for i in range(st.session_state.numberq):
        st.session_state['con'+str(i)] = len(question[i])
        st.session_state['ans'+str(i)] = ans[i]
        for j in range(st.session_state['con'+str(i)]):
            st.session_state[str(i)+'question'+str(j)] = question[i][j]
else:
    pass

if head2.button('Save'):
    head2.write('File Saved')
    save = []
    fields = ['question','answer','index']
    for i in range(len(st.session_state['question'])):
        for j in range(len(st.session_state['question'][i])):
            row = []
            row.append(st.session_state['question'][i][j])
            row.append(st.session_state['ans'][i])
            row.append(str(i+1))
            save.append(row)
    filename = '../Hosted Data/faq_data.csv'
    with open(filename, 'w',newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(save)
else:
    pass

with st.sidebar:
    numberq = st.number_input('Enter number of total Questions',min_value=0,step=1,key='numberq')
#st.write(st.session_state)

question = []
con = []
qno = []
data = {}
ans = []
for i in range(numberq):
    con.append('')
    question.append('')
    ans.append('')
    qno.append(0)
for i in range(numberq):
    con[i] = st.container()
    qno[i] = con[i].number_input(str(i+1)+'. Add or remove Q&A',min_value=0,step=1,key='con'+str(i))
    col1, col2 = con[i].columns([5, 5])
    que = []
    for j in range(qno[i]):
        que.append('')
    question[i] = que
    for j in range(qno[i]):
        question[i][j] = col1.text_input('Container '+str(i+1)+' Question '+str(j+1),label_visibility="visible" if j == 0 else "collapsed",key = str(i)+'question'+str(j))

    ans[i] = col2.text_area('Container '+str(i+1)+' Answer',label_visibility="visible",key = 'ans'+str(i))
# print(question)
# print(ans)
st.session_state['question'] = question
st.session_state['ans'] = ans