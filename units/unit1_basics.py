import streamlit as st
from utils import render_experiment_layout, show_theory, show_success_message, render_circuit_image
from tutor import SmartTutor
from circuits import draw_logic_gate

def render():
    st.title("Unit 1: Basics of Digital Logic")
    
    tutor = SmartTutor()
    
    tab1, tab2 = st.tabs(["Experiment 1: Logic Gates", "Experiment 2: Boolean Algebra & K-Map"])
    
    with tab1:
        run_experiment_1(tutor)
        
    with tab2:
        run_experiment_2(tutor)

def run_experiment_1(tutor):
    # Comprehensive 30-minute Logic Gate Exploration with Micro-Experiments
    tutor_config = [
        {
            "title": "Introduction: Understanding Logic Levels",
            "instruction": "Select the **AND** gate. Before testing, understand that 0 represents LOW voltage (0V) and 1 represents HIGH voltage (typically 5V in TTL logic).",
            "criteria": lambda c: c.get('gate') == 'AND',
            "success_msg": "✓ AND gate selected. You're about to discover how digital logic works at the hardware level!",
            "hint": "Logic gates are the building blocks of all digital computers."
        },
        {
            "title": "AND Gate - Micro-Experiment 1: All Inputs LOW",
            "instruction": "Set **Input A = 0** and **Input B = 0**. This tests the 'both false' condition. What do you predict the output will be?",
            "criteria": lambda c: c.get('gate') == 'AND' and c.get('in_a') == 0 and c.get('in_b') == 0,
            "success_msg": "✓ Verified: 0 AND 0 = 0. When ALL inputs are LOW, AND gate output is LOW.",
            "hint": "AND requires ALL inputs to be HIGH to produce a HIGH output."
        },
        {
            "title": "AND Gate - Micro-Experiment 2: Mixed Inputs (Low, High)",
            "instruction": "Set **Input A = 0** and **Input B = 1**. One input is LOW, one is HIGH. Predict the output before observing.",
            "criteria": lambda c: c.get('gate') == 'AND' and c.get('in_a') == 0 and c.get('in_b') == 1,
            "success_msg": "✓ Verified: 0 AND 1 = 0. Even ONE LOW input makes the output LOW. This is the AND condition!",
        },
        {
            "title": "AND Gate - Micro-Experiment 3: Reversed Mixed Inputs",
            "instruction": "Now set **Input A = 1** and **Input B = 0**. This tests commutativity (A AND B = B AND A). Does order matter?",
            "criteria": lambda c: c.get('gate') == 'AND' and c.get('in_a') == 1 and c.get('in_b') == 0,
            "success_msg": "✓ Confirmed: 1 AND 0 = 0. AND operation is commutative - order doesn't matter!",
            "hint": "Mathematical property: AND is symmetric."
        },
        {
            "title": "AND Gate - The Golden Case: All Inputs HIGH",
            "instruction": "Set **Input A = 1** and **Input B = 1**. This is the ONLY case where AND produces HIGH. Verify it!",
            "criteria": lambda c: c.get('gate') == 'AND' and c.get('in_a') == 1 and c.get('in_b') == 1 and c.get('out') == 1,
            "success_msg": "✓ Perfect! 1 AND 1 = 1. This is the unique HIGH output case for AND. Memorize this truth table!",
        },
        {
            "title": "OR Gate - Switching Context",
            "instruction": "Switch to the **OR** gate. Reset both inputs to **A = 0, B = 0**. How do you think OR differs from AND?",
            "criteria": lambda c: c.get('gate') == 'OR' and c.get('in_a') == 0 and c.get('in_b') == 0,
            "success_msg": "✓ OR gate selected and cleared. OR produces HIGH if AT LEAST ONE input is HIGH.",
            "hint": "OR is the opposite philosophy of AND."
        },
        {
            "title": "OR Gate - Micro-Experiment: First Activation",
            "instruction": "Keep **A = 0**, set **B = 1**. With just ONE HIGH input, the OR gate should activate. Test it!",
            "criteria": lambda c: c.get('gate') == 'OR' and c.get('in_a') == 0 and c.get('in_b') == 1 and c.get('out') == 1,
            "success_msg": "✓ Excellent! 0 OR 1 = 1. OR needs ONLY ONE HIGH to output HIGH (contrast with AND).",
        },
        {
            "title": "OR Gate - Testing Both HIGH",
            "instruction": "Set **A = 1, B = 1**. Unlike AND where this was unique, for OR this is just another HIGH state. Verify!",
            "criteria": lambda c: c.get('gate') == 'OR' and c.get('in_a') == 1 and c.get('in_b') == 1 and c.get('out') == 1,
            "success_msg": "✓ 1 OR 1 = 1. OR is inclusive - 'either or both' produces HIGH.",
        },
        {
            "title": "NOT Gate - Inversion Exploration",
            "instruction": "Switch to **NOT** gate. Set **Input A = 0**. NOT is a unary operator (only one input). It inverts the signal.",
            "criteria": lambda c: c.get('gate') == 'NOT' and c.get('in_a') == 0 and c.get('out') == 1,
            "success_msg": "✓ NOT 0 = 1. Inversion verified! NOT flips the bit - this is digital negation.",
            "hint": "NOT is also called an inverter. Essential for creating complemented variables."
        },
        {
            "title": "NOT Gate - Complete the Inversion Test",
            "instruction": "Set **Input A = 1**. The output should flip to 0. This completes the NOT truth table.",
            "criteria": lambda c: c.get('gate') == 'NOT' and c.get('in_a') == 1 and c.get('out') == 0,
            "success_msg": "✓ NOT 1 = 0. Perfect inversion! NOT is used everywhere in digital logic.",
        },
        {
            "title": "XOR Gate - The Inequality Detector",
            "instruction": "Switch to **XOR** (Exclusive OR). Set **A = 1, B = 0**. XOR outputs HIGH only when inputs are DIFFERENT.",
            "criteria": lambda c: c.get('gate') == 'XOR' and c.get('in_a') == 1 and c.get('in_b') == 0 and c.get('out') == 1,
            "success_msg": "✓ 1 XOR 0 = 1. Inputs are different, so XOR is HIGH. This detects inequality!",
            "hint": "XOR = eXclusive OR. Different inputs → HIGH."
        },
        {
            "title": "XOR Gate - Testing Equality",
            "instruction": "Set **A = 1, B = 1**. When both inputs are the SAME, XOR outputs LOW. Verify this property!",
            "criteria": lambda c: c.get('gate') == 'XOR' and c.get('in_a') == 1 and c.get('in_b') == 1 and c.get('out') == 0,
            "success_msg": "✓ 1 XOR 1 = 0. Same inputs → LOW. XOR is used in parity checking and binary addition!",
        },
        {
            "title": "NAND Gate - Universal Gate Discovery",
            "instruction": "Switch to **NAND** (NOT-AND). Set **A = 1, B = 1**. NAND is AND followed by NOT. What's the output?",
            "criteria": lambda c: c.get('gate') == 'NAND' and c.get('in_a') == 1 and c.get('in_b') == 1 and c.get('out') == 0,
            "success_msg": "✓ NAND(1,1) = 0. It's the opposite of AND(1,1)=1. NAND can build ANY logic circuit!",
            "hint": "NAND is called a 'universal gate' - you can build every other gate using only NAND."
        },
        {
            "title": "NAND Gate - Exploring Other States",
            "instruction": "Set **A = 0, B = 0**. Since AND(0,0)=0, what will NAND(0,0) be? Test your prediction!",
            "criteria": lambda c: c.get('gate') == 'NAND' and c.get('in_a') == 0 and c.get('in_b') == 0 and c.get('out') == 1,
            "success_msg": "✓ NAND(0,0) = 1. It's NOT of AND(0,0)=0. NAND inverts the AND output!",
        },
        {
            "title": "NOR Gate - The Other Universal",
            "instruction": "Switch to **NOR** (NOT-OR). Set **A = 0, B = 0**. Since OR(0,0)=0, what's NOR(0,0)?",
            "criteria": lambda c: c.get('gate') == 'NOR' and c.get('in_a') == 0 and c.get('in_b') == 0 and c.get('out') == 1,
            "success_msg": "✓ NOR(0,0) = 1. NOR is also universal - you can build all gates with just NOR!",
        },
        {
            "title": "FINAL CHALLENGE: Compare AND vs OR vs XOR",
            "instruction": "Go back to **AND** gate and set A=1, B=1. Remember: AND=1, OR=1, XOR=0, NAND=0, NOR=0 for inputs (1,1). You've mastered all basic gates!",
            "criteria": lambda c: c.get('gate') == 'AND' and c.get('in_a') == 1 and c.get('in_b') == 1,
            "success_msg": "🎉 CONGRATULATIONS! You've completed a comprehensive analysis of all 6 fundamental logic gates. You now understand the building blocks of every digital computer!",
        }
    ]

    def simulation():
        st.markdown("""
        <p style='color: #94a3b8; font-size: 1.05rem; margin-bottom: 2rem;'>
            <b>Objective:</b> Systematically analyze the behavioral properties of fundamental logic gates through hands-on micro-experiments. 
            Complete all experiments to understand how computers process information at the lowest level.
        </p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1.2, 2])
        
        with col1:
            st.markdown("### ⚙️ Parameters")
            gate_type = st.selectbox("Logic Gate", ["AND", "OR", "NOT", "NAND", "NOR", "XOR"], 
                                     help="Select the logic function to analyze")
            
            st.markdown("---")
            st.markdown("#### Signal Inputs")
            
            input_a = st.radio("Input A", [0, 1], horizontal=True, key="u1_in_a")
            
            if gate_type != "NOT":
                input_b = st.radio("Input B", [0, 1], horizontal=True, key="u1_in_b")
            else:
                input_b = 0 # Dummy value
                st.info("ℹ️ NOT gate is a unary operator (single input).")
                
        with col2:
            st.markdown("### 🔬 Oscilloscope / Circuit")
            
            # Logic Calculation
            output = 0
            if gate_type == "AND": output = input_a and input_b
            elif gate_type == "OR": output = input_a or input_b
            elif gate_type == "NOT": output = not input_a
            elif gate_type == "NAND": output = not (input_a and input_b)
            elif gate_type == "NOR": output = not (input_a or input_b)
            elif gate_type == "XOR": output = input_a ^ input_b
            
            output = int(output)
            
            # Draw Circuit
            inputs = [input_a]
            if gate_type != "NOT": inputs.append(input_b)
            
            img_buf = draw_logic_gate(gate_type, inputs, output)
            render_circuit_image(img_buf)
            
            st.markdown("<br/>", unsafe_allow_html=True)
            
            # Digital Analyzer View
            c1, c2, c3 = st.columns(3)
            with c1: 
                st.markdown(f"""
                <div class='lab-box' style='text-align: center; background: {"rgba(59, 130, 246, 0.2)" if input_a else "rgba(30, 41, 59, 0.5)"};'>
                    <p style='color: #94a3b8; margin: 0; font-size: 0.9rem;'>Input A</p>
                    <p style='font-size: 2.5rem; font-weight: bold; color: {"#60a5fa" if input_a else "#64748b"}; margin: 0.5rem 0;'>{input_a}</p>
                </div>
                """, unsafe_allow_html=True)
            with c2: 
                if gate_type != "NOT":
                    st.markdown(f"""
                    <div class='lab-box' style='text-align: center; background: {"rgba(139, 92, 246, 0.2)" if input_b else "rgba(30, 41, 59, 0.5)"};'>
                        <p style='color: #94a3b8; margin: 0; font-size: 0.9rem;'>Input B</p>
                        <p style='font-size: 2.5rem; font-weight: bold; color: {"#a78bfa" if input_b else "#64748b"}; margin: 0.5rem 0;'>{input_b}</p>
                    </div>
                    """, unsafe_allow_html=True)
            with c3:
                st.markdown(f"""
                <div class='lab-box' style='text-align: center; background: {"rgba(34, 197, 94, 0.2)" if output else "rgba(30, 41, 59, 0.5)"};'>
                    <p style='color: #94a3b8; margin: 0; font-size: 0.9rem;'>Output Y</p>
                    <p style='font-size: 2.5rem; font-weight: bold; color: {"#22c55e" if output else "#64748b"}; margin: 0.5rem 0;'>{output}</p>
                </div>
                """, unsafe_allow_html=True)

        # Context for Tutor
        context = {
            "gate": gate_type,
            "in_a": input_a,
            "in_b": input_b,
            "out": output
        }
        return context

    theory = """
    ### Logic Gates: The Foundation of Computing
    
    **Historical Context**: In the 1940s, Claude Shannon proved that Boolean algebra could represent switching circuits. This insight led to all modern digital computers.
    
    **The Six Fundamental Gates:**
    1. **AND**: All inputs HIGH → Output HIGH (multiplication in Boolean algebra)
    2. **OR**: Any input HIGH → Output HIGH (addition in Boolean algebra)
    3. **NOT**: Inverts signal (complementation)
    4. **NAND**: NOT-AND (Universal gate - can build everything)
    5. **NOR**: NOT-OR (Also universal)
    6. **XOR**: Exclusive OR (inequality/difference detector)
    
    **Real-World Applications:**
    - **CPU ALU**: Uses XOR for binary addition, AND/OR for logical operations
    - **Memory**: Built entirely from NAND or NOR gates
    - **Error Detection**: XOR used in parity checking
    
    **Advanced Concepts:**
    - **Universal Gates**: NAND and NOR can implement any Boolean function
    - **Gate Delay**: Real gates have propagation delay (~nanoseconds)
    - **Power Consumption**: Static (leakage) vs Dynamic (switching) power
    """
    
    if 'u1_ex1_ctx' not in st.session_state: st.session_state.u1_ex1_ctx = {}
    
    def wrapped_simulation():
        ctx = simulation()
        st.session_state.u1_ex1_ctx = ctx
        return ctx
        
    render_experiment_layout(
        "Experiment 1: Logic Gate Analysis", 
        theory, 
        wrapped_simulation, 
        tutor=tutor, 
        tutor_unit_id="u1_ex1", 
        tutor_steps_config=tutor_config, 
        tutor_context=st.session_state.u1_ex1_ctx
    )

def run_experiment_2(tutor):
    # Enhanced K-Map with 10+ guided steps
    tutor_config = [
        {
            "title": "Understanding the Problem",
            "instruction": "You need to implement F(A,B,C,D) = Σ(0,1,2,4,5,6,8,9,12,13,14). This means the function outputs '1' for these decimal inputs.",
            "criteria": lambda c: True,
            "success_msg": "✓ Problem understood. You'll use a K-Map to visualize and simplify this function.",
            "hint": "K-Maps group adjacent 1s to eliminate variables."
        },
        {
            "title": "Familiarize with K-Map Layout",
            "instruction": "The K-Map uses Gray Code ordering where adjacent cells differ by only 1 bit. Rows are AB, columns are CD.",
            "criteria": lambda c: True,
            "success_msg": "✓ K-Map structure understood. Gray code enables grouping!"
        },
        {
            "title": "Mark Minterm 0 (0000)",
            "instruction": "Click the cell at AB=00, CD=00 (top-left) to mark minterm 0. This represents A'B'C'D'.",
            "criteria": lambda c: 0 in c.get('marked', set()),
            "success_msg": "✓ Minterm 0 marked!",
            "hint": "Minterm 0 is when all variables are LOW."
        },
        {
            "title": "Mark Minterm 1 (0001)",
            "instruction": "Mark AB=00, CD=01 (second cell in top row). This is minterm 1.",
            "criteria": lambda c: 0 in c.get('marked', set()) and 1 in c.get('marked', set()),
            "success_msg": "✓ Minterms 0 and 1 marked. Notice they're adjacent!"
        },
        {
            "title": "Continue Marking: Minterm 2",
            "instruction": "Mark minterm 2 at AB=00, CD=11 (fourth cell in top row).",
            "criteria": lambda c: 2 in c.get('marked', set()),
            "success_msg": "✓ Minterm 2 added."
        },
        {
            "title": "Mark Row 2: Minterms 4, 5, 6",
            "instruction": "Mark cells for minterms 4, 5, and 6 in the second row (AB=01).",
            "criteria": lambda c: 4 in c.get('marked', set()) and 5 in c.get('marked', set()) and 6 in c.get('marked', set()),
            "success_msg": "✓ Second row partially filled!"
        },
        {
            "title": "Mark Bottom Row: Minterms 8, 9",
            "instruction": "Mark minterms 8 and 9 in the bottom row (AB=10, CD=00 and CD=01).",
            "criteria": lambda c: 8 in c.get('marked', set()) and 9 in c.get('marked', set()),
            "success_msg": "✓ Bottom row started."
        },
        {
            "title": "Mark Third Row: Minterms 12, 13, 14",
            "instruction": "Mark the remaining minterms 12, 13, 14 in row AB=11.",
            "criteria": lambda c: 12 in c.get('marked', set()) and 13 in c.get('marked', set()) and 14 in c.get('marked', set()),
            "success_msg": "✓ All minterms marked!"
        },
        {
            "title": "Verify Complete Marking",
            "instruction": "Check that you have exactly 11 cells marked (the 11 minterms). Count them!",
            "criteria": lambda c: len(c.get('marked', set())) == 11,
            "success_msg": "✓ All 11 minterms present. Ready for grouping analysis!"
        },
        {
            "title": "Submit Your Solution",
            "instruction": "Click **Check Solution** to verify your K-Map matches the target function.",
            "criteria": lambda c: c.get('marked', set()) == {0,1,2,4,5,6,8,9,12,13,14},
            "success_msg": "🎉 Perfect K-Map! You've successfully mapped the Boolean function. Next step would be finding prime implicants to minimize the expression.",
            "hint": "Make sure you have EXACTLY the minterms: 0,1,2,4,5,6,8,9,12,13,14"
        }
    ]
    
    if 'u1_ex2_ctx' not in st.session_state: st.session_state.u1_ex2_ctx = {}
    
    # Target minterms for F(A,B,C,D)
    target_minterms = {0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14}
    
    def simulation():
        st.info("📋 **Task**: Minimize the function **F(A,B,C,D) = Σ(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14)**")
        st.markdown("Toggle the cells in the Karnaugh Map below to match the minterms.")
        
        # Initialize K-Map state (4x4 grid)
        if 'kmap_grid' not in st.session_state:
            st.session_state.kmap_grid = [0]*16
            
        # K-Map Layout (Gray Code order)
        grid_map = [
            [0, 1, 3, 2],
            [4, 5, 7, 6],
            [12, 13, 15, 14],
            [8, 9, 11, 10]
        ]
        
        row_labels = ["00", "01", "11", "10"]
        col_labels = ["00", "01", "11", "10"]
        
        # Render Grid
        cols = st.columns([0.5, 1, 1, 1, 1])
        cols[0].markdown("**AB \\\\ CD**")
        for i, label in enumerate(col_labels):
            cols[i+1].markdown(f"**{label}**")
            
        for r, row_label in enumerate(row_labels):
            row_cols = st.columns([0.5, 1, 1, 1, 1])
            row_cols[0].markdown(f"**{row_label}**")
            for c in range(4):
                minterm = grid_map[r][c]
                key = f"cell_{minterm}"
                
                val = st.session_state.kmap_grid[minterm]
                label = "1" if val else "0"
                style = "background: rgba(34, 197, 94, 0.3); color: #22c55e; font-weight: bold;" if val else ""
                
                if row_cols[c+1].button(label, key=key, use_container_width=True):
                    st.session_state.kmap_grid[minterm] = 1 - val
                    st.rerun()

        # Get current marked cells
        user_minterms = {i for i, x in enumerate(st.session_state.kmap_grid) if x == 1}
        
        st.markdown(f"**Currently Marked**: {sorted(user_minterms) if user_minterms else 'None'} ({len(user_minterms)}/11)")
        
        if st.button("Check Solution"):
            if user_minterms == target_minterms:
                st.success("✅ **Perfect!** You've correctly mapped all minterms. K-Map is complete!")
                st.balloons()
                tutor.mark_completed("Unit 1", "Experiment 2")
            else:
                missing = target_minterms - user_minterms
                extra = user_minterms - target_minterms
                msg = "❌ Incorrect."
                if missing: 
                    msg += f" **Missing minterms**: {sorted(missing)}"
                if extra: 
                    msg += f" **Extra minterms**: {sorted(extra)}"
                st.error(msg)
        
        return {
            "marked": user_minterms
        }

    theory = """
    ### Karnaugh Maps: Visual Boolean Minimization
    
    **Purpose**: K-Maps provide a graphical method to simplify Boolean expressions without algebra.
    
    **Key Concepts:**
    1. **Gray Code**: Adjacent cells differ by exactly 1 bit
    2. **Grouping**: Powers of 2 (1, 2, 4, 8, 16 cells)
    3. **Wraparound**: Edges connect (toroidal topology)
    
    **Minimization Rules:**
    - Group largest possible power-of-2 rectangles
    - Each group eliminates variables
    - Overlapping groups allowed
    - All 1s must be covered
    
    **Real Applications:**
    - FPGA synthesis tools
    - Hardware optimization
    - PLA/PAL programming
    """
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u1_ex2_ctx = ctx
        return ctx
    
    render_experiment_layout("Experiment 2: Boolean Algebra & K-Map", theory, wrapped_sim, tutor,
                             tutor_unit_id="u1_ex2", tutor_steps_config=tutor_config, tutor_context=st.session_state.u1_ex2_ctx)
