import streamlit as st
import pandas as pd
from utils import render_experiment_layout, render_circuit_image
from tutor import SmartTutor
from circuits import draw_generic_block

def render():
    st.title("Unit 5: PLDs & Memory")
    
    tutor = SmartTutor()
    
    tab1, tab2 = st.tabs(["Ex 11: PLA/PAL", "Ex 12: FPGA"])
    
    with tab1:
        run_experiment_11(tutor)
    with tab2:
        run_experiment_12(tutor)

def run_experiment_11(tutor):
    # Advanced Tutor Configuration for PLA
    tutor_config = [
        {
            "title": "Understand PLA Architecture",
            "instruction": "A PLA (Programmable Logic Array) has a programmable AND plane feeding a programmable OR plane. We will implement **F = A + B**.",
            "criteria": lambda c: True,
            "success_msg": "✓ Architecture understood. Let's program the logic!"
        },
        {
            "title": "Configure Product Term 1 (Select A)",
            "instruction": "In the **AND Plane**, for **Product Term 1**, check **Input A** and uncheck Input B. This creates the term 'A'.",
            "criteria": lambda c: c.get('p1_a') and not c.get('p1_b'),
            "success_msg": "✓ Product Term 1 set to 'A'."
        },
        {
            "title": "Configure Product Term 2 (Select B)",
            "instruction": "For **Product Term 2**, uncheck Input A and check **Input B**. This creates the term 'B'.",
            "criteria": lambda c: not c.get('p2_a') and c.get('p2_b'),
            "success_msg": "✓ Product Term 2 set to 'B'."
        },
        {
            "title": "Configure OR Plane (Sum Terms)",
            "instruction": "In the **OR Plane**, check both **Include Term 1** and **Include Term 2**. This creates F = Term1 OR Term2.",
            "criteria": lambda c: c.get('or_p1') and c.get('or_p2'),
            "success_msg": "✓ OR Plane configured. Logic is now F = A + B."
        },
        {
            "title": "Test Case 1: 0 + 0",
            "instruction": "Set **Input A = 0** and **Input B = 0**. Verify Output is 0.",
            "criteria": lambda c: c.get('in_a') == 0 and c.get('in_b') == 0 and c.get('out') == 0,
            "success_msg": "✓ 0 OR 0 = 0 verified."
        },
        {
            "title": "Test Case 2: 0 + 1",
            "instruction": "Set **Input A = 0** and **Input B = 1**. Verify Output is 1.",
            "criteria": lambda c: c.get('in_a') == 0 and c.get('in_b') == 1 and c.get('out') == 1,
            "success_msg": "✓ 0 OR 1 = 1 verified."
        },
        {
            "title": "Test Case 3: 1 + 0",
            "instruction": "Set **Input A = 1** and **Input B = 0**. Verify Output is 1.",
            "criteria": lambda c: c.get('in_a') == 1 and c.get('in_b') == 0 and c.get('out') == 1,
            "success_msg": "✓ 1 OR 0 = 1 verified."
        },
        {
            "title": "Test Case 4: 1 + 1",
            "instruction": "Set **Input A = 1** and **Input B = 1**. Verify Output is 1.",
            "criteria": lambda c: c.get('in_a') == 1 and c.get('in_b') == 1 and c.get('out') == 1,
            "success_msg": "✓ 1 OR 1 = 1 verified. Logic F = A + B is working perfectly!",
        },
        {
            "title": "Modify Logic: Implement AND (A * B)",
            "instruction": "Now change the logic to AND. In the **OR Plane**, uncheck Term 1 and Term 2. Wait... AND is a single product term! Go to **AND Plane**, Term 1, check BOTH A and B.",
            "criteria": lambda c: c.get('p1_a') and c.get('p1_b'),
            "success_msg": "✓ Term 1 is now 'A AND B'."
        },
        {
            "title": "Finalize AND Logic",
            "instruction": "In **OR Plane**, check only **Include Term 1**. Uncheck Term 2.",
            "criteria": lambda c: c.get('or_p1') and not c.get('or_p2'),
            "success_msg": "🎉 EXPERIMENT COMPLETE! You've reprogrammed the PLA from OR to AND."
        }
    ]

    # PLA State: 2 Product Terms, 2 Inputs (A, B), 1 Output
    if 'pla_and' not in st.session_state: st.session_state.pla_and = [[False, False], [False, False]]
    if 'pla_or' not in st.session_state: st.session_state.pla_or = [False, False]
    
    def simulation():
        st.markdown("""
        <p style='color: #94a3b8; font-size: 1.05rem; margin-bottom: 2rem;'>
            Program a simple **PLA (Programmable Logic Array)**. 
            Connect inputs to AND gates (Product Terms), then connect those terms to an OR gate (Sum).
        </p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### 🔌 AND Plane Configuration")
            st.caption("Select inputs for each Product Term (AND Gate)")
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Product Term 1**")
                st.session_state.pla_and[0][0] = st.checkbox("Input A", value=st.session_state.pla_and[0][0], key="p1_a")
                st.session_state.pla_and[0][1] = st.checkbox("Input B", value=st.session_state.pla_and[0][1], key="p1_b")
            with c2:
                st.markdown("**Product Term 2**")
                st.session_state.pla_and[1][0] = st.checkbox("Input A", value=st.session_state.pla_and[1][0], key="p2_a")
                st.session_state.pla_and[1][1] = st.checkbox("Input B", value=st.session_state.pla_and[1][1], key="p2_b")
                
            st.markdown("### 🔗 OR Plane Configuration")
            st.caption("Select Product Terms for the Output (OR Gate)")
            
            st.session_state.pla_or[0] = st.checkbox("Include Term 1", value=st.session_state.pla_or[0], key="or_p1")
            st.session_state.pla_or[1] = st.checkbox("Include Term 2", value=st.session_state.pla_or[1], key="or_p2")
            
        with col2:
            st.markdown("### 🧪 Test Bench")
            in_a = st.radio("Input A", [0, 1], horizontal=True, key="pla_in_a")
            in_b = st.radio("Input B", [0, 1], horizontal=True, key="pla_in_b")
            
            # Logic Calculation
            # Term 1
            t1 = 1
            if st.session_state.pla_and[0][0]: t1 &= in_a
            if st.session_state.pla_and[0][1]: t1 &= in_b
            if not st.session_state.pla_and[0][0] and not st.session_state.pla_and[0][1]: t1 = 0 # Unused term is 0
            
            # Term 2
            t2 = 1
            if st.session_state.pla_and[1][0]: t2 &= in_a
            if st.session_state.pla_and[1][1]: t2 &= in_b
            if not st.session_state.pla_and[1][0] and not st.session_state.pla_and[1][1]: t2 = 0
            
            # Output
            out = 0
            if st.session_state.pla_or[0]: out |= t1
            if st.session_state.pla_or[1]: out |= t2
            
            st.markdown("---")
            st.metric("Output F", out)
            
            if out == 1:
                st.markdown("💡 **LED ON**")
            else:
                st.markdown("⚫ **LED OFF**")

        return {
            "p1_a": st.session_state.pla_and[0][0],
            "p1_b": st.session_state.pla_and[0][1],
            "p2_a": st.session_state.pla_and[1][0],
            "p2_b": st.session_state.pla_and[1][1],
            "or_p1": st.session_state.pla_or[0],
            "or_p2": st.session_state.pla_or[1],
            "in_a": in_a,
            "in_b": in_b,
            "out": out
        }

    theory = """
    ### Programmable Logic Devices (PLDs)
    
    **Concept**: Instead of wiring individual gates, PLDs contain a massive array of gates that can be "programmed" to create any logic function.
    
    **Architectures:**
    1.  **PLA (Programmable Logic Array)**:
        -   **Programmable AND Plane** + **Programmable OR Plane**.
        -   Most flexible but slower and more expensive.
        -   Can implement any Sum-of-Products (SOP) expression.
        
    2.  **PAL (Programmable Array Logic)**:
        -   **Programmable AND Plane** + **Fixed OR Plane**.
        -   Faster and cheaper than PLA, but less flexible.
        -   Industry standard for simple logic glue.
        
    3.  **CPLD (Complex PLD)**:
        -   Multiple PAL-like blocks connected by a programmable interconnect.
        -   Non-volatile (keeps configuration when power is off).
        
    **Why use PLDs?**
    -   **Reconfigurability**: Change logic without soldering.
    -   **Integration**: Replace dozens of 7400-series chips with one PLD.
    -   **Speed**: Faster than discrete gate wiring.
    """
    
    if 'u5_ex11_ctx' not in st.session_state: st.session_state.u5_ex11_ctx = {}
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u5_ex11_ctx = ctx
        return ctx

    render_experiment_layout("Experiment 11: PLA/PAL Designer", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u5_ex11", tutor_steps_config=tutor_config, tutor_context=st.session_state.u5_ex11_ctx)

def run_experiment_12(tutor):
    # Advanced Tutor Configuration for FPGA
    tutor_config = [
        {
            "title": "Understanding LUTs",
            "instruction": "A Look-Up Table (LUT) is just a small memory. To implement logic, we store the Truth Table outputs in this memory. We will build an **XOR** gate.",
            "criteria": lambda c: True,
            "success_msg": "✓ LUT concept understood."
        },
        {
            "title": "Program Row 0 (0,0)",
            "instruction": "For Input **0 0**, we want 0 XOR 0 = 0. Set the output for Row 00 to **0**.",
            "criteria": lambda c: c.get('lut', [])[0] == 0,
            "success_msg": "✓ Row 0 programmed."
        },
        {
            "title": "Program Row 1 (0,1)",
            "instruction": "For Input **0 1**, we want 0 XOR 1 = 1. Set the output for Row 01 to **1**.",
            "criteria": lambda c: c.get('lut', [])[1] == 1,
            "success_msg": "✓ Row 1 programmed."
        },
        {
            "title": "Program Row 2 (1,0)",
            "instruction": "For Input **1 0**, we want 1 XOR 0 = 1. Set the output for Row 10 to **1**.",
            "criteria": lambda c: c.get('lut', [])[2] == 1,
            "success_msg": "✓ Row 2 programmed."
        },
        {
            "title": "Program Row 3 (1,1)",
            "instruction": "For Input **1 1**, we want 1 XOR 1 = 0. Set the output for Row 11 to **0**.",
            "criteria": lambda c: c.get('lut', [])[3] == 0,
            "success_msg": "✓ Row 3 programmed. The Truth Table is complete!"
        },
        {
            "title": "Verify Test Case 1",
            "instruction": "Set **Input A = 0, B = 1**. Verify Output is 1.",
            "criteria": lambda c: c.get('in_a') == 0 and c.get('in_b') == 1 and c.get('out') == 1,
            "success_msg": "✓ 0 XOR 1 = 1 verified."
        },
        {
            "title": "Verify Test Case 2",
            "instruction": "Set **Input A = 1, B = 1**. Verify Output is 0.",
            "criteria": lambda c: c.get('in_a') == 1 and c.get('in_b') == 1 and c.get('out') == 0,
            "success_msg": "✓ 1 XOR 1 = 0 verified."
        },
        {
            "title": "Reprogram: Implement OR Gate",
            "instruction": "Now let's change the hardware instantly! Change Row 11 (Input 1,1) to output **1**. This makes it an OR gate (0,1,1,1).",
            "criteria": lambda c: c.get('lut', [])[3] == 1,
            "success_msg": "✓ Reprogrammed! The hardware is now an OR gate."
        },
        {
            "title": "Verify OR Logic",
            "instruction": "Set **Input A = 1, B = 1**. Output should now be 1.",
            "criteria": lambda c: c.get('in_a') == 1 and c.get('in_b') == 1 and c.get('out') == 1,
            "success_msg": "🎉 EXPERIMENT COMPLETE! You've seen how FPGAs can change their logic instantly by updating memory."
        }
    ]

    # LUT Memory: 4 rows for 2 inputs (A, B)
    if 'lut_mem' not in st.session_state: st.session_state.lut_mem = [0, 0, 0, 0]
    
    def simulation():
        st.markdown("""
        <p style='color: #94a3b8; font-size: 1.05rem; margin-bottom: 2rem;'>
            Configure a **Look-Up Table (LUT)**, the core building block of an FPGA. 
            Define the output for every possible input combination to create any logic function.
        </p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### 💾 LUT Configuration")
            st.caption("Define the Truth Table for your custom logic.")
            
            # Custom Truth Table Input
            for i in range(4):
                # Convert i to binary string for label
                bin_str = format(i, '02b')
                a_val = int(bin_str[0])
                b_val = int(bin_str[1])
                
                c1, c2 = st.columns([1, 1])
                with c1:
                    st.markdown(f"**Input {bin_str}** (A={a_val}, B={b_val})")
                with c2:
                    st.session_state.lut_mem[i] = st.selectbox(f"Output for {bin_str}", [0, 1], key=f"lut_{i}")
                    
        with col2:
            st.markdown("### 🧪 Test Bench")
            in_a = st.radio("Input A", [0, 1], horizontal=True, key="fpga_in_a")
            in_b = st.radio("Input B", [0, 1], horizontal=True, key="fpga_in_b")
            
            # Calculate Address
            addr = (in_a << 1) | in_b
            
            # Fetch from LUT
            out = st.session_state.lut_mem[addr]
            
            st.markdown("---")
            st.markdown(f"**LUT Address**: `{format(addr, '02b')}`")
            st.metric("FPGA Output", out)
            
            # Visualizing the active row
            st.markdown("#### Active Memory Cell")
            st.markdown(f"""
            <div style='text-align: center; padding: 1rem; border: 1px solid #475569; border-radius: 8px;'>
                Row {addr}: <b>{out}</b>
            </div>
            """, unsafe_allow_html=True)

        return {
            "lut": st.session_state.lut_mem,
            "in_a": in_a,
            "in_b": in_b,
            "out": out
        }

    theory = """
    ### Field Programmable Gate Arrays (FPGAs)
    
    **Overview**: FPGAs are the pinnacle of reconfigurable hardware. Unlike PLDs, they contain thousands to millions of logic blocks.
    
    **Key Components:**
    1.  **LUT (Look-Up Table)**: The atomic unit of an FPGA.
        -   It's actually a small RAM (e.g., 16x1 bits for a 4-input LUT).
        -   To implement a logic gate (AND, OR, XOR), we simply write its Truth Table into this RAM.
        -   **Power**: Any n-input Boolean function can be implemented by a single n-input LUT.
        
    2.  **CLB (Configurable Logic Block)**:
        -   Contains LUTs, Flip-Flops (for sequential logic), and Multiplexers.
        
    3.  **Routing Matrix**:
        -   Programmable wires that connect CLBs together.
        
    **FPGA vs CPU vs ASIC:**
    -   **CPU**: General purpose, executes instructions sequentially (Slowest).
    -   **FPGA**: Parallel hardware execution, reconfigurable (Fast).
    -   **ASIC**: Custom silicon chip, not reconfigurable (Fastest, most expensive).
    
    **Applications**:
    -   AI/Machine Learning acceleration
    -   High-frequency trading
    -   Video processing
    -   Prototyping new chips
    """
    
    if 'u5_ex12_ctx' not in st.session_state: st.session_state.u5_ex12_ctx = {}
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u5_ex12_ctx = ctx
        return ctx

    render_experiment_layout("Experiment 12: FPGA Architecture", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u5_ex12", tutor_steps_config=tutor_config, tutor_context=st.session_state.u5_ex12_ctx)
