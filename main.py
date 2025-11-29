import streamlit as st
from utils import apply_lab_style
from units import unit1_basics, unit2_combinational, unit3_sequential, unit4_advanced, unit5_pld_memory
from tutor import SmartTutor

# Page Configuration
st.set_page_config(
    page_title="Virtual Digital Logic Lab",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Apply Custom Styling
apply_lab_style()

# Sidebar Navigation
st.sidebar.title("🔌 Digital Logic Lab")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Select Unit:",
    [
        "Home",
        "Unit 1: Basics",
        "Unit 2: Combinational Circuits",
        "Unit 3: Sequential Circuits",
        "Unit 4: Advanced Logic",
        "Unit 5: PLDs & Memory"
    ]
)

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.caption("v1.0.0 | Virtual Digital Logic Lab")

if st.sidebar.button("🗑️ Reset All Progress", help="Clear all experiment progress and start over"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Main Routing
if menu == "Home":
    st.markdown("""
    <div style='text-align: center; padding: 3rem 0 2rem 0;'>
        <h1 style='font-size: 4rem; background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #ec4899 100%); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                   margin-bottom: 1rem; font-weight: 800; letter-spacing: -0.03em;'>
            Virtual Digital Logic Lab
        </h1>
        <p style='font-size: 1.4rem; color: #94a3b8; margin-bottom: 0.5rem; font-weight: 300;'>
            Master Digital Electronics through Interactive Simulation
        </p>
        <p style='font-size: 1rem; color: #64748b; font-weight: 400;'>
            B.Tech 2nd Year ECE • State-Aware Tutor System • 12 Interactive Experiments
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Global Progress with Stats
    tutor = SmartTutor()
    
    # Count progress from both new (tutor_state) and legacy (tutor_progress)
    total_experiments = 12
    
    # New state tracker (unit_id keys)
    new_state_completions = 0
    experiment_ids = ["u1_ex1", "u1_ex2", "u2_ex3", "u2_ex4", "u2_ex5", 
                      "u3_ex6", "u3_ex7", "u3_ex8", "u4_ex9", "u4_ex10", 
                      "u5_ex11", "u5_ex12"]
    
    for exp_id in experiment_ids:
        if exp_id in st.session_state.tutor_state:
            # Get the expected total steps for each experiment
            # If current_step >= total_steps, it's complete
            # For simplicity, we'll assume if the key exists and step > 0, there's progress
            pass
    
    # Legacy progress tracker
    completed_count = len([k for k, v in st.session_state.tutor_progress.items() if v])
    progress = completed_count / total_experiments
    
    st.markdown("---")
    
    # Progress Section with Enhanced Visuals
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%); 
                padding: 2rem; border-radius: 16px; border: 1px solid rgba(96, 165, 250, 0.2);
                margin-bottom: 2rem;'>
        <h2 style='margin-top: 0; color: #60a5fa; font-size: 2rem;'>🚀 Your Learning Journey</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    
    with col_stat1:
        st.markdown(f"""
        <div class='lab-box' style='text-align: center; background: rgba(34, 197, 94, 0.15); border: 1px solid rgba(34, 197, 94, 0.3);'>
            <p style='color: #86efac; font-size: 0.9rem; margin: 0;'>COMPLETED</p>
            <p style='font-size: 2.5rem; font-weight: 700; color: #22c55e; margin: 0.5rem 0;'>{completed_count}</p>
            <p style='color: #86efac; font-size: 0.85rem; margin: 0;'>experiments</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat2:
        remaining = total_experiments - completed_count
        st.markdown(f"""
        <div class='lab-box' style='text-align: center; background: rgba(251, 191, 36, 0.15); border: 1px solid rgba(251, 191, 36, 0.3);'>
            <p style='color: #fcd34d; font-size: 0.9rem; margin: 0;'>REMAINING</p>
            <p style='font-size: 2.5rem; font-weight: 700; color: #f59e0b; margin: 0.5rem 0;'>{remaining}</p>
            <p style='color: #fcd34d; font-size: 0.85rem; margin: 0;'>experiments</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat3:
        st.markdown(f"""
        <div class='lab-box' style='text-align: center; background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.3);'>
            <p style='color: #c4b5fd; font-size: 0.9rem; margin: 0;'>PROGRESS</p>
            <p style='font-size: 2.5rem; font-weight: 700; color: #a78bfa; margin: 0.5rem 0;'>{int(progress*100)}%</p>
            <p style='color: #c4b5fd; font-size: 0.85rem; margin: 0;'>complete</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat4:
        st.markdown(f"""
        <div class='lab-box' style='text-align: center; background: rgba(236, 72, 153, 0.15); border: 1px solid rgba(236, 72, 153, 0.3);'>
            <p style='color: #fbcfe8; font-size: 0.9rem; margin: 0;'>TOTAL UNITS</p>
            <p style='font-size: 2.5rem; font-weight: 700; color: #ec4899; margin: 0.5rem 0;'>5</p>
            <p style='color: #fbcfe8; font-size: 0.85rem; margin: 0;'>modules</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br/>", unsafe_allow_html=True)
    
    # Enhanced Progress Bar
    st.markdown(f"""
    <div style='margin: 2rem 0;'>
        <div style='display: flex; justify-content: space-between; margin-bottom: 0.5rem;'>
            <span style='color: #93c5fd; font-weight: 600; font-size: 1.1rem;'>Overall Progress</span>
            <span style='color: #60a5fa; font-weight: 700; font-size: 1.1rem;'>{completed_count} / {total_experiments} Experiments</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.progress(progress)
    
    st.markdown("---")

    # Unit Cards
    st.markdown("""
    <h2 style='color: #60a5fa; margin-bottom: 2rem;'>📚 Course Curriculum</h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='lab-box' style='background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(37, 99, 235, 0.15) 100%); 
                    border: 1px solid rgba(59, 130, 246, 0.3); transition: all 0.3s;'>
            <h3 style='color: #60a5fa; margin-top: 0;'>🔌 Unit 1: Basics</h3>
            <p style='color: #94a3b8; font-size: 0.95rem; line-height: 1.6;'>Logic Gates, Boolean Algebra, K-Map Minimization</p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(59, 130, 246, 0.2);'>
                <span style='color: #60a5fa; font-size: 0.85rem; font-weight: 600;'>2 Experiments</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='lab-box' style='background: linear-gradient(135deg, rgba(139, 92, 246, 0.15) 0%, rgba(124, 58, 237, 0.15) 100%); 
                    border: 1px solid rgba(139, 92, 246, 0.3); transition: all 0.3s;'>
            <h3 style='color: #a78bfa; margin-top: 0;'>⚙️ Unit 2: Combinational</h3>
            <p style='color: #94a3b8; font-size: 0.95rem; line-height: 1.6;'>Adders, Mux/Demux, Code Converters</p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(139, 92, 246, 0.2);'>
                <span style='color: #a78bfa; font-size: 0.85rem; font-weight: 600;'>3 Experiments</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class='lab-box' style='background: linear-gradient(135deg, rgba(236, 72, 153, 0.15) 0%, rgba(219, 39, 119, 0.15) 100%); 
                    border: 1px solid rgba(236, 72, 153, 0.3); transition: all 0.3s;'>
            <h3 style='color: #ec4899; margin-top: 0;'>🔄 Unit 3: Sequential</h3>
            <p style='color: #94a3b8; font-size: 0.95rem; line-height: 1.6;'>Flip-Flops, Shift Registers, Counters</p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(236, 72, 153, 0.2);'>
                <span style='color: #ec4899; font-size: 0.85rem; font-weight: 600;'>3 Experiments</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br/>", unsafe_allow_html=True)
    
    col4, col5 = st.columns([1, 1])
    with col4:
         st.markdown("""
        <div class='lab-box' style='background: linear-gradient(135deg, rgba(34, 197, 94, 0.15) 0%, rgba(22, 163, 74, 0.15) 100%); 
                    border: 1px solid rgba(34, 197, 94, 0.3); transition: all 0.3s;'>
            <h3 style='color: #22c55e; margin-top: 0;'>🧩 Unit 4: Advanced</h3>
            <p style='color: #94a3b8; font-size: 0.95rem; line-height: 1.6;'>FSM Design, State Machines, Real-world Controllers</p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(34, 197, 94, 0.2);'>
                <span style='color: #22c55e; font-size: 0.85rem; font-weight: 600;'>2 Experiments</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
         
    with col5:
         st.markdown("""
        <div class='lab-box' style='background: linear-gradient(135deg, rgba(251, 191, 36, 0.15) 0%, rgba(245, 158, 11, 0.15) 100%); 
                    border: 1px solid rgba(251, 191, 36, 0.3); transition: all 0.3s;'>
            <h3 style='color: #f59e0b; margin-top: 0;'>💾 Unit 5: PLDs & Memory</h3>
            <p style='color: #94a3b8; font-size: 0.95rem; line-height: 1.6;'>PLA/PAL, FPGA Architecture, Programmable Logic</p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(251, 191, 36, 0.2);'>
                <span style='color: #f59e0b; font-size: 0.85rem; font-weight: 600;'>2 Experiments</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Getting started
    st.header("🚀 Getting Started")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### How to Use This Lab
        
        1. **Select a Unit** from the sidebar navigation
        2. **Choose an Experiment** using the tabs
        3. **Read the Theory** to understand the concepts
        4. **Follow the Smart Tutor** in the right panel for step-by-step guidance
        5. **Interact with Controls** to modify circuit inputs
        6. **Observe Results** in real-time visualizations
        7. **Complete All Tasks** - the tutor validates each step automatically
        
        #### 🎓 Smart Tutor Features
        - **State-Aware Validation**: Checks your circuit configuration in real-time
        - **Contextual Hints**: Get help when you need it
        - **Progress Tracking**: See exactly where you are in each experiment
        - **Automatic Verification**: No manual checking - the system knows when you're right!
        """)
    
    with col2:
        st.markdown("""
        <div class='lab-box' style='background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%); 
                    border: 1px solid rgba(96, 165, 250, 0.3); padding: 2rem;'>
            <h3 style='text-align: center; margin-top: 0; color: #60a5fa;'>🎯 Quick Start</h3>
            <p style='text-align: center; color: #93c5fd; font-size: 1.2rem; margin-bottom: 1.5rem; line-height: 1.6;'>
                Begin your journey with<br/><strong style='font-size: 1.4rem; color: #60a5fa;'>Unit 1: Basics</strong><br/>
                <span style='font-size: 0.95rem; color: #94a3b8;'>from the sidebar</span>
            </p>
            <div style='text-align: center; margin-top: 1.5rem;'>
                <span style='font-size: 3rem;'>👈</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br/>", unsafe_allow_html=True)

elif menu == "Unit 1: Basics":
    unit1_basics.render()

elif menu == "Unit 2: Combinational Circuits":
    unit2_combinational.render()

elif menu == "Unit 3: Sequential Circuits":
    unit3_sequential.render()

elif menu == "Unit 4: Advanced Logic":
    unit4_advanced.render()

elif menu == "Unit 5: PLDs & Memory":
    unit5_pld_memory.render()
