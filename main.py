import streamlit as st
import time

st.title('Streamlit 入門')
st.write('progress bar')

'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!'


left_column, right_column = st.columns(2, gap="small")
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

ep1 = st.expander('問い合わせ1')
ep1.write('問い合わせ内容を書く1')
ep2 = st.expander('問い合わせ2')
ep2.write('問い合わせ内容を書く2')
ep3 = st.expander('問い合わせ3')
ep3.write('問い合わせ内容を書く3')






# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition


# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 10))
# )
# 'あなたの好きな数字は', option, 'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('thumbnail.jpg')
#     st.image(img, caption='Itsukichan', use_column_width=True)

