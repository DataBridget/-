import pandas as pd
import streamlit as st

# 设置页面配置（宽屏模式）
st.set_page_config(layout="wide")

# 标题和说明
st.title('股票代码信息查询应用')
st.markdown("输入股票代码查询企业信息，或浏览下方完整表格。")

try:
    # 读取 Excel 文件
    excel_file = pd.ExcelFile('C:/Users/93137/Desktop/test/股票代码.xlsx')
    
    # 获取指定工作表中的数据
    df = excel_file.parse('Sheet1')
    
    # 重命名列名，使表格更易读
    df = df.rename(columns={
        'Unnamed: 0': '股票代码',
        '企业名称': '企业名称',
        '数字技术应用': '数字技术应用',
        '人工智能技术': '人工智能技术',
        '区块链技术': '区块链技术',
        '大数据技术': '大数据技术',
        '云计算技术': '云计算技术',
        '总词频数': '总词频数'
    })
    
    # 显示完整数据表格（带分页和搜索）
    st.subheader('所有企业信息')
    st.dataframe(
        df,
        use_container_width=True,  # 宽度自适应
        hide_index=True,           # 隐藏索引
        column_config={
            "股票代码": st.column_config.NumberColumn(
                "股票代码",
                format="%d",
            ),
            "企业名称": st.column_config.TextColumn(
                "企业名称",
                width="medium",
            ),
            "数字技术应用": st.column_config.NumberColumn(
                "数字技术应用",
                format="%d",
            ),
            "总词频数": st.column_config.NumberColumn(
                "总词频数",
                format="%d",
            )
        },
    )
    
    # 分隔线
    st.markdown("---")
    
    # 股票代码查询功能
    st.subheader('按股票代码查询')
    
    # 创建一个输入框，让用户输入股票代码
    stock_code = st.text_input('请输入股票代码')
    
    # 当用户输入股票代码后，进行查询
    if stock_code:
        try:
            stock_code = int(stock_code)
            result = df[df['股票代码'] == stock_code]
            
            if not result.empty:
                st.success(f'找到股票代码 {stock_code} 的信息:')
                
                # 使用表格显示详细信息
                st.dataframe(
                    result,
                    use_container_width=True,
                    hide_index=True,
                )
                
                # 显示条形图（技术应用分布）
                st.subheader('技术应用分布')
                tech_data = result.iloc[0][['数字技术应用', '人工智能技术', '区块链技术', '大数据技术', '云计算技术']]
                st.bar_chart(tech_data)
            else:
                st.warning(f'未找到股票代码 {stock_code} 对应的企业信息')
                
        except ValueError:
            st.error('请输入有效的股票代码（整数形式）')

except FileNotFoundError:
    st.error("无法找到指定的 Excel 文件，请检查文件路径是否正确。")
except Exception as e:
    st.error(f"发生错误: {str(e)}")