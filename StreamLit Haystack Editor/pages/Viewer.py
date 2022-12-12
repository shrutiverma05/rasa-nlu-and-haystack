import streamlit as st

st.title("Haystack Editor")

if "num_questions" not in st.session_state:
    st.session_state.num_questions = 0

for k, v in st.session_state.items():
    st.session_state[k] = v

with st.sidebar:
    num_questions = st.number_input(
        "Enter number of total Questions",
        min_value=0,
        step=1,
        key="num_questions",
    )

head1, head2 = st.columns([3, 3])
if head1.button("Load"):
    head1.write("File Loaded")
else:
    pass

if head2.button("Save"):
    head2.write("File Saved")
else:
    pass

for i in range(num_questions):
    if f"qa_num_{i}" not in st.session_state:
        st.session_state[f"qa_num_{i}"] = 0

    if f"ans_{i}" not in st.session_state:
        st.session_state[f"ans_{i}"] = ""

    con = st.container()
    qa_num = con.number_input(
        str(i + 1) + ". Add or remove Q&A",
        min_value=0,
        step=1,
        key=f"qa_num_{i}",
    )
    col1, col2 = con.columns([5, 5])
    for j in range(qa_num):
        if f"question_{i}_{j}" not in st.session_state:
            st.session_state[f"question_{i}_{j}"] = ""

        col1.text_input(
            "Container " + str(i + 1) + " Question " + str(j + 1),
            label_visibility="visible" if j == 0 else "collapsed",
            key=f"question_{i}_{j}",
        )

    col2.text_input(
        "Container " + str(i + 1) + " Answer",
        label_visibility="visible",
        key=f"ans_{i}",
    )