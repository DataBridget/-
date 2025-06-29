import pandas as pd
import streamlit as st
import os

# ��ӡ��ǰ����Ŀ¼
print("��ǰ����Ŀ¼:", os.getcwd())

# ����ҳ�����ã�����ģʽ��
st.set_page_config(layout="wide")

# �����˵��
st.title('��Ʊ������Ϣ��ѯӦ��')
st.markdown("�����Ʊ�����ѯ��ҵ��Ϣ��������·���������")

try:
    # ʹ�����·����ȡ Excel �ļ�
    df = pd.read_excel('��Ʊ����.xlsx', sheet_name='Sheet1', engine='openpyxl')

    # ������������ʹ������׶�
    df = df.rename(columns={
        'Unnamed: 0': '��Ʊ����',
        '��ҵ����': '��ҵ����',
        '���ּ���Ӧ��': '���ּ���Ӧ��',
        '�˹����ܼ���': '�˹����ܼ���',
        '����������': '����������',
        '�����ݼ���': '�����ݼ���',
        '�Ƽ��㼼��': '�Ƽ��㼼��',
        '�ܴ�Ƶ��': '�ܴ�Ƶ��'
    })

    # ��ʾ�������ݱ��񣨴���ҳ��������
    st.subheader('������ҵ��Ϣ')
    st.dataframe(
        df,
        use_container_width=True,  # ��������Ӧ
        hide_index=True,           # ��������
        column_config={
            "��Ʊ����": st.column_config.NumberColumn(
                "��Ʊ����",
                format="%d",
            ),
            "��ҵ����": st.column_config.TextColumn(
                "��ҵ����",
                width="medium",
            ),
            "���ּ���Ӧ��": st.column_config.NumberColumn(
                "���ּ���Ӧ��",
                format="%d",
            ),
            "�ܴ�Ƶ��": st.column_config.NumberColumn(
                "�ܴ�Ƶ��",
                format="%d",
            )
        },
    )

    # �ָ���
    st.markdown("---")

    # ��Ʊ�����ѯ����
    st.subheader('����Ʊ�����ѯ')

    # ����һ����������û������Ʊ����
    stock_code = st.text_input('�������Ʊ����')

    # ���û������Ʊ����󣬽��в�ѯ
    if stock_code:
        try:
            stock_code = int(stock_code)
            result = df[df['��Ʊ����'] == stock_code]

            if not result.empty:
                st.success(f'�ҵ���Ʊ���� {stock_code} ����Ϣ:')

                # ʹ�ñ�����ʾ��ϸ��Ϣ
                st.dataframe(
                    result,
                    use_container_width=True,
                    hide_index=True,
                )

                # ��ʾ����ͼ������Ӧ�÷ֲ���
                st.subheader('����Ӧ�÷ֲ�')
                tech_data = result.iloc[0][['���ּ���Ӧ��', '�˹����ܼ���', '����������', '�����ݼ���', '�Ƽ��㼼��']]
                st.bar_chart(tech_data)
            else:
                st.warning(f'δ�ҵ���Ʊ���� {stock_code} ��Ӧ����ҵ��Ϣ')

        except ValueError:
            st.error('��������Ч�Ĺ�Ʊ���루������ʽ��')

except FileNotFoundError:
    st.error("�޷��ҵ�ָ���� Excel �ļ��������ļ�·���Ƿ���ȷ��")
except Exception as e:
    st.error(f"��������: {str(e)}")