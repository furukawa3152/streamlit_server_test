import streamlit as st
import os

def load_content(file_path):
    if not os.path.exists(file_path):
        # ファイルが存在しない場合は初期内容を作成
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("# 掲示板\nここにメッセージを追加してください。")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def save_content(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
file_path = "board.txt"

# Streamlitアプリケーション
def main():
    st.title("部署内掲示板")

    # 編集モードの状態を保持するセッションステート変数
    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = False
    # テキストファイルから内容を読み込む
    content = load_content(file_path)

    if st.session_state.edit_mode:
        # 編集画面
        new_content = st.text_area("編集内容を入力してください", content, height=300)
        if st.button("保存"):
            save_content(file_path, new_content)
            st.session_state.edit_mode = False
            st.rerun()
        if st.button("キャンセル"):
            st.session_state.edit_mode = False
            st.rerun()
    else:
        # 表示画面
        st.markdown(content, unsafe_allow_html=True)# テキスト入力フィールド
        user_input = st.text_input("編集にはパスワードを入れてね。")
        # 入力された文字列が指定された文字列と一致するかどうかをチェック
        if user_input == "pass":
            # 一致する場合のみボタンを表示
            if st.button("編集"):
                st.session_state.edit_mode = True
                st.rerun()

    # Markdownの一般的な説明文章
    st.markdown("""
    ## Markdownの書き方
    - **見出し**: `# 見出し1`、`## 見出し2`、`### 見出し3`
    - **強調**: `**太字**` または `__太字__`、`*斜体*` または `_斜体_`
    - **リスト**: `- 箇条書き` または `1. 番号付きリスト`
    - **リンク**: `[リンクテキスト](URL)`
    - **画像**: `![代替テキスト](画像URL)`
    - **改行**: `改行＋半角スペース×２`
    """)


if __name__ == "__main__":
    main()

    #起動コマンド
    #$ streamlit run main.py --server.port=8501 --server.enableStaticServing=true

