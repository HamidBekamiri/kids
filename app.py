import streamlit as st


def main():
    # st.title('Game Setup')

    # Player selection
    col1, col2, col3, col4 = st.columns(4)
    st.button('Kick off')
    # with col1:
    #     if st.button('1 Player'):
    #         st.write('1 Player Selected')
    # with col2:
    #     if st.button('2 Players'):
    #         st.write('2 Players Selected')
    # with col3:
    #     if st.button('3 Players'):
    #         st.write('3 Players Selected')
    # with col4:
    #     if st.button('4 Players'):
    #         st.write('4 Players Selected')

    # Game mode selection
    st.header('Game Mode')
    col1, col5, col6 = st.columns(3)
    with col1:
        if st.button('1 Player'):
            st.write('1 Player Selected')
    with col5:
        if st.button('Online'):
            st.write('Online Mode Selected')
    with col6:
        if st.button('Cup'):
            st.write('Cup Mode Selected')

if __name__ == "__main__":
    main()

st.write('Developed by Zhiar and Shayan')
