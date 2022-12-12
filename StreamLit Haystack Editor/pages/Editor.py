import streamlit as st

# Using object notation
with st.sidebar:
    numberq = st.number_input('Enter number of total Questions',min_value=0,step=1)

col1, col2 = st.columns([5, 5])
que = []
con = []
qno = []
with col1:
    if numberq:
        for i in range(numberq):
            con.append('')
            qno.append(0)
        for i in range(numberq):
            con[i] = st.container()
            qno[i] = con[i].number_input(str(i+1)+'. Add or remove Q&A',min_value=0,step=1)
#            con[i].write('Enter the Questions')
            if qno:
                for j in range(qno[i]):
                    que.append('')
                for j in range(qno[i]):
                    que[j] = con[i].text_input('Container '+str(j+1)+'Question '+str(i+1),label_visibility="collapsed")

                #con[i].json(que)

con2 = []
ans = []
with col2:
    if numberq:
        for i in range(numberq):
            con2.append('')
            ans.append('')
#            qno2.append(0)
        for i in range(numberq):
            con2[i] = st.container()
            #con2[i].json(qno)
#            qno[i] = con[i].number_input(str(i+1)+'. Add or remove Q&A',min_value=0,step=1)
#            con[i].write('Enter the Questions')
            # if qno:
            
            ans[i] = con2[i].text_area('Q&A '+str(i+1)+' Answer ',label_visibility="visible")
            # for j in range(qno[i]):
            #     con2[i].markdown('')
#,height = int((110/2)*(qno[i]+1))    
