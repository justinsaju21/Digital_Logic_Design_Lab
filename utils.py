import streamlit as st

def apply_lab_style():
    """Applies a professional, modern dark theme with engineering aesthetics."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
        
        /* Main Background with subtle gradient */
        .stApp {
            background: linear-gradient(135deg, #0a0e1a 0%, #1a1f35 100%);
            color: #e4e7eb;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Better text rendering */
        * {
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        /* Main content padding */
        .main .block-container {
            padding-top: 3rem;
            padding-bottom: 3rem;
            padding-left: 3rem;
            padding-right: 3rem;
            max-width: 1400px;
        }
        
        /* Sidebar with glassmorphism effect */
        [data-testid="stSidebar"] {
            background: rgba(20, 25, 40, 0.95);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(100, 200, 255, 0.1);
            box-shadow: 4px 0 24px rgba(0, 0, 0, 0.3);
        }
        
        [data-testid="stSidebar"] > div:first-child {
            padding-top: 2rem;
            padding-left: 1.5rem;
            padding-right: 1.5rem;
        }
        
        /* Logo styling */
        [data-testid="stSidebar"] img {
            border-radius: 12px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 12px rgba(96, 165, 250, 0.2);
        }
        
        /* Headers with gradient text and better spacing */
        h1 {
            background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 700;
            font-size: 2.75rem !important;
            margin-bottom: 2rem !important;
            margin-top: 0 !important;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }
        
        h2 {
            color: #60a5fa;
            font-weight: 600;
            font-size: 1.875rem !important;
            margin-top: 2.5rem !important;
            margin-bottom: 1.25rem !important;
            border-bottom: 2px solid rgba(96, 165, 250, 0.2);
            padding-bottom: 0.75rem;
            letter-spacing: -0.01em;
        }
        
        h3 {
            color: #93c5fd;
            font-weight: 600;
            font-size: 1.375rem !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
            letter-spacing: -0.01em;
        }
        
        h4 {
            color: #bfdbfe;
            font-weight: 500;
            font-size: 1.125rem !important;
            margin-top: 1.5rem !important;
            margin-bottom: 0.75rem !important;
        }
        
        /* Paragraph spacing */
        p {
            line-height: 1.7;
            margin-bottom: 1rem;
        }
        
        /* Buttons with modern styling */
        .stButton>button {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            padding: 0.875rem 2rem;
            font-size: 1rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.5rem;
        }
        
        .stButton>button:hover {
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
            transform: translateY(-2px);
        }
        
        .stButton>button:active {
            transform: translateY(0);
        }
        
        /* Radio buttons with better spacing */
        .stRadio {
            margin-bottom: 1.5rem;
        }
        
        .stRadio > label {
            color: #93c5fd;
            font-weight: 500;
            font-size: 0.95rem;
            margin-bottom: 0.75rem;
            display: block;
        }
        
        .stRadio > div {
            background: rgba(30, 41, 59, 0.5);
            padding: 1rem;
            border-radius: 10px;
            border: 1px solid rgba(100, 200, 255, 0.1);
            gap: 1rem;
        }
        
        .stRadio > div > label {
            padding: 0.5rem 1rem;
            border-radius: 6px;
            transition: all 0.2s;
        }
        
        .stRadio > div > label:hover {
            background: rgba(59, 130, 246, 0.1);
        }
        
        /* Select boxes with better styling */
        .stSelectbox {
            margin-bottom: 1.5rem;
        }
        
        .stSelectbox > label {
            color: #93c5fd;
            font-weight: 500;
            font-size: 0.95rem;
            margin-bottom: 0.75rem;
            display: block;
        }
        
        .stSelectbox > div > div {
            background-color: rgba(30, 41, 59, 0.8);
            border: 1px solid rgba(100, 200, 255, 0.2);
            border-radius: 10px;
            color: #e4e7eb;
        }

        /* Fix for Selectbox Text Visibility */
        div[data-baseweb="select"] > div {
            color: #e4e7eb !important;
            background-color: rgba(30, 41, 59, 0.8) !important;
        }
        
        div[data-baseweb="select"] span {
            color: #e4e7eb !important;
        }
        
        /* Fix for Dropdown Menu Visibility */
        div[data-baseweb="popover"] {
            background-color: #1e293b !important;
            border: 1px solid rgba(100, 200, 255, 0.2);
        }
        
        div[data-baseweb="menu"] {
            background-color: #1e293b !important;
        }
        
        div[data-baseweb="menu"] div {
            color: #e4e7eb !important;
        }
        
        div[data-baseweb="menu"] li:hover {
            background-color: rgba(59, 130, 246, 0.2) !important;
        }
        
        /* Number inputs */
        .stNumberInput {
            margin-bottom: 1.5rem;
        }
        
        .stNumberInput > label {
            color: #93c5fd;
            font-weight: 500;
            font-size: 0.95rem;
            margin-bottom: 0.75rem;
            display: block;
        }
        
        .stNumberInput input {
            background-color: rgba(30, 41, 59, 0.8);
            border: 1px solid rgba(100, 200, 255, 0.2);
            border-radius: 10px;
            color: #e4e7eb;
            font-family: 'JetBrains Mono', monospace;
            padding: 0.625rem 1rem;
        }
        
        /* Slider styling */
        .stSlider {
            margin-bottom: 1.5rem;
            padding-top: 0.5rem;
        }
        
        .stSlider > label {
            color: #93c5fd;
            font-weight: 500;
            margin-bottom: 1rem;
        }
        
        /* Tabs with modern design */
        .stTabs {
            margin-top: 2rem;
            margin-bottom: 2rem;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background-color: transparent;
            border-bottom: 2px solid rgba(100, 200, 255, 0.1);
            padding-bottom: 0;
        }

        .stTabs [data-baseweb="tab"] {
            height: 56px;
            background: rgba(30, 41, 59, 0.5);
            border-radius: 10px 10px 0 0;
            padding: 12px 28px;
            color: #94a3b8;
            font-weight: 500;
            font-size: 1rem;
            border: 1px solid rgba(100, 200, 255, 0.1);
            border-bottom: none;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(59, 130, 246, 0.1);
            color: #60a5fa;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(37, 99, 235, 0.2) 100%);
            color: #60a5fa;
            border-color: rgba(96, 165, 250, 0.3);
            box-shadow: 0 -2px 12px rgba(59, 130, 246, 0.2);
        }
        
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 2rem;
        }
        
        /* Metrics with better styling */
        [data-testid="stMetricValue"] {
            font-size: 2.25rem;
            color: #60a5fa;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
        }
        
        [data-testid="stMetricLabel"] {
            color: #93c5fd;
            font-weight: 500;
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        
        [data-testid="stMetric"] {
            background: rgba(30, 41, 59, 0.5);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid rgba(100, 200, 255, 0.1);
        }
        
        /* Info/Success/Warning boxes */
        .stAlert {
            background: rgba(30, 41, 59, 0.8);
            border-radius: 12px;
            border-left: 4px solid #60a5fa;
            padding: 1.25rem 1.75rem;
            backdrop-filter: blur(10px);
            margin: 1.5rem 0;
        }
        
        /* Expander with better styling */
        .streamlit-expanderHeader {
            background: rgba(30, 41, 59, 0.6);
            border-radius: 10px;
            border: 1px solid rgba(100, 200, 255, 0.1);
            color: #93c5fd;
            font-weight: 500;
            padding: 1rem 1.25rem;
            margin-bottom: 0.5rem;
        }
        
        .streamlit-expanderHeader:hover {
            background: rgba(59, 130, 246, 0.1);
            border-color: rgba(96, 165, 250, 0.3);
        }
        
        .streamlit-expanderContent {
            border: 1px solid rgba(100, 200, 255, 0.1);
            border-top: none;
            border-radius: 0 0 10px 10px;
            padding: 1.5rem;
            background: rgba(15, 23, 42, 0.5);
        }
        
        /* Dataframe styling */
        .stDataFrame {
            margin: 1.5rem 0;
        }
        
        [data-testid="stDataFrame"] {
            background: rgba(30, 41, 59, 0.5);
            border-radius: 10px;
            border: 1px solid rgba(100, 200, 255, 0.1);
        }
        
        /* Sidebar elements */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: #60a5fa;
        }
        
        [data-testid="stSidebar"] .stRadio > div {
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid rgba(96, 165, 250, 0.2);
        }
        
        /* Progress bar */
        .stProgress > div > div > div {
            background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 50%, #ec4899 100%);
            border-radius: 10px;
        }
        
        .stProgress > div > div {
            background: rgba(30, 41, 59, 0.5);
            border-radius: 10px;
        }
        
        /* Checkbox */
        .stCheckbox {
            color: #93c5fd;
            margin-bottom: 0.75rem;
        }
        
        .stCheckbox > label {
            padding: 0.5rem 0;
        }
        
        /* Custom classes */
        .lab-box {
            background: rgba(30, 41, 59, 0.6);
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid rgba(100, 200, 255, 0.15);
            margin-bottom: 2rem;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }
        
        .lab-box:hover {
            border-color: rgba(96, 165, 250, 0.3);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        }
        
        .circuit-container {
            background: rgba(15, 23, 42, 0.8);
            padding: 2.5rem;
            border-radius: 16px;
            border: 1px solid rgba(100, 200, 255, 0.2);
            text-align: center;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
            margin: 1.5rem 0;
        }
        
        /* Horizontal rule */
        hr {
            border: none;
            border-top: 1px solid rgba(100, 200, 255, 0.1);
            margin: 2rem 0;
        }
        
        /* Code blocks */
        code {
            background: rgba(30, 41, 59, 0.8);
            padding: 0.25rem 0.5rem;
            border-radius: 6px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9em;
            color: #f472b6;
        }
        
        pre {
            background: rgba(15, 23, 42, 0.8);
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid rgba(100, 200, 255, 0.1);
            overflow-x: auto;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 12px;
            height: 12px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(15, 23, 42, 0.5);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: rgba(96, 165, 250, 0.3);
            border-radius: 10px;
            border: 2px solid rgba(15, 23, 42, 0.5);
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(96, 165, 250, 0.5);
        }
        
        /* Column spacing */
        [data-testid="column"] {
            padding: 0 1rem;
        }
        
        [data-testid="column"]:first-child {
            padding-left: 0;
        }
        
        [data-testid="column"]:last-child {
            padding-right: 0;
        }
        
        /* Responsive Design for Mobile/Tablets */
        @media (max-width: 768px) {
            .main .block-container {
                padding: 2rem 1rem;
            }
            
            h1 {
                font-size: 2rem !important;
            }
            
            h2 {
                font-size: 1.5rem !important;
                margin-top: 1.5rem !important;
            }
            
            h3 {
                font-size: 1.2rem !important;
            }
            
            .lab-box {
                padding: 1.25rem;
            }
            
            [data-testid="stMetricValue"] {
                font-size: 1.75rem;
            }
            
            .circuit-container {
                padding: 1rem;
            }
            
            /* Stack columns on mobile */
            [data-testid="column"] {
                width: 100% !important;
                margin-bottom: 1rem;
            }
        }
        </style>
    """, unsafe_allow_html=True)

def show_theory(title, content):
    """Displays a theory section in an expander."""
    with st.expander(f"📖 Theory: {title}", expanded=False):
        st.markdown(content)

def show_success_message(message):
    st.success(f"✅ {message}")

def show_info_message(message):
    st.info(f"ℹ️ {message}")

def render_experiment_layout(title, theory_content, simulation_func, tutor=None, steps=None, current_step_index=0, tutor_unit_id=None, tutor_steps_config=None, tutor_context=None):
    """
    Standard layout for all experiments with Tutor on the right.
    Supports both legacy (steps list) and advanced (tutor_steps_config) modes.
    """
    st.header(f"{title}")
    
    # Create two columns: Main Content (Left) and Tutor (Right)
    col_main, col_tutor = st.columns([3, 1])
    
    with col_main:
        tab_sim, tab_theory = st.tabs(["🔬 Simulation", "📖 Theory"])
        
        with tab_sim:
            simulation_func()
            
        with tab_theory:
            st.markdown(theory_content)
            
    with col_tutor:
        if tutor:
            if tutor_steps_config and tutor_unit_id:
                # New Advanced Tutor
                tutor.guide(tutor_unit_id, tutor_steps_config, tutor_context)
            elif steps:
                # Legacy Tutor
                tutor.render_right_panel(steps, current_step_index)
            else:
                st.info("Tutor is ready.")

import base64

def render_circuit_image(img_buf):
    """
    Renders a matplotlib image buffer inside a styled HTML container.
    """
    if img_buf:
        b64 = base64.b64encode(img_buf.getvalue()).decode()
        html = f"""
            <div class='circuit-container'>
                <img src='data:image/png;base64,{b64}' style='max-width: 100%; border-radius: 8px;'>
            </div>
        """
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("No circuit image generated.")
