import streamlit as st

# -------------------- Page Config -------------------- #
st.set_page_config(
    page_title="Instagram ID Duplicate Cleaner",
    page_icon="📸",
    layout="wide"
)

# -------------------- Custom CSS -------------------- #
st.markdown("""
<style>
    .main-container {
        max-width: 900px;
        margin: auto;
    }
    .gradient-text {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #ff4b2b, #ff416c, #7f00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .subtext {
        text-align: center;
        color: #888;
        margin-bottom: 30px;
    }
    .section-divider {
        margin: 30px 0;
        border-top: 1px solid #e6e6e6;
    }
    .stats-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #eee;
        color: #333;
    }
    .stats-box h3 {
        margin: 0;
        color: #ff416c;
    }
    /* Style the text area labels */
    .stTextArea label p {
        font-size: 1.1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- Header -------------------- #
st.markdown('<div class="gradient-text">Instagram ID Duplicate Cleaner</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Instantly remove duplicates and normalize your lists</div>', unsafe_allow_html=True)

# -------------------- Main UI -------------------- #
# Using columns to center the content visually
left_co, cent_co, last_co = st.columns([1, 8, 1])

with cent_co:
    st.markdown("### 📥 Paste Instagram IDs")
    input_text = st.text_area(
        "Enter one Instagram ID per line:",
        height=250,
        placeholder="user1\nuser2\nuser1 (will be removed)",
        key="input_area"
    )

    clean_clicked = st.button("🚀 Clean IDs", use_container_width=True)

    if clean_clicked and input_text.strip():
        # Processing logic
        lines = input_text.splitlines()
        cleaned = []
        seen = set()
        total_count = 0

        for line in lines:
            original = line.strip()
            if original:
                total_count += 1
                lowered = original.lower()
                if lowered not in seen:
                    cleaned.append(original)
                    seen.add(lowered)

        unique_count = len(cleaned)
        duplicate_count = total_count - unique_count
        cleaned_text = "\n".join(cleaned)

        # -------------------- Stats Section -------------------- #
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown("### 📊 Statistics")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="stats-box"><h3>{total_count}</h3><p>Total Entered</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="stats-box"><h3>{unique_count}</h3><p>Unique Remaining</p></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="stats-box"><h3>{duplicate_count}</h3><p>Duplicates Removed</p></div>', unsafe_allow_html=True)

        # -------------------- Output Section -------------------- #
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown("### ✅ Cleaned Instagram IDs")
        
        output_area = st.text_area(
            "Copy your cleaned list below:",
            value=cleaned_text,
            height=250,
            key="output_area"
        )

        # Download Button
        st.download_button(
            label="⬇ Download as .TXT",
            data=cleaned_text,
            file_name="cleaned_ids.txt",
            mime="text/plain",
            use_container_width=True
        )
        
        st.success(f"Successfully cleaned {duplicate_count} duplicates!")

    elif clean_clicked and not input_text.strip():
        st.warning("Please paste some IDs first.")